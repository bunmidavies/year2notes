[[COMP26120]]

- binary search trees can be skewed, and cause problems with efficiency - we should aim for a **balanced tree**

- to calculate height balance at any point, take the height of the left child - high of the right child

## avl tree
- the avl tree has the same invariant as a [[binary search tree]], but has an additional invariant
	- height balance al all nodes is between **-1 and 1**

## rotation
- rotation is a tree manipulation operation, which moves nodes around in a tree while preserving invariants
![[Pasted image 20221204214746.png]]

- sometimes, a single rotation won't be good enough, so double rotations can be used
![[Pasted image 20221204215024.png]]

## complexities
[[avl tree complexities]]