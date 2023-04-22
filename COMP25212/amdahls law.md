[[COMP25212]]

### ~ definition
- Amdahl's law estimates a parallel systems maximum performance, based on the available parallelism in an application (originally intended to discourage parallel architectures)

### ~ formula
$$\textrm{SPEED UP =} \frac{S + P}{S + (P/N)}$$
- $S$ = fraction of code which is serial
- $P$ = fraction of code which can be parallel
- $N$ = number of processors

![](https://i.imgur.com/mcyByls.png)
