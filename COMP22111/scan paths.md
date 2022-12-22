[[COMP22111]]

scan paths improve the testability of a circuit by providing **observability** and **controllability** (as mentioned in [[test coverage]])

certain "blocks" within a circuit may contain latches, which are made of flip flops. These flip flops can be replaced with scan flip flops, where scan flip flops will retain data in a "block" after the clock stops

now, by retaining the value in a scan flip flop after the clock has stopped, the value within latches are accessible outside of the "block"

the main problem with scan paths is that big circuits may have many reachable states, so blocks can end up holding an infeasible number of latches to scan (?)

the workaround for scaling problems is to subdivide blocks, and test the blocks in parallel so that all can still be tested in a feasible amount of time