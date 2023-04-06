[[COMP26120]]

### ~ definition
- euclid's algorithm finds the ==greatest common divisor (GCD)== of 2 positive integers
- *note that GCD == HCF (highest common factor), and is simply the largest integer which divides both positive integers*
- ==given 2 positive integers a and b, a must be greater than b== - $a \gt b$

### ~ algorithm
- euclids algorithm can be defined in a simple recursive manner, as `gcd(a,b)`
```pug
gcd(a,b)
	if b = 0
		return a
	else
		r = a mod b
		return gcd(b, r)
```

### ~ example, a = 30 & b = 21
![ | 300](https://i.imgur.com/pgVFmen.png)
- the algorithm stops at the 3rd column, since it would be called as `gcd(9,0)`, thus b is 0 and $a$ (9) is returned