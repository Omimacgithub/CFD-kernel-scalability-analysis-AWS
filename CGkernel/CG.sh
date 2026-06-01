#!/bin/bash
#
#SBATCH --job-name=NPB-CG
#SBATCH --output=NPB-CG.out
#SBATCH --partition=aws
#
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=1
#SBATCH -n 16
#SBATCH --mem-per-cpu=2G
#
module load mpi
NP=(1 2 4 8 16)
for np in "${NP[@]}"; do
  for i in {1..5}; do
    echo "----------------------"
    echo ""
    echo "----------------------"
    echo "------- I = $i -------"
    echo "----------------------"
    echo ""
    echo "----------------------"
    mpirun -np $np cg.C.x
  done
done
