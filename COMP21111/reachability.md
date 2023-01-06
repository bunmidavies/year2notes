[[COMP21111]]

reachability is useful in order to tell if any ==bad states== are possible to encounter within a system - [[safety requirements]]

given some number $n$, it is possible to find a ==symbolic representation== of the set of states which are reachable from an initial state within $n$ steps

let $C(\bar{x})$ represent some set of states $S$. We define:
- $FR(\bar{x}) = \exists\bar{x_1}(C(\bar{x}_1)\land T(\bar{x_1},\bar{x}))$
where $FR$ is the ==set of reachable states== from $S$ in ==1 step==

$R_n$ defines reachability in $n$ states:

$R_0(\bar{x}) = I(\bar{x})$ ($I$ means ==argument is an initial state==)

$R_n(\bar{x}) = \exists\bar{x}_{n-1}(R_{n-1}(\bar{x}_{n-1})\land T(\bar{x}_{n-1},\bar{x}))$



there are three main algorithms used to determine reachability, which are normally implemented with ==propositional SAT solvers==, or as an extension of the ==DPLL== algorithm - [[DPLL - QBFs and Propositional]]

[[bounded model checking aka onesided forward reachability]]

[[complete forward reachability]]

[[backward reachability]]