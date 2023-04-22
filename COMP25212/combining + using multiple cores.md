[[COMP25212]]

### ~ distributed memory vs shared memory
- ==distributed memory== - each core has its own ==independent memory==
- within distributed memory, communication / synchronisation must be coded explicitly
- ==shared memory== - all cores have the same view of memory, making communication / sync implicit
- shared memory is easier to program, and generally considered the ideal option for general CPUs

### ~ separate tasks vs parallel programming
- separate tasks - different cores in a processor handle complete different tasks, meaning they typically wouldn't interfere with eachother e.g. 1 core runs the OS, another core runs a browser, another runs another program etc
- parallel programming - utilised when wanting to utilise multiple cores on a ==single application==, and common approaches include shared memory, message passing, independent threads etc

### ~ exemplar multicore architectures
![ | 450](https://i.imgur.com/2M21hbc.png)
- a common approach is to have shared L3 caches, and separate L1s / L2s
![](https://i.imgur.com/QyIFVnx.png)
- the same idea can be seen in this i7 chip