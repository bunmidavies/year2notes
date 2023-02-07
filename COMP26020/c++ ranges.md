[[COMP26020]]

- ranges are basically when you put begin / end [[c++ iterators]] in one
- containers with begin()/end() are automatically converted into ranges

- with functions like `find` where you would previously type:
```c++
std::vector<int> c1; find(c1.begin(), c1.end(), 0);
```
- now you can do:
```c++
std::vector<int> c1; find(c1,0);
```
- and get the same output

- [[c++ range views]] have only been added a couple of years ago, so not all compilers will actually support them