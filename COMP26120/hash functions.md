[[COMP26120]]

- hash functions are an essential part of a [[hash map]]

there are a couple of problems that hash functions are faced with:
- **hashing problem** - given a universe $U$ of keys, create a function that maps each key to an integer in the range \[0,N)
- **uniform hashing problem** - given a universe $U$ of keys, create a function that uniformly maps each key to an integer in the range \[0,N) 

- a hash function maps a universe of keys to a set of integers
- <span id="important">there are two main parts of a hash function</span>
	- hash code - mapping the universe to an integer
	- compression - compressing the integer to an integer in the range \[0,N)

## hash codes
- what we want to hash can be seen as a sequence of integers - and we want to create a single integer using this
- symmetry / not accounting the order of sequences will cause collisions
- polynomial based hash codes can help to avoid symmetry, for instance $a_0c^{n-1} + ... a_{n-1}$
- where $c$ is a constant you choose
## compression
- $mod$ n is one of the most common compressions - but can run into problems depending on which $n$ you choose.
- making $n$ prime is a common way to get uniformity in compression
- making $n$ a power of 2 is also a common method (but may result in more collision - an XOR may also be performed to prevent this)

