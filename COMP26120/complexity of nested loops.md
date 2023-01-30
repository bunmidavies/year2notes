[[COMP26120]]

example:
```Java
for (int i = n; i > 0; i /= 2)
{
	for (int j = 1; j < n; j *= 2)
	{
		for (int k = 0; k < n; k += 2) 
		{
			//constant number of operations
		}	
	}
}
```

- we do not worry about the constants involved within these loops, we just need to take into account how it *grows*

- for instance `for (int k = 0; k < n; k += 2)` grows constantly. It may take $n/2$ iterations, but the $2$ is still a constant, so we classify this loop as $O(n)$

- next, we see that $j$ ==doubles== with each iteration. This is different to $O(n)$, and we can class this loop as ==logarithmic== i.e. $O(logn)$
- what is the base of the log? depends on what is being multiplied. Since it is being multiplied by 2 here, we class it as $O(log_2n)$

- the same logic as above, applies to the very outer loop. We may have changed how we adjust the for loop counter, but the growth is still logarithmic

- we piece these loops together depending on how they're nested
$$O(logn) \cdot O(logn) \cdot O(n)$$
the final complexity is 
$$O(n(logn)^2)$$