[[COMP26020]]

- lexical analysis is ==the first phase of compilation==
- ==a stream of characters is turned into a stream of tokens==
- *in a natural language, mapping words to a part of speech is idiosyncratic, while in formal languages, mapping words to a part of speech is syntactic*
![](https://i.imgur.com/hYsN8DA.png)
- lexical analysis is useful to understand specification and implementation of languages, and to avoid writing lexical analysers by hand - we want to be able to specify ==lexical patterns== which can then be used to derive tokens, where different parts of this pattern can vary in complexity


### definitions
- since lexical analysis deals with the structure of the language, a few definitions are useful (mainly covered in computation y1)
	- ==vocabulary== = finite set of symbols
	- ==string== = finite sequence of symbols from vocab
	- ==language== = set of strings over fixed vocab. in the context of a CFG - all terminal productions over a CFG
	- ==grammar== = finite way of describing a language
	- ==context free grammar (CFG)== = 4-tuple, consisting of:
		1. starting symbol
		2. set of non-terminal symbols
		3. set of terminal symbols
		4. set of production rules

### example grammar
![](https://i.imgur.com/T7R23J9.png)

### practical considerations
- note that if a programming language is designed poorly, it can cause problems with lexical analysis
- for instance, ==template syntax in C++== allows you to write something like:
```c++
aaaa<mytype<int>>
```
- but since `>>` is an operator in c++, confusion be caused, and this is something that the lexical analyser cannot handle - this can typically be sorted by the parser, in [[syntax analysis]] (by matching opening and closing brackets)