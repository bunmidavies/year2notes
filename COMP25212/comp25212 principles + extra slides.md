[[COMP25212]]

### increasing bandwidth/throughput
- parallelism - by adding more units (i.e. bus, PCIe, disks), bandwidth can be increased
- the main tradeoff is more wieres/pins/space
- SIMD/superscalar

### interleaving
- essentially works like dual porting a system

### caching
- works well for 'typical' behaviour
- applications include:
	- computer main memory
	- page trasnlation
	- virtual memory pages
	- blocks on board disk drive
	-  branch prediction
	-  web browsers

### speculation
- instruction prefetching relies on most instructions being sequential, and is typically associated with pipelining
- instruction prefecthing is also improved by branch prediction

### synchronisation
- its important to give the appearance of keeping everything in the original order
- systems need to have a reliable means of synchronising parallel threads

### profiling
- standard concept in software involving finding where most of its time is spent - theres no point optimising rare events, therefore optimise the common features in the code
- architectural features are introduced in order to improve the execution of typical code

### benchmarks
- benchmarks exist to profile architecture for a specific application