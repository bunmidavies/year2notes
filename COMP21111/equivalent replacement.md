Propositional formula notes from week1
**Equivalent Replacement Lemma:**
	*Let $I$ be an interpretation and $I \vDash A_1 \leftrightarrow A_2$. Then $I\vDash B[A_1] \leftrightarrow B[A_2]$* 
- **Notation**: $A[B]$ = formula $A$ with fixed occurence of formula $B$. Therefore $A[B']$ is the formula obtained from $A$ by replacing the occurence of $B$ with $B'$
- The lemma means by replacing $A_1$ with $A_2$ given they're equivalent, the syntactic structure is irrelevant thus the value of the resulting formula stays the same
- This becomes the **Equivalent Replacement Theorem**:
	  *Let $A_1 \equiv A_2$. Then $B[A_1] \equiv B[A_2]$.*

QBF
- let $I$ be an interpretation and $I \models F_1 \leftrightarrow F_2$. Then $I \models G[F_1] \leftrightarrow G[F_2]$
- Let $F_1 = F_2$. Then $G[F_1] = G[F_2]$
- *given two equivalent formulas, they can be replaced in a bigger formula, obtaining equivalent formulas for both*