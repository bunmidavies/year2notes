[[COMP26020]] - [[C++]]

### definition + use
A template is the generic programming mechanism in C++

- templates are only instantiated for specific types at compile-time

```C++
template<typename T> T max(T& a, T& b)
{
	...
};
```

To call a function which has a template, provide the types required within the template while calling the function

```C++
int x = 3;
int y = 5;
max<int>(x, y);
```

- **for both functions and classes, simply prepend `template<typename T>` before the definition, and this enables templates**
- [[Python vs C++ Templates]]

- Templates in C++ are very powerful - they are in fact ==turing complete==