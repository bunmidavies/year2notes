## exercise 1
- invariant - with each recursive call, $f(n) = 3^n$
- initialisation - when $n$ = 0, $exp(n)$ should equal $3^0$, and this is correct according to the function
- step case:
*n is even*
when $n$ is even, return $exp(n/2) \cdot exp(n/2)$, and using the inductive hypothesis, $exp(n/2) = 3^{n/2}$, so $3^{n/2} \cdot 3^{n/2}$ = $3^n$, which matches our invariant
*n is odd*
when $n$ is odd, return $3 \cdot exp((n-1)/2) \cdot exp((n-1)/2)$
using induction hypothesis, $3 \cdot 3^{(n-1)/2} \cdot 3^{(n-1)/2}$
$3 \cdot 3^{(n-1)}$
$3^n$, which matches up with our invariant

therefore proved

## exercise 2

$T(n) = T(\lceil{\frac{n}{2}}\rceil) + 1$  is $O(log_2{n})$

We are proving $T(n) \leq log_2{n}$
proof by induction:

base case: n = 1
$log_2{1} = 0$
$T(1) = 1$ (as mentioned in the question)
$0 \leq 1$, therefore base case holds

step case:
n is even:
$T(n) = T(\frac{2n}{2}) + 1$
$T(n) = T{n} + 1$
$T(n) \leq log_2{n} + 1$
$T(n) \leq log_2{n}$
Therefore proved

n is odd:
$T(n) = T(\frac{2n+1}{2}) + 1$
$T(n) = log_2{\frac{2n+1}{2}} + 1$
$T(n) = (log_2{(2n+1)} - log_2{2}) + 1$
$T(n) = (log_2{(2n+1)} - 1) + 1$
$T(n) = log_2{(2n+1)}$
$T(n) = log_2{(2(n+\frac{1}{2}))}$
$T(n) = log_2{2} + log_2{(n+\frac{1}{2})}$
$T(n) = 1 + log_2{(n+\frac{1}{2})}$  
$T(n) = log_2{(n)}$

## exercise 3

$T(n) = 2T(n^{\frac{1}{4}}) + 1$, if $n > 1$
$T(n) = 1$ if $n = 1$

$m = logn$
$n = 2^m$
$T(2^m) = 2T(2^{m/4}) + 1$
$S(m) = 2S(m/4) + 1$

Solving with master method
$a = 2, b = 4, f(m) = 1$
$log_b{a} = log_4{2} = \frac{1}{2}$
$f(n) = O(m^{log_b{a} - \epsilon})$
$f(m) = O(m^0) = O(1)$, where $\epsilon = \frac{1}{2}$
Therefore $S(m) = \Theta(m^{1/2})$
$T(n) = T(2^m) = S(m)$
$O(m^{1/2}) = O((logn)^{1/2})$

## ex 4





## ex 5

A) 
$T(n) = 2T(n/2) + n^4$
$a = 2, b = 2, f(n) = n^4$
$n^{log_b{a}} = n^{log_2{2}} = n^1 = n$
$f(n) = n^4$
$f(n) = \Omega(n^{log_2{(2+\epsilon)}})$ *(case 3)*
$f(n) = \Omega(n^4)$
$\epsilon = 14$
$af(n/b) \leq cf(n)$ where $c < 1$
$2((n/2)^4) \leq cn^4$
$2((n^4/16)) \leq cn^4$
$n^4/8 \leq cn^4$
$c = 1/2, n^4/8 \leq n^4/2$ holds
therefore $T(n) = \Theta(n^4)$

B)
$T(n) = T(10n/7) + n$
$a = 1, b = 10/7$
$f(n) = n$
$n^{log_b{a}} = n^{log_{10/7}{1}}$
$log_b{a} = 0$
$f(n) = \Theta(n)$
$f(n) = \Omega(n^{0+1})$ 

therefore $T(n) = n$

C
$T(n) = 2T(n/4) + \sqrt{n}$
$a = 2, b = 4, f(n) = \sqrt{n}$
$log_b{a} = log_4{2}$
$log_b{a} = \frac{1}{2}$
$f(n) = \Theta(n^{\frac{1}{2}})$
therefore $T(n) = \Theta(\sqrt{n}logn)$


Therefore, in terms of runtime:
1. C
2. B
3. A


