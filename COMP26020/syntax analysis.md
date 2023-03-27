[[COMP26020]]

- ==syntax analysis is also known as parsing==, and takes place after [[lexical analysis]]
- lexical analysis produced tokens based off characters in the input program, and syntax analysis now aims to discover a derivation for ==sentences== within the input program, and answer the following:
	- Are the tokens in a syntactically correct order?
	- Do the tokens form valid sentences of the input language?
- Since regular expressions are unable to be used for things such as ==nested constructs==, as well as the fact that non terminal symbols cant be used before theyre fully defined, something more powerful than regular expressions are required for syntax
- ==context-free grammars== are the next most powerful way to express languages, and context-free syntax is specified with context-free grammars

### grammars
- a grammar is a ==4-tuple== $G=\{S,N,T,P\}$
	- $S$ = starting symbol
	- $N$ = non terminal symbols
	- $T$ = terminal symbols
	- $P$ = production rules

### derivation
- a ==derivation step== consists of replacing some non-terminal symbol in a sentence, and a ==derivation== as a whole is made up of these steps
- derivations can be represented using ==parse trees==
- ==choosing different non-terminal symbols at different times can lead to different derivations==
- there are 2 main types of derivation which are used within syntax analysis:
	- ==leftmost derivation== - at each step, replace the leftmost non-terminal symbol
	- ==rightmost derivation== - at each step, replace the rightmost non-terminal symbol

### derivation example

![](https://i.imgur.com/w55wjpF.png)
- it should be found that it is possible to find ==2 leftmost and 2 rightmost derivations==
*given $x-2*y$, when we try to take the leftmost nonterminal symbol, do we take x-2 as the leftmost nonterminal, or just x as the leftmost nonterminal? same goes for the right*

- ==a grammar is ambiguous if there are multiple leftmost / rightmost derivations== - [[ambiguity in grammars]]

### parsing
- the process of discovering a derivation for some sentence can be called ==parsing==
- there are two main [[parsing summary]] - ==bottom-up== and ==top-down== parsing