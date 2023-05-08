[[COMP26020]] - [[C]]

### enums
- an enumeration is a user defined type, allowing the programmer to assign textual names to integer constants
- what makes enumerations useful is that the compiler assigns the integer constants ==under the hood== 
- this means you can just use the enum values without worrying about the actual integer values
- example:
```C
enum color {
	RED,
	GREEN,
	BLUE
};

int main() {
	enum color c1 = BLUE;

	switch(c1) {
		case RED:
			printf("c1 is red\n"); break;
		case GREEN:
			printf("c1 is blue\n"); break;
		case BLUE:
			printf("c1 is green\n"); break;
		default:
			printf("unknown colour");
	}

	return 0;
}
```
- by convention, enums are typically ALLCAPS
- enumerations can also be typedef'd ([[custom types in C]]), in order to avoid using `enum` with every declaration
- the typedef declaration works the same as you would with a struct