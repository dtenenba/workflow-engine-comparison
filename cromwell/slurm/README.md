# Cromwell on slurm

## Prerequisites

You must be on a `rhino` node or another node that can submit jobs
to our slurm clusters.

Load Java version 1.8 or higher:

`ml Java/1.8.0_181`

You need the most recent Cromwell JAR file, it can be downloaded from 
[here](https://github.com/broadinstitute/cromwell/releases/latest). 
These instructions assume the JAR file lives in the same directory as this `README`. We will refer to it as `cromwell-36.jar` even though the version
number may have gone up by the time you read this.


The `slurm.conf` file is what allows Cromwell and slurm to communicate.


`myWorkflow.wdl` is a simple task description written in 
[WDL](https://software.broadinstitute.org/wdl/documentation/)
 (Workflow Description Language), developed at the Broad Institute.
 It prints out the classic `hello world`.

 The command to run this task on the cluster is:

 ```
 java -Dconfig.file=slurm.conf -jar cromwell-36.jar run myWorkflow.wdl
 ```

You should see the output on the screen, as well as under the `cromwell-executions` directory created by the above command.

## Running a CWL job

Just to prove that we can run CWL jobs as well as WDL jobs, here's a quick example. `example.cwl` is another simple `echo` task, and `example-job.yaml`
provides the value of the variable referenced in the `cwl` file.

We can start the CWL job with the following command:

```
java -Dconfig.file=slurm.conf -jar cromwell-36.jar run example.cwl -i example-job.yaml
```
Once again, output is available under the `cromwell-executions` directory 
created by the above command.


