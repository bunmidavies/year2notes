[[COMP25212]]

- a superscalar processor is a processor which is able to execute ==more than 1== instruction in parallel
- an ==n-way== superscalar processor is able to execute n instructions in parallel
- in order to transform a regular i.e. ==scalar== processor into a ==superscalar== processor, the following hardware additions are required:
	- adding extra execution lanes (ALUs)
	- increasing the number of ports to memory and the processors register bank (such that there are enough in order to process instructions in parallel)
- the operation cycles for a superscalar processor can be shown as such
![ | 550](https://i.imgur.com/uxmI5c6.png)
- the main drawbacks of superscalar processors are that they're obviously much more complex in hardware, in comparison to a scalar process
- furthermore, whether an application can actually benefit from superscalar extension varies - if an application doesn't exhibit any parallelism, then there is no benefit of it being executed with a superscalar processor