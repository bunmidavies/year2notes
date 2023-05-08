[[COMP26020]] - [[C]]

### intro
- all of a programs code/data exists somewhere within memory - everytime a new variable is declared, more memory is allocated
- there are different kinds of memories used within programs:
	- ==stack== - stores local variables - ==allocation/deallocation== is automatic on the stack
	- ==heap== - heap memory is ==allocated and deallocated by programmers==, i.e. ==dynamically allocated==

### allocating to the heap
- `malloc` is the typical function used in C to find a specified amount of free memory, and return a pointer to it ([[pointers]])
- example:
```C
int size = 10;
int * heap_array = malloc(size * sizeof(int));
if (heap_array == NULL) return -1;
/*
code here ...
*/
free(heap_array);
```
- this memory ==must== be deallocated using `free`, otherwise a ==memory leak== will occur
- its important to also check that the returned pointer isnt null - this ensures that there was enough memory to be allocated