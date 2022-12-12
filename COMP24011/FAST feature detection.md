[[COMP24011]] / #comp24011
[[feature detection]]

## feature detection example: FAST
1. select a pixel to test $(p)$. selected pixel has intensity $I_p$
2. select an appropriate threshold value $t$
3. consider the circle of 16px around $p$
4. if there are 12 contiguous pixels which are brighter than $I_p + t$, or darker than $I_p - t$, $p$ is a *corner feature*