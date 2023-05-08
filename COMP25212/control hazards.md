[[COMP25212]]

### definition
- control hazards can occur within [[pipelining]] - the idea is that instructions are fetched sequentially (i.e. one after the other), and when a branch is fetched (following the idea of a processor cycle being broken down into stages - [[cycles of operation + stages]]) we will only know that it is a branch when we decode it in the cycle's 2nd stage
- by the time it is known that this instruction is a branch, the instruction directly after the branch instruction has been fetched by the previous pipeline stage
- this is a problem since ==what if this is no longer the next instruction?== its basically implied since there'd be no reason to have a branch which branches to the direct next instruction
![|450](https://i.imgur.com/djwfemZ.png)
- the solution to this is to ==mark instruction 5 as unwanted== - but by this point, IF on instruction 5 has already been done (i.e. the instruction has already been fetched), so this means a cycle has been wasted - this is also called a ==bubble==
- this is just the case for an ==unconditional== branch - with a ==conditional== branch, we wouldn't know whether we're branching or not for sure until the execute (EX) stage, so even later than the decode (ID) stage. This could then result in 2 bubbles
- however, this can be avoided by reading registers during the decode stage

- in short - 'bubbles' due to branching are called ==control hazards== - they occur because it takes more than one pipeline stage to detect if a branch is actually happening
- if there are more stages in a processor before the decode/execute stage, then there will be more bubbles
- we can apply ideas like [[branch prediction]] in order to essentially preemptively tell if a branch is happening, and try prepare for it in order to prevent control hazards