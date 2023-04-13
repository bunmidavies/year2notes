[[COMP26020]] - [[C++]]

- the key thing to understand about manual memory allocation, is that it implies we also have to manually deallocate memory
- the most obvious drawback of this is that memory leaks now become a possibility

- the alternative to manual memory allocation is [[RAII]]
- RAII promotes dynamic memory management in automatic objects. This means
	- the object constructor / methods will allocate memory for you
	- the object destructor will deallocate this memory
	- the object destructor is also called automatically (no need to use `delete`)

- in c++, the right hand value / object you assign to another variable will be **copied**. this means, for large objects (for instance a vector with many values), you will be using a lot of memory using regular assignment

- with c++, another general point to understand is that variables within the scope of a function will be declared **on the stack** - therefore, it is kind of against c++ principles to be able to directly return a variable defined within a function
- note that objects will typically have things like their dimensions stored on the heap, but their data will exist on the stack

- move semantics can be used to move references that are about to be deleted - **rvalues** - to another reference