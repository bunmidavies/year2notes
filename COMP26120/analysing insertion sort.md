`week 2` !

![](https://i.imgur.com/ozd5aFJ.png)


==example runthrough==

![](https://i.imgur.com/AWFsrg7.png)

`a[j] > key` therefore we make `a[j+1] = a[j]`
![](https://i.imgur.com/wKsAsR5.png)

afterwards, we decrement j and make `a[j+1] = key`
i is incremented because this is a for loop
running through the next iteration, we make `key = a[i]` where `i` now equals `3`
![](https://i.imgur.com/jMwD0AJ.png)

the condition `a[j] > key` isnt met, therefore we dont go through the while loop
i now becomes 4, and key becomes a[i] i.e. 20
![](https://i.imgur.com/uEIDgjX.png)

the while loop condition is met again, so 20 gets swapped with 40
20 will then get swapped with 30 as well, and the key gets reinserted
![](https://i.imgur.com/DAn7TyI.png)


list is sorted!

***
### conditions
- `preconditions` of the sort: at least 2 elements
- ==how many times does the while loop run?== - $n - 1$. This is because the for loop begins with $i = 2$
- `postconditions` of the sort: list is in sorted order

therefore we can define the following terms:
- invariant: `A[1..i-1]` consists of elements originally in `A[1..i-1]`, but in sorted order
- termination condition: when `i == n+1` (video uses 1-based indexes in the array)
***
### cost of program in terms of effort
![](https://i.imgur.com/BGppGxw.png)

for each instruction, we consider it to have some set amount of time to be executed. This means, we assign a constant $c$ to each line of code - we do not need to break this down into assembly or even consider what this constant might be at this time, but we need to be ==aware== of this

we define $T$ as the ==total number of while loop executions== across each and every outer loop. I.e.
$$T = t_2 + t_3 + ... + t_n$$
where $t_i$ is the $i$'th for loop iteration

therefore, we can sum the total time for this program
![](https://i.imgur.com/fLxbdbN.png)


what are the potential case scenarios which affect this sum?

### ==best case time calculation==
$T = t_2 + t_3 + ... + t_n$
![](https://i.imgur.com/HGfaAsP.png)

each of the times are a constant 1, so you get $n - 1$ 1's since you start from $i = 2$

now we know $T(n) = c_1n + ... + c_7(n-1)$ previously, but now we can remove any mention of $T$ with $n-1$, and simplify the equation
$$T(n) = c_1n + c_2(n-1) + c_3(n-1) + c_4T + c_5(T-(n-1)) + c_6(T-(n-1)) + c_7(n-1)$$
$$T(n) = c_1n + c_2(n-1) + c_3(n-1) + c_4(n-1) + c_7(n-1)$$
$$T(n) = (c_1 + c_2 + c_3 + c_4 + c_7)\cdot n - (c_2 + c_3 + c_4 + c_7)$$
$$T(n) = c_1n - c_2$$
$$T(n) = O(n)$$

### ==worst case time calculation==
so for the best case we know that the while loops are going to be executed for all possible loops
![](https://i.imgur.com/dsPaRvZ.png)


(assuming we wont have to do some shit like this in the exam but who knows)
![](https://i.imgur.com/AbLhmO8.png)


by mashing all the sums involving constants into singular constants, we obtain:
$$T(n) = an^2 + bn - c$$
therefore
$$T(n) = O(n^2)$$

### average case ???
- this is not the focus of COMP26120