[[COMP26120]]

- a disjoint set is a colloection of disjoint sets that can be merged

## disjoint set operations
- add(x) : creates a new set with x
- find(x) : finds the set that contains x
- union(x,y) : merge sets x and y

## example - connected components
- given a set of edges between components, you may want to find out if any two components are connected to eachother

- DS = new disjointSet()
- for x in components:
	- DS.add(x)
- for (x,y) in edge:
	- DS.union(x,y)

- to check if two components are connected:
  DS.find(component1) == DS.find(component2)
- as find will return the corresponding set

## disjoint set structures
- disjoint sets need two main operations - find and union
- different data structures will typically provide a fast find, or a fast union, **but most do not provide both**

- linked structure
there is a pointer to each item, so find is O(1)
but each pointer would need to be updated for union, so union is O(n) (n pointers)

- array structure
value stored at array[i] is the set which item i belongs to
find is O(1)
but union is also O(n)

- rooted trees
find is O(n)
union is find + O(1)

## path compression
- path compression can be performed on rooted trees, to improve the find operation. as seen above, the union operation can be efficient, but the find operation is not
- path splitting is like path compression, but only moving to the grandparent of the parent pointer
- path halving similar to above