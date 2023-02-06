[[COMP22111]]

==a coprocessor is a processor which provides specific/tailored functions for the CPU==

examples of coprocessors:
- [[DSPs]]
- FPUs (explained below)
- [[GPUs]]
- Machine Learning accelerators (as ML is more compute intensive than graphics)

these specific tasks may be processor intensive, so by offloading them to a coprocessor, system performance can be accelerated

coprocessors may also have a number of dedicated instructions within an ISA

examples of coprocessors operations for ARM include:
- data processing (CDP) - operations like floating point multiplication may be handled by a coprocessor
- register transfer (MCR/MRC) - values can be moved to/between ARM registers to coprocessor registers
- load/store (LDC/STC) - a coprocessor register value is moved to/from memory

==emulator trap== - if a coproccesor instruction is called but the required coprocessor doesn't exist, the instruction is treated like an illegal operation and throws an error. The OS can provide a software model for the missing coprocessor

the main disadvantage of an emulator trap is that a software implementation of a coprocessor instruction is probably much slower

regarding [[floating point processing]] / arithmetic, these operations can be handled within software using a floating-point library, but can also be handled with a ==floating point unit (FPU)==. What you use depends on how often you need these operations