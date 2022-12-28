[[COMP26120]]

karatsuba multiplication improves the typical $O(n^2)$ time complexity for integer multiplication, where $n$ is the number of bits used to represent the integers

==typical method==

the numbers are split into ==two halves== - higher bits and lower bits
therefore, given integers $x$ and $y$, where $x_h$ and $y_h$ are the higher halves, and $x_l$/$y_l$ are the lower halves:

$x = x_h * 2^{n/2} + x_l$
$y = y_h * 2^{n/2} + y_l$

since the higher halves need to be shifted

therefore, $xy$ must equal:
$$x_h y_h 2^n + x_h y_l 2^{n/2} + x_l y_h 2^{n/2} + x_l y_l$$
these will be referred to with ==labels== $z_1$ to $z_4$

referring to these with their time complexities in terms of $n$, we see that
$$T(n) = 4T(n/2) + cn$$
by applying the [[master method]] (1st half of COMP26120), we receive a time complexity of $O(n^{log_24})$ = $O(n^2)$

==karatsubas method==

note that $(x_l - x_h)(y_h - y_l) = x_ly_h - x_hy_h - x_ly_l + x_hy_h$
so we can write $x_hy_l + x_ly_h = (x_l - x_h)(y_h-y_l) + x_hy_h + x_ly_l$

we wrote that $xy$ = $x_h y_h 2^n + x_h y_l 2^{n/2} + x_l y_h 2^{n/2} + x_l y_l$, which is also
$2^{n/2}(x_hy_l + x_ly_h) +  x_hy_h2^n + x_ly_l$

we'll make $(x_l - x_h)(y_h - y_l)$ = $z_5$

so we can simplify this to $z_12^n + (z_5 + z_1 + z_4)2^{n/2} + z_4$

this new time complexity can be used with the [[master method]], giving us a time complexity of $O(nlog_23)$