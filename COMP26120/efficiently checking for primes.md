[[COMP26120]]

### naive attempt: trial division
- a simple way to check if a number is prime is just by checking if it can be divided by any number less than it:
```
y := x-1
while y > 0:
	if y divides x then break
	else y -= 1
if y == 1 return True
else return False
```
- a small optimisation can be making y start at $\sqrt{x}$
- complexity: if x is made of n bits, we consider this as $O(2^{\frac{n}{2}})$

### using fermat's little theorem
- Fermat's little theorem stated if $p$ is prime and $x$ is an integer where $x \text{ mod } p \neq 0$ then $x^{p-1}=1(\text{ mod }p)$
- fast modular exponentiation, which has a linear complexity, can then be used by picking an $x$ at random - if $x^{p-1}\text{ mod }p\neq 1$
- if $x^{p-1}\text{ mod }p = 1$, we either have:
	- a carmichael number (not prime)
	- an actual prime number
- we extend this idea to a full solution below

### randomized primality testing
- we firstly assume we have a ==witness function== $\text{witness}(x,n)$, which works as follows:
	- if $n$ is prime, then witness(x,n) returns `false`
	- if $n$ is composite, then witness(x,n) returns `false` with probability $q<1$, otherwise `true`
- the randomised primality testing algorithm is as follows
![](https://i.imgur.com/p1l7M8Y.png)
- the algorithm ==is supposed to return false== (meaning $n$ is prime) with an error probability of $2^{-k}$
- $k$ is called the *confidence parameter*, i.e. how sure we want to be that $n$ is prime
- false is returned with probability $q^t$, assuming each $x$ is picked independently
![](https://i.imgur.com/OYwVIEq.png)
##### example calculation
![](https://i.imgur.com/nRYaiNp.png)

### example witness  function: Rabin-Miller
- facts required:
	- if $p$ is prime, then if $x^2\mod p =1$ then either $x=1(\mod p)$ or $x=-1(\mod p)$
	- if $n$ is odd then $n-1 = 2^tm$ for some odd number $m$
- develop a pattern and figure out which pattern the number $n$ belongs to
![](https://i.imgur.com/UnVadco.png)
##### example implementation - looking for the 'probably prime' pattern
![](https://i.imgur.com/XqiYxCL.png)
##### example implementation - looking for the 'composite' pattern
![](https://i.imgur.com/4ri1wkT.png)
- if $n$ is composite, there are at most $\frac{n-1}{4}$ values for $x$, such that witness(x,n) returns false
- $q = \frac{1}{4}$ (the error probability), therefore the $t$ calculated in the randomised primality algorithm above would be $\frac{k}{2}$ if this witness function is used
- ==complexity== $\frac{k}{2}$ fast modular exponentiation operations ($\log n$), therefore $O(k\log n)$
- the error probability of Rabin-Miller is also $2^{-k}$