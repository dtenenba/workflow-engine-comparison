# Nextflow on AWS Batch

## Prerequisites

* Java 1.8 or higher
* [Install Nextflow](https://www.nextflow.io/docs/latest/getstarted.html#installation)
* [Create an AMI](https://www.nextflow.io/docs/latest/awscloud.html#custom-ami) which has the AWS CLI pre-installed so that Nextflow can mount it and have it available regardless of whether the container being run has it, then create a compute environment based on that AMI, and a queue containing that compute environment. This has already been done in the SciComp AWS account.
* If you have multiple AWS profiles in your `~/.aws/config`, you need to work around an [issue](https://github.com/nextflow-io/nextflow/issues/860) by running:

```
export AWS_PROFILE=[your-profile-name]
pip install pipenv # if you don't have pipenv
pipenv install
pipenv shell
eval $(python3 hack.py)
```

## Running a sample job

`main.nf` defines another simple `hello world` job, only it uses `channels`, which in the AWS Batch context means 
each of the 4 sub-jobs runs in its own container. 


```
nextflow run main.nf -w s3://dtenenba-test/nextflow
```



