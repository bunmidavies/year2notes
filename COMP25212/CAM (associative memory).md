[[COMP25212]]

### ~ definition + uses
- CAM is ==Content Addressable Memory==, but also known as ==associative memory==
- in RAM, an address goes in, and data comes out- this is basically the ==opposite== to CAM where data goes in, and an address where this data is stored comes out (more or less)
- in the context of [[fully associative cache]], the data going in is the ==memory address==, and the expected result is the tag which is storing this memory address
- CAM is not directly part of main memory hierarchy - its a component it may be used in different architectural elements such as:
	- highly associative caches
	- packet routing lookup (in networks)
	- AI/ML acceleration

![ | 450](https://i.imgur.com/X2xddDQ.png)
