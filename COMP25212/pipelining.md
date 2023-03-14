[[COMP25212]]

- as covered within the [[fetch-execute]] cycle, and showing the individual stages which exist within this ([[cycles of operation + stages]]), we've shown that certain parts of a processor can be waiting within a cycle, not being utilised
- pipelining aims to utilise these 'stages' which typically wouldnt be used, and does this through inserting ==buffers in between stages==
![](https://i.imgur.com/LVknNqn.png)
- when previously the output of each stage was just sent to the next stage, the output of each stage can now be stored in a buffer, meaning the stage can begin to start working on something else
- this is similar to something like in a car production line, and results in 5x faster execution by increasing the ==clock frequency== by 5x
- ==note that only one instruction is still executed per cycle==

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

### effects of pipelining + real world pipelines
![](https://i.imgur.com/SSRJ4Rj.png)

![](https://i.imgur.com/ATE0oyQ.png)
