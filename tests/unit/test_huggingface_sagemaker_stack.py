from aws_cdk import Environment
import aws_cdk as core
import aws_cdk.assertions as assertions

from huggingface_sagemaker.huggingface_sagemaker_stack import HuggingfaceSagemakerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in huggingface_sagemaker_snowflake_deployment/huggingface_sagemaker_snowflake_deployment_stack.py
def test_sqs_queue_created():
    app = core.App()
    # env = Environment(account='123456789012', region='us-west-2')
    # stack = HuggingfaceSagemakerStack(app, "huggingface-sagemaker", env=env)
    stack = HuggingfaceSagemakerStack(app, "huggingface-sagemaker")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
