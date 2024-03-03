import aws_cdk as core
import aws_cdk.assertions as assertions

from huggingface_sagemaker_snowflake_deployment.huggingface_sagemaker_snowflake_deployment_stack import HuggingfaceSagemakerSnowflakeDeploymentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in huggingface_sagemaker_snowflake_deployment/huggingface_sagemaker_snowflake_deployment_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HuggingfaceSagemakerSnowflakeDeploymentStack(app, "huggingface-sagemaker-snowflake-deployment")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
