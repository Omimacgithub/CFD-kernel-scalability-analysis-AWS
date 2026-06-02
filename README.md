# CFD-kernel-scalability-analysis-AWS
This project performs a comprehensive analysis of the AWS infrastructure tested on the **NAS Parallel Benchmark (NPB)** (a set of computational fluid dynamics (CFD) programs) for several kernels (CG and MG) and cluster (HPC and HTC) configurations.

## Context

This repository includes the scripts for executing the NAS Parallel Benchmark (NPB) on a HPC and HTC cluster configuration deployed on AWS with **CloudFormation** tool. The aim of this project is to **analyze the AWS infrastructure scalability** for several NPB workloads (CG as a communication-intensive workload and MG as a computation-intensive workload) as the number of CPU cores grows. Two main experiments were conducted:

- First, a comparison between HTC (instances deployed across multiple availability zones) and HPC (instances deployed within a single availability zone) was conducted for the communication-intensive CG kernel workload to evaluate the impact of instance affinity on performance.

- Secondly, compute instances (c7i) were evaluated against general-purpose instances (m5a) for the computation-intensive MG kernel workload to assess their cost-performance ratio.

# Conclusions

- **Instance affinity significantly impacts CG kernel performance**. HPC cluster instances are co-located within a single availability zone (inter-node distance ~meters), whereas HTC cluster instances span multiple availability zones (inter-node distance ~kilometers). This topological difference explains the superior performance of HPC clusters for communication-intensive workloads. While HTC clusters feature 25 Gbps network interfaces that could partially mitigate this disadvantage, the performance gap would widen for lower-bandwidth configurations.

- Compute instances (c7i) outperform, as expected, general-purpose instances (m5a) for the compute-intensive (MG kernel) workload. However, the performance advantage of c7i instances diminishes with increasing core count, likely due to the relatively lower performance scaling of c7i compared to m5a and increased memory overhead per process (given that c7i instances provide half the memory per vCPU of m5a instances). Consequently, **m5a instances may offer superior cost-effectiveness for compute-intensive workloads at higher core counts**.

## File tree

Repository files are organized as follows:

* `analysis.pdf` &rarr; Report with instance and kernel size choices for the experiments, as well as experiments results and analysis.
* `CGkernel` &rarr; Scripts and .out files for CG kernel experiments.
    - `plots` &rarr; Matplotlib scripts for visual representation of experiments results.
        * `CGbar.py` &rarr; Bar plot representation of experiments results for HTC and HPC clusters.
        * `CGbar2.py` &rarr; Bar plot representation of experiments results for HTC and HPC clusters with a different data aggregation.
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