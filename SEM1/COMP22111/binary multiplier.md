[[COMP22111]]

a binary multiplier is a circuit **built using binary adders**, used to multiply two binary numbers. Most techniques involve computing a set of partial products, then adding them together

The general process involes multiplying one input by each digit of the other input - e.g. 54 x 360 = 50 x 3 + 4 x 3 + 50 x 60 + 4 x 60. The partial products are then shifted accordingly, and added together

multipliers allow for parallelism, because several partial products can be evaluated simultaneously. [[FPGA]]s may typically provide small preoptimised multipliers

different adders exist for adding partial products e.g. Carry save adder, or Tree carry ripple adder. The tree carry ripple adder will have more gates on the critical path, but is actually quicker than the carry save adder according to the lecture