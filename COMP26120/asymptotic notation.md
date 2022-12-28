[[COMP26120]]


### $\Theta$-notation
Theta notation is used for ==asymptotically tight bounds==. $\Theta$ notation is applicable when a function's O bound is ==equal== to its $\Omega$ bound:

- $f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$

This theorem is normally used to prove asymptotically tight bounds once you already have the asymptotic ==upper== and ==lower== bounds. It is the ==most precise==, thus the ==most preferred==

### running times
when discussing running times its important to not omit what 'case' a running time is being declared for, because for instance the best case running time for the insertion sort may be $\Theta(n)$, and the worst case running time is $\Theta(n^2)$
but you cannot say the ==overall running time== is $\Theta(n^2)$ - this statement then makes the assumption the best case is $n^2$, when it isnt

however with algorithms like merge sort, where it runs in $\Theta(nlogn)$, in all cases, it is okay to say its running time is $\Theta(nlogn)$ without specifying case