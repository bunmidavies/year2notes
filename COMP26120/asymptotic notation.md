[[COMP26120]]

taken from chapter 3.2 of [[intro to algorithms 4th edition.pdf]]

### $\Theta$-notation
Theta notation is used for ==asymptotically tight bounds==. $\Theta$ notation is applicable when a function's O bound is ==equal== to its $\Omega$ bound:

There exists positive constants $c_1, c_2$ and $n_0$ such that:
$$0 \leq c_1g(n) \leq f(n) \leq c_2g(n)$$
for all $n \geq n_0$

![](https://i.imgur.com/49Tcekz.png)


and in terms of big-O and omega: 
($f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$)
==this term can be used to identify tight bounds from upper and lower bounds, but the definition above is the real definition==

Essentially, you're able to describe a function as the tight bound of some other function if you're able to find 2 constants such that $c_1g(n) \leq f(n) \leq c_2g(n)$

This theorem is normally used to prove asymptotically tight bounds once you already have the asymptotic ==upper== and ==lower== bounds. It is the ==most precise==, thus the ==most preferred==

### running times - best case/worst case/overall
- when discussing running times its important to not omit what 'case' a running time is being declared for if you are using theta notation
- for instance the best case running time for the insertion sort may be $\Theta(n)$, and the worst case running time is $\Theta(n^2)$ - ut you cannot say the ==running time== is $\Theta(n^2)$ - this is a blanket statement which now assumes $\Omega(n^2)$ and $O(n^2)$ for the algorithm in any case, but this is not true
- insertion sorts best case times are $\Omega(n)$ and $O(n)$, therefore we can say $\Theta(n)$
- However you can correctly say insertion sort is generally $O(n^2)$, as $O(n)$ in the best case for insertion sort still fits under $O(n^2)$. You can also say that $\Omega(n)$ is the running time of insertion sort, because of the best case $\Omega$

- because $O$ is an upper bound, it can actually mean it's not really possible to determine whether one algorithm performs better than another
- for instance, saying:
  *"an $O(nlogn)$ algorithm runs faster than an $O(n^2)$ algorithm"*
  could be right or wrong. O-notation just denotes the asymptotic upper bound, so in reality the $O(n^2)$ algorithm could still run in $\Theta(n)$
- the aim with asymptotic notation is to provide the most precise and useful upper/lower bound


### inequations / inequalities
- $=$ is typically used rather than the $\in$ sign for asymptotic notation, when the asymptotic notation stands alone. For example
$$2n^2 + 100n + 200 = O(n^2)$$
$$\textrm{is the same as}$$
$$2n^2 + 100n + 200 \in O(n^2)$$

- however, formulas like the following can also appear:
$$2n^2 + 3n + 1 = 2n^2 + \Theta(n)$$
- we interpret $\Theta(n)$ as some anonymous function that hasn't been named:
  $$2n^2 + 3n + 1 = 2n^2 + f(n)$$
$$f(n)\in \Theta(n)$$
- in this example we can let $3n + 1 = f(n)$, because $3n + 1 \in \Theta(n)$
- ==The number of anonymous functions in an expression is equal to the number of times the asymptotic notation appears==
![](https://i.imgur.com/61fuvGz.png)


### $o$-notation (little o) and $\omega$-notation (little omega)

- little o is used to describe big-$O$ notation which ==isn't tight== - for instance:
$$2n^2 = O(n^2)$$
- is a tight upper bound, but:
$$2n = O(n^2)$$
- is ==not== a tight upper bound
- therefore the definition of $o(g(n))$ is:
![](https://i.imgur.com/R4RQ2SO.png)

- the difference between little o and big O is that $f(n) \lt cg(n)$  holds for ==any constant c > 0== when talking about little o, while $f(n) \leq cg(n)$ holds for ==some constants c > 0== when talking about big O

- this means that as n gets large, $f(n)$ becomes insignificant relative to $g(n)$
![](https://i.imgur.com/eNZfvC7.png)



- $\omega$-notation is similar to o-notation, but for $\Omega$. It's like a *lower than low* bound for a function, and by definition
$$f(n) \in \omega(g(n))\textrm{ if and only if } g(n) \in o(f(n))$$


### semi-useful comparison
![](https://i.imgur.com/m6OcYjZ.png)

![](https://i.imgur.com/CeD38kH.png)


