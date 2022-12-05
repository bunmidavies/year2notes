[[COMP26120]]


## skip list
- a skip list is a list that has nodes of variable size
- it is a generalisation of a sorted linked list
- known as a **randomised** data structure
![[Pasted image 20221204224532.png]]

-inf and +inf are known as **sentinel nodes**


## searching in a skip list
- skip as much as possible - check if the element you're looking for is greater than the next element on the current level
- if the value is greater, you can go to that next element (thus **skipping** anything on lower levels)
- if it is not, you have to go down a level

## complexities
[[skip list complexities]]