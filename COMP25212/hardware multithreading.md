[[COMP25212]]

### ~ definition
- the main idea behind hardware multithreading is that independent instructions can be found within ==independent processes== - in the case where a number of programs running all lack ==parallelism==, the idea is to allow multiple ==threads== to share a single processor
- the ability for hardware multithreading is built into the processor, and requires no extra software, as opposed to [[software multithreading]] - hardware multithreading mainly focuses on the architecture of the processor in order to exploit instruction level parallelism

- in order to allow multiple threads to share a single processor, and for thread switching to be performed quickly, ==hardware must be replicated for each thread== - this includes:
	- replicating registers
	- replicating PCs
	- replicating TLBs
- this is the main reason thread switching becomes quicker in comparison to the OS having to swap in and out of singular processes in [[software multithreading]] - there is extra hardware to support the swapping
- in terms of memory, [[virtual memory + page tables]] can be used to share memory among separate threads (synchronisation issues must be kept in mind), as well as cache (cache thrashing is a big issue to avoid)

![ | 450](https://i.imgur.com/j0fjw1g.png)

### how hardware multithreading appears to the OS
- each hardware thread appears as a ==virtual processor== in linux / windows / unix (thus, multiprocessor support is required from the OS)