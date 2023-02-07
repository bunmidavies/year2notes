[[COMP26020]]

- range views are lightweight objects that indirectly represent [[c++ ranges]]
- they can contain an actual range, or just a recipe for constructing a range (lazy evaluation)


### lazy evaluation range views - natural numbers
- lazy evaluation - the range views can **represent** some kind of sequence, looking like they could continue to infinity, but only returning the values needed. For instance, creating a range view of all natural numbers looks like
```c++
std::views::iota v(1); // 1, 2, 3, 4, 5 ...
```
- we can do whatever we like with the view, for instance with some of the algorithms mentioned in [[fp in C++]]. these can also be piped to perform one after the other:
```c++
v = std::views::transform([](int x) {return (1<<x) - 1;}) |
		std::views::filter(is_prime) //lambda written elsewhere
```

- we can then take however many we want with `take`
```c++
auto res_view = std::views::take(v3, 8);
```
- and construct the vector we want
```c++
std::vector<int> output(v4.begin(), v4.end());
```


- there are a number of range view algorithms in `std::views`

### range view vs range examples
square a vector of numbers using ranges
```c++
std::ranges::transform(v,s.begin(), [](int x) {return x * x;});
```

square a vector of numbers using range views
```c++
auto view = std::views::transform(v, [](int x) {return x*x;});
//copy the view into a range
std::ranges::copy(view, s.begin());
```