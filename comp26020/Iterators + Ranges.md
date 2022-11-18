- Iterators aim to emulate [[pointers]] in arrays - they are basically **generalised pointers**

- Operators within iterators are overriden by different containers, in order to traverse such containers as needed

- By doing this, iterators abstract away how to actually access the container, and programmers use generic code which works for all containers

*tedious iterator method*
- calling `begin()` on a container returns the iterator pointing to the first element in the container
- calling `end()` on a container returns the iterator point to **just past the last element in the container**
- by using these, you are able to traverse a container by incrementing the iterator which pointed to the beginning, until it is equal to the end iterator

- by using `auto`, we can avoid declaring the iterators type at the start of each line as it is obvious

- Range-for
  ```C++
  std::vector<int> c1;
  for (auto& elem: c1)
  {
	  //do something
  }
```

- More on [[C++ ranges]]