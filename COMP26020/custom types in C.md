[[COMP26020]] - [[C]]

### declaring a custom type
- use `typedef` to declare a custom type in C

### declaring a custom data structure
- `struct` is used in C to define a data structure with named fields
- the fields of the variable can be accessed using `<var_name>.<field_name>`
- declare a new struct using `struct <struct_name> newStruct`
- example:
```C
struct person {
	char name[10];
	float height;
	float weight;
}

void print_person(struct person p) {
	printf("%s has a height of %f and weighs %f",p.name,p.height,p.weight);
}
```
- the fields of a struct are ==placed consecutively in memory== (though the compiler may insert padding)

### combining custom types with structs
- in order to not have to use `struct` when declaring a new struct everytime, `typedef` can be used
- for instance `typedef struct struct_name s`
- now the new struct can just be created using `s`, or whatever name you choose
- an even faster way is to write `typedef struct` in the struct declaration, and end the declaration with the custom type name:
```C
typedef struct {
	char name[10];
	float height;
	float weight;
} person;
```