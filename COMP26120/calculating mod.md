[[COMP26120]]

mainly useful for calculators which do not have the `mod` function

### ~ steps
- to calculate $x \textrm{ mod } y$
1. calculate $x \div y$
2. take away any number to the left of the decimal point, so you're left with whatever < 1
3. multiply the result by $y$

### ~ example
- 463 mod 7, i.e. $x = 463, y = 7$
1. $463 \div 7 = 66.142857142857143$
2. remove everything to the left of decimal point $\rightarrow 0.142857142857143$
3. $0.142857142857143 \times 7 = 1$
- therefore 463 mod 7 = 1
