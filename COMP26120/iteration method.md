[[COMP26120]]

there are 3 main steps in the iteration method:
1. expand recurrence
2. use algebra to express recurrence as a summation
3. evaluate the summation (using techniques to analyze [[complexity of recursive programs]])

### Example 1
we want to ==solve== i.e. find the complexity of the following recurrence:
$s(n)$
![](https://i.imgur.com/C9qtLIF.png)


we see that $s(n) = c + s(n-1)$ (given $n > 0$), so we know
$s(n) = c + c + s(n-2)$
$s(n) = c + c + c + s(n-3)$
$= 3c + s(n-3)$
this can be ==generalized== as:
$= kc + s(n-k)$, where $n > k$

so when $k = n$:
$s(n) = cn + s(0) = cn$
$s(n) = cn$ - where $c$ is some constant

this means $s(n) = O(n)$

### Example 2
we want the complexity of the following recurrence:
![](https://i.imgur.com/3HxR3OT.png)


we try to generalize $s(n)$ again where $n > k$
$s(n) = n + s(n-1)$
$= n + n-1 + s(n-2)$
$= n + n-1 + n-2 + s(n-3)$
$=   ...$
$= n + n - 1 + n - 2 + ... + n - (k-1) + s(n-k)$ where $k$ is some constant

so we try to solve the equation when $n = k$

$n + n-1 + n - 2 + ... + n - (k - 1) + s(0)$
$= n + n-1 + n-2 + ... + n - (k - 1)$

using the knowledge from [[complexity of recursive programs]], we can identify this as an ==arithmetic sum==:
$$n + n-1 + n-2 + ... + n - (k - 1) = (\sum_{i=n-k+1}^{n} i) + s(n-k)$$

so now we solve the recurrence for when $n = k$
$$\sum_{i=n-k+1}^{n} i + s(n-k) = \sum_{i=1}^{n} i + s(0)$$
$$\sum_{i=1}^{n} i + 0 = n \cdot \frac{n+1}{2}$$
finally, $n\frac{n+1}{2} = O(n^2)$
### Example 3
we want to find the complexity of the following recurrence:
![](https://i.imgur.com/kd6YA2d.png)


as done before, we can ==generalize== the case where $n > 1$
note that we are able to write $2T(n/2) + c$ as $2(2T(n/2/2)+c) + c$ because:

if $T(n) = 2T(n/2) + c$ when $n>1$, then to get $T(n/2)$ we should use the original equation, with $n/2$ in place of $n$
![](https://i.imgur.com/DJfDQOG.png)


So for $n > 2^k$ we have $T(n) = 2^kT(n/2^k) + (2^k - 1)c$

we can then sub in $k = logn$ to solve the recurrence equation:

$$T(n) = 2^{logn}T(n/2^{logn}) + (2^{logn} - 1)c$$
$$= nT(n/n) + (n-1)c$$
$$=nT(1) + (n-1)c$$
$$=nc + (n-1)c = (2n - 1)c$$
therefore, we can say $T(n) = O(n)$
### Example 4
we want to know the recurrence equation and time complexity of the following:
![](https://i.imgur.com/F1aCrwO.png)


(page for finding complexity goes here)

we now have the recurrence equation, so we want to know the complexity:
![](https://i.imgur.com/qis5GuY.png)


we generalize as usual - while also factorising
![](https://i.imgur.com/ZmNhqQl.png)


so we now have $T(n) = a^kT(n/b^k) + cn(a^{k-1}/b^{k-1} + ... + a^2/b^2 + a/b + 1)$

if we set $k = log_bn$ then we find
$T(n) = a^kT(n/n) + ...$
we can treat $a^k \cdot 1$ as $a^kc$ as theyre both ==constants==
$T(n) = cn(a^k/n + a^{k-1}/b^{k-1} + ... + a^2/b^2 + a/b + 1)$
and because $k = log_bn$, we know that $n = b^k$
$T(n) = cn(a^k/b^k + a^{k-1}/b^{k-1} + ... + a^2/b^2 + a/b + 1)$

as we don't know what $a$ and $b$ are, we have to consider ==all possible cases==, and determine the complexity of each

1. a = b
when a = b, it is clear to see $T(n) = cn(1 + 1 + ... + 1)$ no matter the values of a and b
so we are left with $cn(k +1)$, which becomes:
$cn(log_bn + 1)$
$cnlog_bn + cn$
we take the highest bound here, so we are left with
$\Theta(nlog_bn)$

2. a < b
as we noted in [[complexity of recursive programs]], we can define a ==geometric== series:
![](https://i.imgur.com/EARC8zE.png)

given $T(n) = cn(a^k/b^k + a^{k-1}/b^{k-1} + ... + a^2/b^2 + a/b + 1)$, we can write this as:
$$\frac{(a/b)^{k+1} - 1}{(a/b) - 1}$$ we can then multiply both sides by -1
$$\frac{1 - (a/b)^{k+1}}{1 - (a/b)}$$
==because a < b==, we can say that $(a/b) < 1$ at all times, thus
$$\frac{1 - (a/b)^{k+1}}{1 - (a/b)} < \frac{1}{1 - (a/b)}$$
therefore
$$T(n) = cn \cdot \frac{1}{1-(a/b)}$$
$$T(n) = cn \cdot \Theta(1)$$
$$T(n) = \Theta(n)$$

3. a > b
we can obtain the same summation as before:
$$\frac{(a/b)^{k+1} - 1}{(a/b) - 1}$$
but now as $a >b$ , for whatever reason (?) we can represent this as:
$$\Theta((a/b)^k)$$
Thus we're left with:
$$T(n) = cn \cdot \Theta(a^k/b^k)$$
as we previously said $k = log_bn$, we can now sub this in
$$T(n) = \Theta(cn \cdot n^{log_ba}/n)$$
this uses the logarithmic law that $a^{log_bn} = n^{logba}$
$$T(n) = \Theta(n^{log_ba})$$

==We now have our final complexities==
![](https://i.imgur.com/Wy6qKnk.png)
