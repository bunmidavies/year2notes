[[COMP26120]]


## skip list
- a skip list is a list that has nodes of variable size (having a height between 1 and O(logn))
- it is a generalisation of a sorted linked list, making it easy to implement
- known as a ==randomised== data structure
![](https://i.imgur.com/fmVXYsG.png)


-inf and +inf are known as **sentinel nodes** - the sentinel nodes always mark the ==start== and the ==end== of the list

- ==note that the skip list must be sorted==

## searching in a skip list

- the goal while searching in a skip list is to skip over as many nodes as possible, while not skipping over the node you want
- this is achieved by inspecting the ==next nearest key== within the current height
- if ==next key < value==, you can skip over all the elements to this key
- if ==value < next key==, then you must go down a level


## inserting in a skip list

- the insertion process in a skip list is very similar to the search process, except when reaching the bottom level, once a node which has a ==greater== value than what we are trying to insert lies ahead, we insert our new node here
- in order to decide the height of the new node, we use coin flips, this is what makes the skip list a ==randomised== data structure

## complexities
[[skip list complexities]]

