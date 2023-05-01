[[COMP25212]]

### ~ intro
- clusters/supercomputers/datacentres all essentially refer to having a bunch of CPUs on a number of motherboards
- today, the terms are overloaded/misused, and any distinctions that existed between the tree continue to blur
- any of the three have typical common uses discussed below

### ~ high performance computing
- running one large task as quickly as possible - typically suited to ==supercomputers== but sometimes clusters

### ~ high throughput computing
- running as many tasks per unit of time as possible
- clusters/farms as well as datacentres are typically associated with this idea

### ~ big data analytics
- analysing and extracting patterns from large+complex datasets - fittingly, datacentres are mostly associated with this

### ~ building clusters/supercomputers/datacentres
- computers typically come in a small form factor, and since large numbers of these are piled together they're typically ==optimised for cooling and power efficiency==
- a rack will house 1000s of cores, and the upside of this is ==high redundancy== for ==fauly tolerance==
- to join racks together, things such as:
	- a network
	- power distribution
	- cooling
	- dedicated storage
- need to be added in, as well as a couple of "frontend" computers/nodes, which handle user functions

### ~ links
- [top 500 supercomputers](https://www.top500.org)
- [HPL benchmark](https://www.icl.utk.edu/files/print/2016/hpl-sc16.pdf)