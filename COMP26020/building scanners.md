[[COMP26020]]

- there are a number of steps involved in converting a specification into code
- a ==scanner== is a software tool which essentially performs automated lexical analysis, based off a regular expression it has been given
- the term scanner is interchangeable with ==automatic lexical analyser==
- Flex (Fast Lexical Analyser Generator) and Lex are popular tools for generating lexical analysers - a regular expression is provided, and a C source file is outputted

There are ==4 main steps== to go from a regular expression, to a DFA:
1. Writing down the regular expression for the input language
2. Converting the RE to a NFA ([[thompsons construction - RE to NFA]])
3. Building the DFA which simulates / is a subset of the NFA ([[NFA to DFA]])
4. [[hopcrofts algorithm - DFA minimisation]]

- The reason we want a DFA, is because we can use its transition table to directly build a ==recogniser== that detects acceptance for a given stream of characters
- However, ==table driven recognisers can be inefficient==, since the entire table needs to be encoded - thus taking up large amounts of memory