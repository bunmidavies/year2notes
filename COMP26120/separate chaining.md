[[COMP26120]]

- separate chaining is a method of dealing with collision in a [[hash map]]
- how this is technically implemented, is that each element within the array (the underlying data structure) just holds a pointer to a linked list
- so rather than adding the element you want to add directly to the array for the hash map, you actually create a new pointer (if not existing), then add the element to the end of this linked list
- this means when retrieving items from a hash map with separate chaining, we may have to search through the linked list the hash code points to first
- bad [[hash functions]] can result in your hash map potentially consisting of one linked list, with all your elements (which is not efficient/desirable)