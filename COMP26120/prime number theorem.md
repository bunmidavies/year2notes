[[COMP26120]]

### definition
- let $\pi(n)$ be the ==prime distribution function==, specifying the number of primes that are less than or equal to $n$
- e.g. $\pi(10) = 4$, since there are 4 primes less than or equal to 10
- the ==prime number theorem== states:
$$\lim_{n\rightarrow\infty}\frac{\pi (n)}{n/\ln n} = 1$$
- therefore, $n/\ln n$ gives an ==approximation== for $\pi (n)$

### guessing random numbers
- if a large number $n$ is picked, then there is a $\frac{\pi(n)}{n}$ chance that it is a prime. This can be expanded to be written as a $\frac{1}{\ln n}$ chance it is prime.
- if we want a prime of the same size as $n$, then if we pick $\ln n$ random numbers of that size we will most likely find a prime. Example: finding a 1024 bit prime will take $\ln 2^{1024} \approx 710$ attempts
- since this isn't a huge number (thus quite easy to find), the task of finding prime numbers becoming easy requires checking whether a random number is prime to be easy as well