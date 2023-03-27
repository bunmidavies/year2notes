[[COMP26020]] 

- the LL(1) property is useful within [[top-down parsing]], and essentially means:

given $A\rightarrow B$ and $A\rightarrow C$ both appear in the grammar, any first terminal symbol produced by $B$ must be different from any first terminal symbol produced by $C$

- this property allows the parser to make a correct choice with a lookahead of 1 symbol, and prevents a grammar from being ==left-recursive== (check [[top-down parsing]] for an example)
- if the LL(1) property doesnt exist for a grammar, it can typically be introduced by transforming the grammar, factoring any common prefix:
- $A \rightarrow ab_1 | ab_2 | ab_3$ would become $A \rightarrow aZ$ and $Z \rightarrow b_1|b_2|b_3$