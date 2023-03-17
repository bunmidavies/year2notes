[[COMP26120]]

- binary search trees can be skewed, and cause problems with efficiency - we should aim for a **balanced tree**

- to calculate height balance at any point, take the height of the left child - high of the right child

## avl tree
- the avl tree has the same invariant as a [[binary search tree]], but has an additional invariant
	- height balance al all nodes is between **-1 and 1**

## rotation
- rotation is a tree manipulation operation, which moves nodes around in a tree while preserving invariants
![](https://i.imgur.com/Q3CI80w.png)


- sometimes, a single rotation won't be good enough, so double rotations can be used
![](https://i.imgur.com/1SglzS8.png)


## complexities
[[avl tree complexities]]