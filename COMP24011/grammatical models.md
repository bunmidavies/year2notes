[[COMP24011]] / #comp24011 

grammatical models are used by agents in order to recognise [[natural language for communication]]

a ==grammar== itself is a set of rules used to define a language, as a set of allowable strings of words

they consist of 3 main components:
- ==lexical category== - nouns, adjectives, verbs
- ==syntactic category== - combinations of lexical categories. Noun + phrase = noun phrase
- ==phrase structure== - combinations of syntactic categories to form ==trees== (nested phrases)

a ==Context-free grammar== (CFG) is a set of rules where each rule takes the form of:
- A->$\alpha$
A = ==non-terminal== symbol
$\alpha$ = string of ==terminal== or ==non-terminal== symbols

a ==probabilistic== CFG is where the grammar assigns a probability to every string

[[syntactic parsing]] is the process of uncovering the phrase structure of some string of words, according to a grammar. 