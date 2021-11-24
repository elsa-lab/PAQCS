# PAQCS ![Ubuntu](https://shields.io/badge/Ubuntu-16.04-orange) ![BoostCpp](https://shields.io/badge/Boost%20C++-1.58-green) ![Python_3.6](https://shields.io/badge/Python-3.6-blue)

This repository contains the source code for the paper, "PAQCS: Physical Design-aware Fault-tolerant Quantum Circuit Synthesis," IEEE Transactions on VLSI Systems, which is a backup from the [source](https://www.princeton.edu/~cad/download/PAQCS.tar.gz). You may want to refer the [original Readme file](https://github.com/elsa-lab/PAQCS/blob/main/Readme.original.txt).

In our paper, "Mapping Nearest Neighbor Compliant Quantum Circuits onto a 2-D Hexagonal Architecture," we reimplement PAQCS based on the original paper for a fair comparison in terms of execution time. Therefore, the numerical results reported in our paper may not be identical. Please refer to the guide for preparing PAQCS based on our implementation.

## Modification on the cost function of qubit placement [![commit](https://shields.io/badge/commit-2c48012-critical)](https://github.com/elsa-lab/PAQCS/commit/2c48012f386fe9577bd5c9728499941cb00111d5)

The snapshot of the content related to the cost function is shown as the following, therefore the modification is applied in order to be consistent with the content of the paper.

![costfunc](https://i.imgur.com/hoflx1q.png)

## Quick Start

Please refer [Real2QASM](https://github.com/elsa-lab/Real2QASM#quick-start) to prepare quantum circuits in the format of `QASM`.

```bash
$ sudo apt update
$ sudo apt install -y build-essential libboost-graph-dev
$ PAQCS=/path/to/paqcs
$ QASMS=/path/to/circuits/in/qasm
$ CIRCS=${PAQCS}/Log/circs
$ cd ${PAQCS}; make
$ mkdir -p ${CIRCS}; cd ${CIRCS}
$ for qasm in ${QASMS}/*.qasm; do python ${PAQCS}/script/convert.py ${qasm} | tee ${qasm##*/}.txt; done
$ cd ${PAQCS}/Log
$ for circ in ${CIRCS}/*.txt; do ${PAQCS}/dist/Debug/GNU-Linux-x86/paqcs ${circ} ${circ##*/}; done
```

## Usage

```
$ ./paqcs -h
<input file> <output file> <grid W> <grid H> <window size>
```

The fields `input file` and `output file` are required.

## Example

```
$ ./paqcs ${CIRCS}/hwb9_123.qasm.txt hwb9_123.qasm.txt
#qubit=9
#2qGate: 49777
(W,H)= (3,3)
window size=3, costB=87530, costR=16852, costU= 13446
 ***Synthesis Time=24.8995***
```

## Reference

If you use of PAQCS contributes to a published paper, please cite the following BibTeX entry.

```
@article{lin2014paqcs,
  title={PAQCS: Physical design-aware fault-tolerant quantum circuit synthesis},
  author={Lin, Chia-Chun and Sur-Kolay, Susmita and Jha, Niraj K},
  journal={IEEE Transactions on Very Large Scale Integration (VLSI) Systems},
  volume={23},
  number={7},
  pages={1221--1234},
  year={2014},
  publisher={IEEE}
}
```
