[[COMP24011]]

conditional independence is often used as it allows probabilistic systems to ==scale up==. Conditional independence is also more common to come across in comparison to ==asbolute independence==

conditional independence can normally be inferred from events which are the ==root cause== of other events

$$P(Cause,Effect_1,...,Effect_n) = P(Cause)\cdot \prod_i P(Effect_i|Cause)$$

this distribution is known as ==naive bayes== - it is known as "naive" because it is often used in cases where the $Effect$ variables are ==not conditionally independent== given the $Cause$