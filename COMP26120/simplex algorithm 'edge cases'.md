[[COMP26120]]

### ~ the origin is not a solution
- take the following example
![ | 250](https://i.imgur.com/yZj3D8R.png)
- unlike in problems explored in [[simplex algorithm]], if we set $x_1 = 0, x_2 = 0$, we do ==not== have a solution, since the 2nd constraint is not met
- furthermore if we convert this to ==slack form==, $s_2$ would have to be equal to 12, which now violates the ==non-negativity constraint==, so this cant be a solution either

- the workaround for this is ==artificial variables== - these variables are introduced so that $x_1 = 0$ and $x_2 = 0$ are solutions
- then the goal becomes to make these artifical variables equal to 0 in the optimal solution
- so we now add in artificial variable $a_1$ to the problem
![ | 250](https://i.imgur.com/8bqBdiU.png)
- $M_1$ stands for massive, meaning ==if a1 is anything other than 0 there is a huge penalty== - this can now be expressed as an augmented matrix
![ | 300](https://i.imgur.com/vGifoCu.png)
- we can now pivot, swapping $a_1$ with $s_2$, to get an initial feasible solution involving $M_1$
![](https://i.imgur.com/ipR4gmh.png)
- the resulting matrix can then just be solved as normal

### ~ solution space is unbounded
- one typical way to notice if you have an unbounded problem is where you have a column with ==only negative values== in an augmented matrix
- as well as this, an unbounded problem might be a mistake 

### ~ zero slack
- consider the following example:
![ | 250](https://i.imgur.com/Pu3qKr3.png)

