# Cromwell on AWS Batch

## Prerequisites

* Access to the SciComp AWS account
* Java 1.8 available (and loaded with `ml Java/1.8.0_181` on shared systems)
* The Cromwell JAR file in the same directory as this README. Download it
  [here](https://github.com/broadinstitute/cromwell/releases/latest).
* AWS credentials available in `~/.aws`. If you have more than one
  AWS account described in your credentials files, specify the correct
  one by exporting its name as the variable `AWS_PROFILE`.
* AMI, Compute environments, queues, buckets, etc. already created in AWS Account.
  This was done 10/22/2018 with help from the following documents:
  * [Large scale genomics workflows on AWS](https://docs.opendata.aws/genomics-workflows/)
  * [Introduction on AWS Batch for genomics workflows](https://docs.opendata.aws/genomics-workflows/aws-batch/configure-aws-batch-start/)
  * [Using Cromwell with AWS Batch](http://awsfeed.com/post/179088681134/using-cromwell-with-aws-batch)

## Files:

* `aws.conf` is the configuration file that enables Cromwell to talk to Batch.
  This is where you define the AWS Batch Job Queue you want to use.
* `hello.wdl` is the description of the workflow you want to run. It's another
  simple `hello world` task. Note that the name of the Docker image you want  
  to use also goes here.
* `hello.inputs` is a JSON file that contains the value of a variable 
  referenced in `hello.wdl`. 

  ## To run:

  ```
  java -Dconfig.file=aws.conf -jar cromwell-36.jar run hello.wdl -i hello.inputs
  ```    

The output will be available in the S3 bucket/prefix referenced in `aws.conf`.

## Run a CWL job in Batch:

```
java -Dconfig.file=aws.conf -jar cromwell-36.jar run example.cwl -i example-job.yaml
```