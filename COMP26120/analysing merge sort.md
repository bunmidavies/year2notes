algorithm:
![](https://i.imgur.com/XwOr4WD.png)


- in order to figure out how much the entire algorithm costs, we need to know what the merge algorithm is doing separately

## analysing runtime of merge subalgorithm

![](https://i.imgur.com/sVJX3VN.png)


- we then break down the runtimes of the lines separately:
```Java
n1 = mid-left+1
n2 = right-mid
create two sorted subarrays L[0..n_1] and R[0..n2]
```
all constant. $\Theta(1)$

```Java
for i=0 to n1 - 1
	do L[i] = A[left + i]
for j=0 to n2 - 1
	do R[j] = A[mid + j + 1]
```
these depend on the sizes of the arrays, $\Theta(n_1)$ and $\Theta(n_2)$

```Java
L[n1] = inf
R[n2] = inf
i = 0
j = 0
```
all constant. $\Theta(1)$

```Java
for k=left to right
	do if L[i] <= R[j]
		then A[k] = L[i]
			i+=1
		else A[k] = R[j]
			j+=1
```
this is the actual merging part of the algo, inserting everything into the list.
Therefore, $\Theta(n)$ (this is a tight bound because there is ==no breaking out of the loop==)

from this, we can deduce that this merging act is going to be linear

## analysing overall runtime of MergeSort
![](https://i.imgur.com/rFgZnX9.png)


MergeSort is annotated as $T(n)$ due to the $n$ subproblems it gets divided into
