[[COMP26120]]

- open addressing is a method of dealing with collisions within a [[hash map]]
- the most common example of open addressing is **linear probing**

- the main concept for open addressing is that **there is always one item within each bucket** - this differs to [[separate chaining]]

- if there is an item already sitting in the bucket you planned to insert an item into, there are 3 main techniques that comp26120 looks at:
	- linear probing: Probe (hash(k) + i) % N for $i = 0 \rightarrow N$
	- quadratic probing: Probe (hash(k) + $i^2$) % N for $i = 0 \rightarrow N$
	- double hashing: Probe (hash(k) + ($i \times hash2(k)$)) % N for $i = 0 \rightarrow N$

## linear probing
- the directly next available space is checked
- the main drawback of linear probing is the potential clusters it can cause (with poor [[hash functions]])

## quadratic probing
- quadratic probing creates secondary clusters, by squaring the current index ($0\rightarrow N$) % $N$ until an empty space is found

## double hashing
- one hash function is applied, and if its not successful, apply the second
- the main drawback is that the potential computation may be doubled, due to you using 2 hash functions every time