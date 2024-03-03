from aws_cdk import (
    aws_sagemaker as sagemaker,
    Environment
)
from constructs import Construct
from .constants import LATEST_PYTORCH_VERSION, LATEST_TRANSFORMERS_VERSION, region_dict

def get_image_uri(
    region=None,
    transformmers_version=LATEST_TRANSFORMERS_VERSION,
    pytorch_version=LATEST_PYTORCH_VERSION,
    use_gpu=False,
):
    # Note: Update the repository URI if there is a Python 3.10 compatible image available.
    repository = f"{region_dict[region]}.dkr.ecr.{region}.amazonaws.com/huggingface-pytorch-inference"
    # Update the tag to reflect Python 3.10 (py310) if available
    tag = f"{pytorch_version}-transformers{transformmers_version}-{'gpu-py310-cu111' if use_gpu == True else 'cpu-py310'}-ubuntu20.04"
    return f"{repository}:{tag}"


def is_gpu_instance(instance_type):
    return True if instance_type.split(".")[1][0].lower() in ["p", "g"] else False


class SageMakerEndpointConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        env: Environment,
        huggingface_model: str,
        huggingface_task: str,
        execution_role_arn: str,
        instance_type: str,
    ) -> None:
        super().__init__(scope, construct_id)

        ##############################
        #     Construct Variables    #
        ##############################

        model_name = f'model-{huggingface_model.replace("_","-").replace("/","--")}'
        endpoint_config_name = f'config-{huggingface_model.replace("_","-").replace("/","--")}'
        endpoint_name = f'endpoint-{huggingface_model.replace("_","-").replace("/","--")}'

        # creates the image_uri based on the instance type and region
        use_gpu = is_gpu_instance(instance_type)
        image_uri = get_image_uri(region=env.region, use_gpu=use_gpu)

        # defines and creates container configuration for deployment
        container_environment = {"HF_MODEL_ID": huggingface_model, "HF_TASK": huggingface_task}
        container = sagemaker.CfnModel.ContainerDefinitionProperty(environment=container_environment, image=image_uri)

        # creates SageMaker Model Instance
        model = sagemaker.CfnModel(
            self,
            "hf_model",
            execution_role_arn=execution_role_arn,
            primary_container=container,
            model_name=model_name,
        )

        # Creates SageMaker Endpoint configurations
        endpoint_configuration = sagemaker.CfnEndpointConfig(
            self,
            "hf_endpoint_config",
            endpoint_config_name=endpoint_config_name,
            production_variants=[
                sagemaker.CfnEndpointConfig.ProductionVariantProperty(
                    initial_instance_count=1,
                    instance_type=instance_type,
                    model_name=model.model_name,
                    initial_variant_weight=1.0,
                    variant_name=model.model_name,
                )
            ],
        )

        # Creates Real-Time Endpoint
        endpoint = sagemaker.CfnEndpoint(
            self,
            "hf_endpoint",
            endpoint_name=endpoint_name,
            endpoint_config_name=endpoint_configuration.endpoint_config_name,
        )

        # adds depends on for different resources
        endpoint_configuration.node.add_dependency(model)
        endpoint.node.add_dependency(endpoint_configuration)

        # construct export values
        self.endpoint_name = endpoint.endpoint_name
