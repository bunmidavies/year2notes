[[COMP26120]]

[[pertrubation method]]

### Sums

Given a sequence of $a_1,a_2,...,a_n$ of numbers, where $n$ is a ==non-negative integer== we can write the finite sum $a_1 + a_2 + ... + a_n$ as:
$$\sum_{k=1}^{n}a_k$$
if $n = 0$, the value of this summation is 0

Given an ==infinite== sequence of $a_1,a_2,...,a_n$, we now write the summation as:
$$\lim_{x \to \infty}\sum_{k=1}^{n} a+_k$$
If a limit doesn't exist the series ==diverges==
If a limit does exist the series ==converges==

Sums can also be manipulated ==algebraically==:
$$\sum_{k\in K} ca_k = c\sum_{k\in K} a_k$$
$$\sum_{k\in K} (a_k + b_k) = \sum_{k\in K} a_k + \sum_{k\in K} b_k$$
$$\sum_{k\in K} a_k = \sum_{p(k)\in K} a_{P(k)}$$
*(this rule is known as ==permutation== - the sum value is unchanged by permuting the order of the summands)*

### Arithmetic Series

The summation:
$$\sum_{k=1}^n = 1 + 2 + ... + n$$
is ==arithmetic== and has the value
$$\frac{1}{2}n(N+1) = \Theta(n^2)$$
Where $\Theta$ is the ==strict bound== of time complexity ([[asymptotic notation]])

### Geometric Series

Used when the summation is
$$\sum_{k=0}^{n} x^k = 1 + x + x^2 + ... + x^n$$
and $x\neq 1$. This summation is equal to:
$$\sum_{k=0}^{n} x^k = \frac{x^{n+1} - 1}{x - 1}$$