[[COMP22111]]
following on from [[GPUs]]

***
#### which applications for CPU / GPU

- CPU for sequential code where latency matters. When code contains a lot of ==control flow==, CPUs are best suited
  
- GPU for parallel problems where extra throughput is beneficial. Little ==control flow== or ==synchronization== should be required for these tasks to be suitable, and preferably ==number crunching== should be involved

The best applications will find places to utilise both ==sequential code== and ==concurrency== (**heterogeneous computing**)

Open Computing Language (OpenCL) provides a framework for providing heterogeneous systems

***

#### when to use FPGA?

FPGAs can work as a CPU or a GPU - when pipelining can be applied to large datasets, and processing information is involved (as well as this data potentially being of a custom type), FPGA is ==well suited==

FPGA is also very good in ==bit fiddling== operations e.g. compression, crypto

Typically, if the tasks involve a limited number of small tasks repeatedly performed in parallel, FPGA can be suitable due to its low power consumption

***

#### power consumption
![](https://i.imgur.com/7NFiRzl.png)

for lower wattage, FPGAs are able to perform many more operations per seconds, allowing for both efficiency at low power