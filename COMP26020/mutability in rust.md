[[COMP26020]]

### intro
- as mentioned in [[ownership in rust]], reference variables can be borrowed, and all reference variables have an owner
- basic types in rust such as `u32` ==dont need to be borrowed==, as ownership doesnt apply to them
- in rust, ==all variables are also immutable by default== 
- if a variable is to be modified, it needs to be explicitly declared as mutable

### `mut`
- mutable types in rust are declared using `mut` - e.g. `let mut i = 10;`
- a reference can also be made mutable, by using `&mut`