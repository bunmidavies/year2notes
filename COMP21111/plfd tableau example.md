[[COMP21111]]

refer to [[tableau rules]] / [[tableaux for plfd]] / [[connective precedence]]

is $\neg(mode \in \{idle\} \lor mode \in \{cooking\} \rightarrow mode \in \{idle\})$ satisfiable?

a) $\neg(mode \in \{idle\} \lor mode \in \{cooking\} \rightarrow mode \in \{idle\}) = 1$
- top connective is negation, $\neg$

b) $(mode \in \{idle\} \lor mode \in \{cooking\} \rightarrow mode \in \{idle\}) = 0$
- top connective is implication, $\rightarrow$

c) $(mode \in \{idle\} \lor mode \in \{cooking\}) = 1$
d) $(mode \notin \{idle\})$
- we can apply one of the exclusive expansion rules for plfd on d)

e) $(mode \in \{cooking, defrost\})$
- going back to c), the top connective is disjunction $\lor$

f) $mode \in \{idle\}$
g) $mode \notin \{cooking\}$
- using the last tableau rule related to the conjunction of sets, we get the following

path f) = $mode \in \{\}$ - *closed*
path g) = $mode \in \{idle,defrost\}$ = $mode \in {defrost}$ - *open*

therefore, this branch is **satisfiable** due to there being an open branch