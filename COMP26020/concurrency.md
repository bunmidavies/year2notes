[[COMP26020]]

### ~ definition
- ==concurrency = doing multiple tasks at the same time==
- in more abstract terms, concurrency essentially means 'parts' of 'computation' which happen at the same time - parts and computation could refer to instructions within a function, or threads within a program etc.
- concurrency is a key concept within multicore/parallel systems in order to achieve high performance, and solve problems occuring at large scales
- concurrency breaks the idea of ==atomicity== and computations being specifically ==ordered== 
- concurrency within software can be implemented via a number of different methods (more: comp25212 - [[software multithreading]])

### ~ threads
- threads are ==independent streams of computation== with a ==shared state== (i.e. shared memory)
- interactions between threads are implicit (since the memory is shared, one thread can technically communicate with another just by changing one of its variables), but coordination has to be explicit
- each thread has its own stack, registers and PC, 

### ~ processes
- processes are also independent streams of computation, but have ==their own memory space== 
- ==threads exist within processes== - this is why threads may be known as ==lightweight processes==, while the actual processes are known as being ==heavyweight==
- since processes are completely seperate, communication between each of them is explicit - ==message passing== is a common technique used to do this