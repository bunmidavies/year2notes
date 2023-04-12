[[COMP22111]]
following on from [[coprocessors]]

the GPU is a highly specific piece of hardware, which only speeds up graphics code. It does not transparently accelerate. ==Code must be rewritten to target GPUs== 

==FLOPs are a useful measure of computer performance, standing for Floating Point Operations Per Second==

Teraflops are more useful, with one teraflop representing $10^{12}$ floating point operations per second

Specific uses for GPUs include:
- graphics rendering
- matrix multiplication

A GPU essentially has 2000-2500 ALUs in a single processor, allowing you to execute thousands of operations in parallel. Therefore, many more threads of computation are run on a GPU in comparison to a CPU

GPUs have several hundred pipelines, or thousands of threads, in comparison to CPUs 10-20 pipelines / threads

Example GPU architecture (NVIDIA)
![](https://i.imgur.com/HzXc8NF.png)

- The individual blocks are known as 'stream multiprocessors'
- Register sets are shared by multiple threads
- There is a high memory bandwidth, due to parallelism

GPUs are focused on **throughput** in order to be efficient. They perform tasks which can tolerate a certain amount of latency
This means that ==GPUs do not need a cache==, as CPUs use them to minimise latency

==CPU = low latency, low throughput
GPU = high latency, high throughput==

more is explained within [[CPU vs GPU vs FPGA]]