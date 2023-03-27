[[COMP26020]]

- there are a number of steps involved in converting a specification into code
- a ==scanner== is a software tool which essentially performs automated lexical analysis, based off a regular expression it has been given
- the term scanner is interchangeable with ==automatic lexical analyser==

There are ==4 main steps==:
1. Writing down the regular expression for the input language
2. Converting the RE to a NFA ([[thompsons construction - RE to NFA]])
3. Building the DFA which simulates / is a subset of the NFA ([[NFA to DFA]])
4. [[DFA minimisation]]