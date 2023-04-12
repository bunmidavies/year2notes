[[COMP24011]] / #comp24011 

syntactic parsing is used in [[grammatical models]] with CFGs

a string can be parsed ==top-down== or ==bottom-up==

example:
![](https://i.imgur.com/Ct0Z9Rm.png)


uncovering the phrase structure is one thing, but uncovering ==intended meaning== is also a problem in itself

e.g. *Milk drinkers are turning to powder* isn't an ambiguous statement for humans when it comes to interpreting the intended meaning, but is ==highly ambiguous== to machines

there are several types of ==ambiguity==
- lexical: a word having more than one meaning
- syntactic: a phrase with multiple parses
- semantic: the actual meaning of the phrase
- metonomy: figures of speech where one object actually means another

probabilities can be then assigned to different interpretation to determine if it is the correct interpretation (this is known as ==disambiguation==) - different models may also be required such as:
- world model: likelihood of sentence occuring in the world
- mental model: intention of communicating a fact
- language model: likelihood that such a string of words will be chosen
- acoustic model: for ==spoken== communication