[[COMP26120]]

### ~ definition
- modular arithmetic is regular arithmetic over integers, except all results have the modulo operation applied to them by the same integer $n$

### ~ multiplicative inverses
- the multiplicative inverse of a given number $a$ ==with respect to a modulus== $n$, is the number which you can multiply $a$ by, then mod $n$ and get 1:
$$a \times \textrm{ [multiplicative inverse] mod } n = 1$$
- for example, if $n = 9$, the multiplicative inverse of 5 is 2: $5 \times 2 \textrm{ mod } 9 = 1$
- ==multiplicative inverses always exist for prime numbers== (other than 0) - but in general multiplicative inverses wont always exist

### ~ $\mathbb{Z}_n$ and $\mathbb{Z}_n^*$
- $\mathbb{Z}_n$ is just {0,1,...$n-1$}, the set of (positive) integers less than $n$
- meanwhile, $\mathbb{Z}_n^*$ represents the set of integers less than $n$ which have ==multiplicative inverses== (mod $n$)

### ~ generators i.e. primitive roots
- a primitive root is an integer that generates all possible remainders, when raised to different powers
- essentially, $g$ is a primitive root modulo $n$ if by raising $g$ to different powers modulo $n$, you are able to obtain all possible remainders from $0$ to $n-1$
- if a number is prime, a ==primitive root must exist==
- ( you are not expected to be able to find primitive roots )
- using primitive roots, a public key for [[el gamal encryption]] can be selected