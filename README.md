
# Welcome to your CDK Python project!

# Instructions

1. [Create AWS account, setup AWS CDK, and setup IAM Identity](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

> [!WARNING]
> This can be the most time-consuming part. Make sure to use AWS CLI v2 and carefully follow the steps.

2. Bootstrap

```
cdk bootstrap \
   -c model="distilbert-base-uncased-finetuned-sst-2-english" \
   -c task="text-classification"
```

3. Deploy

```
cdk deploy \
   -c model="distilbert-base-uncased-finetuned-sst-2-english" \
   -c task="text-classification"
```

Test your endpoint with curl:

```
curl --request POST \
  --url {HuggingfaceSagemakerEndpoint.hfapigwEndpointE75D67B4} \
  --header 'Content-Type: application/json' \
  --data '{
	"inputs": "Hugging Face, the winner of VentureBeat’s Innovation in Natural Language Process/Understanding Award for 2021, is looking to level the playing field. The team, launched by Clément Delangue and Julien Chaumond in 2016, was recognized for its work in democratizing NLP, the global market value for which is expected to hit $35.1 billion by 2026. This week, Google’s former head of Ethical AI Margaret Mitchell joined the team."
}'

# Background

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
