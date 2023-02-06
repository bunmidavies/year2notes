[[COMP24011]]

constraint satisfaction problems are a type of problem where a solution which ==satisfies== a set of constraints / requirements is required

CSPs typically ==model real-world situations==, typically involving things like scheduling, resource allocation problems, design and optimization problems

[[constraint networks]] are typically used to represent these problems

all constraint satisfaction problems can be viewed as a ==**search problem**==

we create a tree, where for each level a partial assignment is made. The first node in the tree is where no variables are assigned

While going down the tree, we can just eliminated nodes which violate the constraints, and traverse these nodes no further. **We will ==always find a solution== using this approach, however it is the ==least practical== as problem size increases**

forward checking aka [[constraint propagation]] is a more practical technique

another way of avoiding ==blind searching== is by finding [[cycle cut-sets]], which can remove redundant cycles in graphs representing constraint networks

the final method to solve constraint satisfaction problems covered in the lecture is [[backjumping]]