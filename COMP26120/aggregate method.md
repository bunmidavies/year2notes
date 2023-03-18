[[COMP26120]]

the aggregate method is a method used to perform [[amortized analysis]], in order to gain an average time for each operation related to some ==data structure==

in aggregate analysis, we show that for all $n$ (any size), a sequence of $n$ operations takes worst-case time $T(n)$ in total. In the worst case, the ==amortized cost== per operation is $T(n)/n$

So by figuring out $T(n)$ then dividing it by $n$, you receive the ==amortized cost== - in the aggregation method, this cost applies to each operation, even if there are several types of operation in the sequence

the aggregate method ==differs to other methods== because the method assigns the same amortized cost to ==all== operations

### example 1 : stack (MULTIPOP)

consider stack operations `PUSH` and `POP`, both taking $O(1)$ time

so this means we consider the *cost* to be 1. If we have a ==sequence== of $n$ `PUSH`/`POP` operations, the actual running time for $n$ operations is $\Theta(n)$

we create a new stack operation `MULTIPOP(k)`, which removes the $k$ top objects from a stack (or the entire stack if its size is less than $k$)

we want to analyze a sequence of $n$ `PUSH`,`POP`, and `MULTIPOP` operations on an initially ==empty stack==

we know that the worst case cost of a `MULTIPOP` must be $O(n)$, since in the worst case we have a stack of size $n$. This is the ==worst cost== in comparison to `PUSH` and `POP` being $O(1)$, so we can say this entire sequence costs $O(n^2)$
*this worst case could occur where we have $O(n)$ MULTIPOP operations costing $O(n)$ each*

==however== we find that any sequence of $n$ `PUSH`/`POP`/`MULTIPOP` operations costs at most $O(n)$. This is because there can only be as many `POP` operations as there are `PUSH` operations (`MULTIPOP` is also just made up of `POP`s)

this means for any $n$, the total sequence of $n$ `MULTIPOP`/`POP`/`PUSH` will take $O(n)$

$O(n) / n = O(1)$ amortized time per any stack operation


### example 2 : incrementing a binary counter

we want to implement a ==k-bit binary counter==, that counts up from 0

we can do this using an array of bits ($A$), where $A$.length=$k$
the lowest order bit i.e. 0, is stored in $A[0]$

the `INCREMENT` operation itself is defined as follows:
![](https://i.imgur.com/SbRdMy0.png)


so the cost of each `INCREMENT` is lienar in the number of bits flipped in the first `while` loop

since there are $k$ bits, the worst case is $\Theta(k)$, so a ==sequence of n INCREMENT operations== must take $O(nk)$ in the worst case (which in this case would give us an amortized time of $O(k)$ for each operation)

however, in general for $i = 0,1,...,k-1$, bit $A[i]$ will flip $n/2^i$ times for a sequence of $n$ `INCREMENT` operations

using info on [[geometric series]] we can sum this to $2n$.

the worst-case time for a sequence of $n$ `INCREMENT` operations then ends up being $O(n)$, thus the ==amortized cost== becomes $O(n) / n = O(1)$ per `INCREMENT`
### example 3 : stack (MULTIPUSH)

if we take the previous example we had with ==MULTIPOP==, but instead have ==MULTIPUSH==, which pushes $k$ items onto the stack, would the $O(1)$ bound on the amortized cost of all stack operations still hold?

consider you now have a sequence of $n$ `PUSH`, `POP`, and `MULTIPUSH` operations

in the worst case, we have $n$ `MULTIPUSH` operations. This means that $k$ `PUSH` operations take place within each `MULTIPUSH`, giving the worst case bound of $\Theta(nk)$. 

therefore, we amortize this worst bound giving us $\Theta(k)$ per operation. $k$ is ==NOT a constant==, which is the reason we can not reduce this to $\Theta(1)$