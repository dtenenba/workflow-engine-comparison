# Workflow Engine Proofs of Concept

Testing various workflow engines on AWS Batch and Slurm (for now;
perhaps further testing to come on GCP and Azure).

## Background:

Some researchers at the Hutch are ready for more robust workflow engines 
to use with either Slurm or AWS Batch. Therefore we should be evaluating
engines which claim to work on both back ends. 

Here are the workflow engines that were evaluated:


|  Engine    | Source |  Written in | Workflow language(s) | Actively Maintained | Slurm support | AWS Batch Support | GCP Support | Azure Support | Notes                                                                   | 
|-----------|------|------|----------------------|---------------------|---------------|-------------------|-------------|---------------|-------------------------------------------------------------------------| 
| [Cromwell](https://github.com/broadinstitute/cromwell) | Broad Institute | Scala      | CWL/WDL              | ☑️                | ☑️          | ☑️              | ☑️        | ❌         | <sup>1</sup> | 
| [NextFlow](https://nextflow.io) | Center for Genomic Regulation (Spain) | Java       | Groovy DSL           | ☑️                | ☑️          | ☑️              | ❌       | ❌         | <sup>2</sup>              | 
| [Toil](https://github.com/DataBiosphere/toil)  | UCSC    | Python     | Python/CWL           | ☑️                | ☑️          | ❌             | ☑️        | ☑️          | <sup>3</sup>                                | 
| [Luigi](https://github.com/spotify/luigi)   | Spotify  | Python     | Python               | ☑️                | ❌         | ☑️              | ☑️        | ❌         |                                                                         | 
| [SciLuigi*](https://github.com/jgolob/sciluigi/tree/containertask) | Pharmbio (SE) / jgolob | Python     | Python               | ❌               | ☑️          | ☑️              | via luigi?  | ❌         | <sup>4</sup>     | 


<p><sup>1</sup> GCP support via Google Genomics Pipelines API.</p>
<p><sup>2</sup> Has Kubernetes support so that may allow it to work on GCP.</p>
<p><sup>3</sup> Runs on AWS (EC2, ECS(?), but not Batch).</p>
<p><sup>3</sup> *=jgolob's fork, `container-task` branch provides AWS Batch support, he and sminot are actively using it.</p>

## Contents of Repository

In this repository you should find a directory for each engine, 
each of which contains `batch` and `slurm` directories. In each you'll find a `README` with instructions and links, and files needed to run the examples.

## AWS Access

These examples assume you have administrator or otherwise high-level access
to the `SciComp` AWS account.

