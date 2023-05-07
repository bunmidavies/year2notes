[[COMP26020]]

### definition
- in rust, functions need to represent the 'lifetimes' of their inputs/outputs if the compiler cant infer them
- a lifetime is essentially a stretch of code for which a variable is allocated for, and is used to ensure that a ==borrow is valid==
- lifetimes are explicitly referred to with a quotation mark followed by the variable, e.g. `<'m>`

### links 
- [rust by example - lifetimes](https://doc.rust-lang.org/rust-by-example/scope/lifetime.html)