[[COMP24011]]

there are many known variants of ==backjumping==, but only one is covered in the lecture

when performing a search in a constraint satisfaction problem, if we violate some given ==constraint==, we do not simply want to jump back one node at all times

we want to jump back to the ==assignment which was involved in the violated constraint==

==Gasching backjumping== is the method covered in the lecture
It essentially jumps back to the first assignment which it believes will make a change in the outcome of the algorithm, i.e. will not jump back to try another value which violates the exact same constraint

![[Pasted image 20221231161711.png]]
![[Pasted image 20221231162252.png]]