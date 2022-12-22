[[COMP22111]]
following on from [[types of testing]]

CAD tools typically can provide all of these types of testing

Design-level
- done at RTL level - all source code is executed, all alternative routes are taken, but not **all** data patterns are tried as input where applicable

Circuit-level
- done once the circuit has been synthesized

Production-level
- at this point the design is believed to work, but could still fail at some point

when wanting to test a system, in order to make the testing process easier, two factors should be kept in mind:
- **controllability** - the ability to inject inputs into a system within a circuit shouldn't be extremely difficult
- **observability** - the ability to view the outputs from the Device Under Test clearly 
