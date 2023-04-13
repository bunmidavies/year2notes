[[COMP26020]] - [[C++]]

- dynamic creation in traditional c++ required the `new` keyword in order to manually allocate memory

- for instance, if you wanted to create a pointer to some object that could be derived or the base class, **and you can only determine this based on current conditions**, a way that would work is the following:
```c++
BaseClass *ptr = (condition) ? new BaseClass : new DerivedClass;
```
**note that below doesnt work, as the classes only exist within their scope (their stack), which is that ternary operator**
```c++
BaseClass *ptr = (condition) ? BaseClass() : DerivedClass();
```
you will get a pointer to an **rvalue** ([[c++ move semantics]])

- the problem is that this method is not [[RAII]] compliant. In order to be RAII compliant, we'd need the lifetime of this new object we created to be associated with an automatic object
- smart pointers fit this exact description

***
## smart pointer
- a smart pointer encapsulates a raw pointer to the heap, and have custom constructors / destructors to manage the lifetime of the object being pointed to
- this basically means objects created within some functions scope can be binded to a smart pointer, in order to be used elsewhere, and deallocated automatically when no longer used
- the syntax is similar to regular pointers
***

- there are 3 main types of smart pointer: unique pointer, shared pointer and weak pointer
- we use smart pointers by dynamically creating an object, then passing its pointer to a smart pointer, which will then manage the memory deallocation for us
- we can do these two steps at once using `make_unique`/`make_shared`
`auto smart_pointer = (condition) ? std::make_unique<Base>() : std::make_unique<Derived>();`
