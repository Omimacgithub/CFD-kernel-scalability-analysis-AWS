# CFD-kernel-scalability-analysis-AWS
This proyect performs a deep analysis of the AWS infrastructure tested on the **NAS Parallel Benchmark (NPB)** (a set of computational fluid dynamics (CFD) programs) for several kernels (CG and MG) and cluster (HPC and HTC) configurations.

## Context

This repository includes the scripts for executing the NAS Parallel Benchmark (NPB) on a HPC and HTC cluster configuration deployed on AWS with **CloudFormation** tool. The aim of this project is to analyze the infrastructure scalability for several NPB workloads (CG as a communication-intensive workload and MG as a computation-intensive workload) as the number of CPU cores grows. Two main experiments were conducted:

- Firstly, a comparison between HTC (instances deployed on several availability zones) and HPC (instances deployed on the same availability zone) clusters was made for a communication-intensive workload (CG kernel), in order to highlight the instance affinity relevance for communication-intensive workloads.

- Secondly, compute instances (c7i) were tested versus general purpose instances (m5a) for a computation-intensive workload (MG kernel), in order to demonstrate if compute instances price worth enough.

# Conclusions

- **Instance affinity matters for CG kernel performance**. Instances on HPC cluster are located on the same availability zone, so the distance between them is in order of meters, unlike HTC cluster, where the different availability zones are separated in order of kilometers/miles, that is the reason way **HPC cluster performs better**. Moreover, HTC cluster could fought with HPC cluster due to its 25 Gbps instances, if instances bandwidth were lower, the bigger the performance gap would be in favor to HPC cluster.

- Compute instances (c7i) outperforms, as expected, general purpose instances (m5a) for the compute-intensive (MG kernel) experiment. However, the execution time gap between them **decrease** when the number of cores increases. Reasons for this behaviour can be the lower performance gain of c7i compared to m5a and also the additional memory overhead when number of processes (cores) increases (remember that c7i instances memory is half of m5a instances). We conclude that m5a instances **are not worth enough** compared to c7i instances in terms of performance-price balance for computation-intensive workloads.

## File tree

Repository files are organized as follows:

* `analysis.pdf` &rarr; Report with instance and kernel size choices for the experiments, as well as experiments results and analysis.
* `CGkernel` &rarr; Scripts and .out files for CG kernel experiments.
    - `plots` &rarr; Matplotlib scripts for visual representation of experiments results.
        * `CGbar.py` &rarr; Bar plot representation of experiments results for HTC and HPC clusters.
        * `CGbar2.py` &rarr; Bar plot representation of experiments results for HTC and HPC clusters with a different data agrupation.
        * `CGlinesSpeedUp.py` &rarr; HPC and HTC clusters Speed Up comparison depending on number of CPU cores.
    - `out` &rarr; Raw experiments results.
        * `HPCcluster.out` &rarr; Raw HPC cluster experiment results.
        * `HTCcluster.out` &rarr; Raw HTC cluster experiment results.
    - `CG.sh` &rarr; Script for CG kernel experiment execution on a Slurm cluster.
    - `make.def` &rarr; Config file with benchmark compilation flags.
    - `suite.def` &rarr; Config file for compiling specific kernels with specific problem sizes.
* `MGkernel` &rarr; Scripts and .out files for MG kernel experiments.
    - `plots` &rarr; Matplotlib scripts for visual representation of experiments results.
        * `MGc6id.py` &rarr; Bar plot representation of experiments results for m5a and c6id clusters.
        * `MGc7i.py` &rarr; Bar plot representation of experiments results for m5a and c7i clusters.
        * `MGSpeedUpc7i.py` &rarr; m5a and c7i clusters Speed Up comparison depending on number of CPU cores.
    - `out` &rarr; Raw experiments results.
        * `c6idcluster.out` &rarr; Raw c6id cluster experiment results.
        * `c7icluster.out` &rarr; Raw c7i cluster experiment results.
        * `m5acluster.out` &rarr; Raw m5a cluster experiment results.
    - `MG.sh` &rarr; Script for MG kernel experiment execution on a Slurm cluster.
    - `make.def` &rarr; Config file with benchmark compilation flags.
    - `suite.def` &rarr; Config file for compiling specific kernels with specific problem sizes.
* `template.yaml` &rarr; Template for cluster configuration on AWS CloudFormation tool.