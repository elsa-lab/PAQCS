# Guidelines for Preparing PAQCS from NNCQC

In our paper, "Mapping Nearest Neighbor Compliant Quantum Circuits onto a 2-D Hexagonal Architecture," we reimplement PAQCS based on the original paper for a fair comparison in terms of execution time. Our implementation of PAQCS can be prepared from NNCQC.

## Quick Start

Before starting, please make sure that the building process of [NNCQC](https://github.com/elsa-lab/NNCQC) works smoothly.

```bash
$ NNCQC=/path/to/nncqc
$ QASMS=/path/to/circuits/in/qasm
$ sed -i 's/std::max/std::min/g' ${NNCQC}/src/placer/nncqc_placer.cpp
$ mkdir PAQCS_from_NNCQC_build; cd PAQCS_from_NNCQC_build
$ cmake ${NNCQC}; make -j4
$ for qasm in ${QASMS}/*.qasm; do ./nncqc -i ${qasm} -o ${qasm##*/} -m square -p nncqc -r nncqc; done
```

Please note that the grid type must switch from `hex` to `square`.

## Example

```
$ ./nncqc --input hwb9_304.qasm -m square -p nncqc -r nncqc
Warning: using default size of map.

<< Program Options >>
   Input QASM file: hwb9_304.qasm
  Output QASM file: output.qasm
Output layout file: map.layout
     Height of map: 14
      Width of map: 13
       Type of map: square
    Type of placer: nncqc
    Type of router: nncqc

<< Purposed layout >>
   82   67   41    7   52   27  145  169  131  132    6  170  171
   94   60    9   12  146  162  130  136  164   70   26  172  173
   34   10   13    5   96  156   95  128   64  160  116   18  174
   66   31    8   37  138   20   80   36   19   81  115  137  175
   16   22  142  117  163   33   32   35  104   57  113  102   72
   48  121  147   23  148  127  135   11   24   56  101  134  133
  166  149   17  106  120   46    2  114   14  129   47   28  158
  122  119  150  118  125  157  155    0  144   69  126   29  141
  109  165  105  152  111   97    1   39  143  140  112  159   25
  123  108  107  153  103   49   54  139   63   53   62   61   30
  124    3  167  168   91   50   76   68   92   84   15  161   21
  110   99   98   55  154   83   42   73   88  151   85   93  176
  177  100   75   78   51   77   43   38   65   58   86   79  178
  179  180    4   87   90   40   44   89   74   71   45   59  181

<< Selected look-ahead window size: 10 >>
<< Swap count after routing >>
Max #swap gates reuqired: 22402
 Actual #swap gates used: 5004
```

## Comparison Between the Original Implementation and Our Implementation

The following table shows the average improvement in UB, SWAP, and T among different types of benchmark circuits.

| Category |      UB |   SWAP |       T |
|:--------:|--------:|-------:|--------:|
|   Tiny   | -15.29% |  6.78% |  55.85% |
|   Small  |  -9.29% |  1.49% |   3.83% |
|  Medium  | -15.75% | -2.01% | -60.99% |
|   Large  | -10.65% |  2.55% | -76.47% |
|          |         |        |         |
|   Total  | -12.85% |  2.24% | -20.05% |

Where `UB` stands for the upper bound of the number of SWAP gates for making a circuit nearest neighbor compliant after applying global reordering strategy, `SWAP` the number of inserted SWAP gates after applying the local reordering strategy, and `T` the execution time.

For detailed numerical results of each benchmark circuit, please refer to [this spreadsheet](https://docs.google.com/spreadsheets/d/1OLfespZVpdhAm3e1DoJfWj5RmkiH0Yr7j8kqr9qzKR4/edit#gid=852549832).
