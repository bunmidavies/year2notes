[[COMP25212]]

### ~ definition
- GPU architecture is based on arrays of cores executing the same instruction on large amounts of data (a similar idea to [[SIMD instructions]], but even more 'enforced' or structured)
- GPUs have several arrays of cores - they are the best in terms of raw performance and efficiency, and this is partly due to it being specialised towards specific tasks
- general purpose GPUs i.e. GPGPUs are GPUs harnessed for their parallel processing capabilties, in an attempt to speed up general purpose computing tasks

### ~ limitations of GPGPUs
- the following limitations affect the performance which can be extracted for a GPU
	- moving data to/from memory is ==very expensive==
	- the memory accessed by all cores within an array needs to be consecutive (things like pointers make this difficult)
	- all cores execute the same instruction, meaning condtionals require both the `if` and `else` to be executed
	- programming models for GPUs differ significantly compared to programming models used for CPUs
- in short, not all generalised workloads can be ported efficiently to a GPU