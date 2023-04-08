[[COMP26020]]

### ~ safety / liveness
- safety properties and liveness properties are the 2 main properties used when specifying how a concurrent system ==should behave==

- ==safety property== - a property which describes what should ==always== be true, or something that should ==never== happen e.g. never have deadlocks, never have race conditions
- ==liveness property== - a property which ==should== happen in a concurrent system, at some point in the future e.g. termination, the completion of a task

- being able to describe these properties in a formal way can allow for ==automatic bug discovery== in concurrent systems, where bugs are typically notoriously difficult to uncover