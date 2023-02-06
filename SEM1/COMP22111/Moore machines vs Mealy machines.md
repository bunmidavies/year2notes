[[COMP22111]]

### Moore Machine vs Mealy Machine
- A ==moore machine== is a sequential system which determines its outputs ==**only using the current state**== - the input changing here doesn't affect the outputs if the state remains the same

- The difference between this and the ==**Mealy Machine**== is that the inputs are connected to the output logic of the system, such that the outputs are determined using ==**both the current state and current inputs**==

- The advantage of the mealy machines is that you may be able to use less states within the system, but issues like timing can arise (due to the ==asynchronous== behaviour)