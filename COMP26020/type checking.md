[[COMP26020]]

### definition
- a values ==type== is just the set of properties associated with the value, thus a set of different types within a programming language is called its ==type system==
- type checking is the process of ==assigning/inferring== types for expressions within a programming language, and making sure such types are used legally
- inferrence for expression types is usually straightforward if a programming language has a ==declare before use== policy (i.e. state the variables type before you assign it) - type inference becomes difficult when declarations are not needed
- there are two main types of type checking:
	- ==statically checked== - types are checked at compile time
	- ==dynamically checked== - types are checked at run time

- programming languages may have tables which define the resulting types of certain operations with different types, for instance:
![ | 400](https://i.imgur.com/SfZtwFe.png)
