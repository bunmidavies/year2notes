[[COMP25212]]

### definition
- as covered within the [[fetch-execute]] cycle, and showing the individual stages which exist within this ([[cycles of operation + stages]]), we've shown that certain ==blocks of logic== of a processor can be waiting within a cycle, not being utilised
- pipelining aims to utilise these blocks which typically wouldnt be used, and does this through inserting ==buffers in between stages==
![|450](https://i.imgur.com/LVknNqn.png)
- previously, the output of each stage was just sent to the next stage
- now, the output of each stage can now be stored in a buffer, meaning the stage can begin to start working on something else
- the buffers are clocked once per cycle
- this is similar to something like in a car production line, and results in 5x faster execution by increasing the ==clock frequency== by 5x
- ==note that only one instruction is still executed per cycle== - this isnt parallelism or anything

### effects of pipelining + real world pipelines
![](https://i.imgur.com/SSRJ4Rj.png)
- this is where the notion of ==5x faster execution== comes from - since the buffers are clocked every cycle, the result essentially needs to be stored with each clock cycle
- what is important here is the actual length of the tables - with pipelining requires 7 cycles, but these cycles are 1/5th of the time compared to the without pipelining cycles
- therefore if we counted the with pipelining cycles as 1 block of time:
	- without pipelining -> ==completion in 25 time blocks==
	- with pipelining -> ==completion in 7 time blocks==

### drawbacks of pipelining
- since you increase the clock frequency to benefit from pipelining, this also means you increase the power draw of the processor, increasing energy consumption
- by introducing pipelining (as well as more stages), you introduce extra hardware, a more complex logic design, a potential difficulty in splitting up the processing cycle into uniform blocks, and have to keep in mind the register loading time limits the cycle period
- since pipelining introduces a longer datapath, theres a higher chance of [[control hazards]] occuring, and the penalties are worse when these hazards do occur

### deeper pipelining
- as mentioned before, in the examples we break the processor cycles down into 5 pipeline stages, but these cycles could potentially be broken down into more stages if wanted/needed
- these longer pipelines are also known as ==deeper pipeliens==
- deeper pipelines mean that each pipeline stage does less, and each step takes less time so clock frequency increases
- however, there is a much greater penalty for hazards with longer pipelines, and its also more likely that instructions may have conflicts down the pipeline
- to add onto all of this, there is obviously more complex logic and hardware by having more stages with buffers - a trade-off between many different aspects (including frequency, power, area) is made here


![](https://i.imgur.com/ATE0oyQ.png)
