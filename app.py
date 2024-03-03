#!/usr/bin/env python3
import os
from aws_cdk import App, Environment
from huggingface_sagemaker.huggingface_stack import HuggingfaceSagemaker

# Environment
# CDK_DEFAULT_ACCOUNT and CDK_DEFAULT_REGION are set based on the
# AWS profile specified using the --profile option.
my_environment = Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"])

app = App()
sagemaker = HuggingfaceSagemaker(app, "HuggingfaceSagemakerEndpoint", env=my_environment)

app.synth()
