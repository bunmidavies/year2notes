[[COMP25212]]

### definition
- in fine-grained threading, the processor will switch between threads every few cycles, if not every cycle - it is the number of cycles before a switch takes place which is what is described as being fine in ==granularity== here
- this means thread switches occur much more commonly than in [[coarse-grained multithreading]] - this means ==instantaneous thread switching== is typically required, which involves complex hardware
- in terms of which threads get switched, ==round robin== switching is the typical policy

### summary
- pipeline resources are better utilised, resulting in ==better overall performance==
- short stalls no longer have a negative impact, since instructions can be executed from other threads within that time
- each thread will perceive that it is being executed slower - since instructions from other threads are overlapped with eachother - but the overall performance is better
- an ==instantaneous== thread switching mechanism is required (which is expensive)

![ | 450 ](https://i.imgur.com/y5Cpz3U.png)
![ | 450](https://i.imgur.com/jWbtSL7.png)
