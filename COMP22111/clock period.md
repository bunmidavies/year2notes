[[COMP22111]]

At the gate level of a circuit, the clock period is roughly set by the number of gates a signal travels through between 2 registers. An approximate max would aim for 30 gates, but high performance clocking pipelines should aim for much less

the **minimum allowed clock period** is a sum of:
- propagation delay of the source register
- propagation delay of the logic
- set up time of the target register
- additional time margin for uncertainty (jitter, skew)

propagation / set up time are explained within [[flip flop delay]]

**clock skew** is the difference in arrival times of a clock signal to different parts of a circuit. In order to reduce skew, [[clock distribution]] strategies exist

[[clock domain + metastability]]
