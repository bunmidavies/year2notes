[[COMP25212]]

- branch prediction relies on the idea that ==in most programs, branches are executed many times==
- if we ==take note== of the address of the branch + the address being branched to (using a small cache - a ==branch target buffer==) we can potentially reduce the number of wasted cycles and fetch the 'target branch' address straight away
- the main penalty of getting a branch prediction wrong are ==bubbles==, i.e. [[control hazards]]
- branch prediction techniques other than BTB exist, but are more complex. There are typically 2 things that branch prediction mainly depends on:
	1. history (previous branches)
	2. context (how was this branch reached)

### Branch Target Buffer (BTB)
- as a branch is fetched, the BTB can be checked - if there is a valid entry in the BTB, the next instruction can be fetched from the target address stored by the BTB, rather than fetching the PC incremented instruction
![ | 250](https://i.imgur.com/xhO9W4a.png)

- there are 2 main cases which occur within the BTB, given the type of branch:
	- ==unconditional branch== - the BTB will always be storing the correct address to be fetched
	- ==conditional branch== - whether the BTB stores the correct address depends on the probability of reaching the target
- ==BTB is simple to understand, but expensive to implement== - only the most recent branch is ever used for prediction

### benefits of branch prediction
![](https://i.imgur.com/J8KK74t.png)
