[[COMP26020]]

- lexical analysis is ==the first phase of compilation==. Characters are read, and sequences of tokens are produced - the idea is to recognise a programming languages ==parts of speech==
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
