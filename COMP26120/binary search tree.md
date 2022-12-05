[[COMP26120]]

- **binary search tree invariant**: left.val < node.val < right.val

- different [[tree traversal]]s will give us different sequences in a binary search tree - an in-order traversal gives us the elements in **ascending order**

- to search, insert, delete from a BST you always have to start from the root node

## removing from a BST
there are two main cases you may deal with when deleting from a BST (the third is if its a leaf node, which is simple)
- node to be deleted has a child - the child of the node is elevated i.e. takes to be deleted's space
- node to be deleted has 2 children - take the **in-order** successor of node to be deleted ([[tree traversal]])

- with the second case, this procedure may be recursive, as the in-order successor might be a subtree / not be a leaf. so you take the in-order successor of that node to replace it as well

## complexities of BST
- [[binary search tree complexities]]

## avl trees
- [[avl trees]] are a different type of binary search tree