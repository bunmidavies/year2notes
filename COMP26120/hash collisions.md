[[COMP26120]]

- hash collisions will probably inevitably occur within a hash map implementation
- what is key to note is that you should be using **1 method** to solve hash collisions - you shouldn't mix them together

- [[separate chaining]] is a common method to solve collisions - everything ends up getting held in a linked list
- [[open addressing]] is an alternative method which doesn't used linked lists, thus has less of a risk of increasing in complexity