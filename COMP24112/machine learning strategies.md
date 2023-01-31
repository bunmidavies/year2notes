[[COMP24112]]

the typical ML strategy is the ==Data + Model== strategy:

Data: X $\rightarrow$ Model: $f(\theta,X)$

Data can be described as a collection of ==experience==, $E$

the function $f$, is controlled by its parameters $\theta$, and provides solutions to a task $T$

the actual task within machine learning is to find the best parameters, resulting in the best function, i.e. the ==best performance P of task T==

the ==Objective Function==, $O(\theta)$ computes the performance of task T - therefore, the ==optimisation== ([[ML optimisation]]) of this objective function is whats known as the learning/training process in machine learning