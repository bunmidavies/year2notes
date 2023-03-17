[[COMP26120]]
[[data structure complexities]]

## average complexities
- we assume there is a uniform distribution of elements, in order to arrive at these average complexities

- find: $O(logN)$
  you have to traverse the tree to find any element - with uniform distribution, you should be halving the number of elements each time
- insert: $O(logN)$
  to insert, you need to find the insertion point. So this just uses find
- delete: $O(logN)$
  same case as above

## worst complexities
- we assume that the worst case is where the tree looks like a chain, where every element only has 1 child
![](https://i.imgur.com/dYCPOtr.png)


- the worst case for **all** operations is $O(N)$
