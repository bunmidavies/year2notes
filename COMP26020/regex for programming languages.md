[[COMP26020]]

- patterns form a regular language. A ==regular expression== is a way of specifying a regular language - its a formula that describes a possibly infinite set of strings
- regular expressions allow [[lexical analysis]] to be ==automated== - we can encode a RE into a DFA, which can be represented with a ==transition table==, and build a lexical analyser which simply looks to the table to tokenize any input of a given language
- ==every regular expression can be converted to a Deterministic Finite Automaton (DFA)== - [[building scanners]]

### basic regex
- $\varepsilon$ is a RE denoting the empty set, $\{\varepsilon\}$
- if $a \in \textrm{Vocabulary}$, then $a$ is a RE denoting $\{a\}$
- if $r_1$ and $r_2$ are REs then:
	1. $r_1*$ denotes 0+ occurences of $r_1$
	2. $r_1r_2$ denotes concatenation
	3. $r_1|r_2$ denotes either $r_1$ or $r_2$
- $[a-d]$ is the same as $a|b|c|d$
- $r+$ is the same as $rr*$
- $r?$ is the same as $r|\varepsilon$

==Not all languages can be described by regular expressions==:
- regular expressions cant be used to describe balanced or nested constructs, e.g. nested ifs, any strings with balanced parantheses, the set of all 0s followed by an equal number of 1s
- in regex, a non terminal symbol cant be used before it has been fully defined