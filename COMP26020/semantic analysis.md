[[COMP26020]]

### intro + definition
- prior to semantic analysis, [[syntax analysis]] has just taken place, where a ==parse tree== has been generated - this is the basic form of the intermediate representation which is given to the [[middle-end of a compiler]]
- the problem is that, at this point the code can still have errors which context-free grammars cannot detect - for example:
	- has a certain variable being referenced been declared?
	- is an expression ==type consistent?== ([[type checking]])
	- who is responsible for space allocation for some variable, and how long should it be preserved?
	- has a certain function been called with the right types of arguments?
- these questions ==rely on values, rather than syntax== - as well as this, non local information may be involved, and computation to figure out if an expression is legal may also be required

### using formal methods for semantic analysis
- formal methods like context-sensitive grammars or attribute grammars could not answer many of the questions posed above, just because its too difficult to encode these scenarios within grammars
- instead, using ==symbol tables== - described below - is the most important technique for semantic analysis

### symbol tables
- ==a symbol table is a data structure which acts as a central repository of facts==
- the symbol table itself could be one table, or a set of symbol tables within itself - it can be generated during [[lexical analysis]], and essentially would store:
	- variable names, defined constants, procedure/function names
	- with each of these symbols the following can be stored; textual name, data type, declaring procedure, storage info, number of parameters/types (for functions)
- to check a basic semantic question, a snippet of code can be checked against some production rule which executes each time the parser reduces that production ([[syntactic parsing]])
- for example, code that checks if a variable is declared before it is used, on a production rule like Factor $\rightarrow$ id
- this type of evaluation works well with the [[LR(1) property + LR parsing]]
- also since symbol tables will need to be constantly referred to, ==efficiency of access is critical==

### organising symbol tables
- linked lists:
	- the simplest approach, and has no fixed size
	- the main problem is that a lookup may take up to $O(n)$, so becomes very inefficient for larger lists
- binary trees:
	- the worst case for a balanced tree is $O(log_2n)$, which is an improvement from the linked list, but in the worst case the tree will deteriorate to a linear search as well
- hash tables:
	- the main challenge with hash tables are to come up with an inexpensive hash function and efficient collision policy
	- if the above requirements are met, hash tables can have $O(1)$ lookup

*week 4 pt 1 video covers stuff about hashing but notes on this basically already exist in [[COMP26120]]*

### issue - lexical scoping
- different programming languages have different ideas of ==scope== i.e. where two values can be referred to with the same name and not interfere with eachother
- the problem is that if there are multiple values with the same variable name, at some given point when one of these is used, the compiler needs to know which value is actually being referred to?
- the main workaround for this is to initialise a symbol table ==for each scope==