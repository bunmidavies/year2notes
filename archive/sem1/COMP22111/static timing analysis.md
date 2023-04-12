[[COMP22111]]

> [!in general]
> STA identifies anything that is significantly bad, at a low cost

STA is known as "static" because it just finds the longest path between two flip flops, as this will be the "upper bound" for the delay. It does not simulate the circuit with any inputs

**advantages**
- low computational complexity
- faster than simulations
- conservative in providing an upper bound

**disadvantages**
- as it always finds the longest path, it may provide an upper bound which isn't really necessary, as the path in question may never be taken