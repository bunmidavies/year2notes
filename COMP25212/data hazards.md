[[COMP25212]]

- the following example code demonstrates a ==data dependency== between 2 instructions:
```Pug
ADD R1, R2, R3
MUL R0, R1, R1
```
- the ADD produces a value in R1, and the MUL uses R1 as input, so MUL basically has to wait until the ADD result is written back to R1 (otherwise the 'old' value of R1 will be retrieved by the MUL instruction)
- there are multiple ways to deal with these data dependencies, as shown below

### pipeline stalling
- dependencies can be detected in hardware, and instructions can be ==held== in the decode stage until the data is ready. This is also known as ==pipeline stalling==. Cycles are wasted because of this, but it at least ensures that instructions aren't wrongly executed using old reg values
![](https://i.imgur.com/57x4ZPQ.png)

### reordering instructions
- rather than detecting dependencies in hardware, dependencies would be detected by the compiler, and if the compiler finds something useful to do while instructions writeback their results, they can be reordered
- if an appropriate reordering can't be found, NOP instructions are just inserted, which at that point basically makes it no different to pipeline stalling
![](https://i.imgur.com/7nzliGP.png)
- further info exists within [[reordering instructions]]

### forwarding (adding extra hardware)
- extra data paths can be added for specific cases - e.g. the output of the execution (EX) stage feeds back into the input of the same stage
- the main drawback to this is that the logic now becomes more complex
- in the example above, forwarding is shown for the execution stage, but forwarding could also be applied after the memory (MEM) stage, if for instance the output from an LDR instruction is needed in the instruction after
- note that other pipelines may still need to stall until the data is available, but the idea is that ==less stalling== will be required:
![](https://i.imgur.com/wUVrfu4.png)
