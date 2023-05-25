[[COMP26020]] - [[C++]]

- **All containers are templated**, i.e. the data type for any given container is a template parameter
- This means a common limitation to C++ containers is being restricted to only storing one type within any container

The 3 core types of C++ container

The 2 core types of container like objects:
- Adaptors: Stack, Queue, Prio Queue
- Views: Span, mdspan

Non containers:
- Tuple, pair

![](https://i.imgur.com/2CIIxZh.png)


Containers in C++ have a *common interface* - a list of functions which work across all containers regardless

***
### exam specific containers

- vector
- array
`size of the array exists within the template parameters for an array, for instance `std::array<int,5>` declares an array of size 5 `
- unordered_set
- unordered_map
- [[C++ span]]
- tuple
- pair