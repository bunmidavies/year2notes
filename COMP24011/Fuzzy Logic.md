[[COMP24011]]

- By this point, what an [[object]] is, and how they can be members of certain [[categories]] should be clear
- Fuzzy logic becomes involved when the requirements for an object to be a member of a certain category isn't completely clear

- Fuzzy logic is the method for reasoning with logical expressions describing [[Fuzzy set]]s
- Example: the truth value of $Warm(d) \land Humid(d)$ is a function of truth values of its components
	- $T(A\land B) = min(T(A),T(B))$ - to what extent is it warm and humid?

- Fuzzy set theory is described below, and by using these ideas a [[Fuzzy Control]] system can be constructed

***
## Fuzzy Set Theory

- Fuzzy set theory specifices how well an object belongs to a specific category
- For instance, "It's **warm** today"
	- What is warm specifically?
	- There are different degrees of being warm, and different perspectives on what that may be
	- $Warm(d)$ has a truth value which is a continuous number between 0 and 1 (Rather than $warm$ just being `true` or `false`)

- Fuzzy sets are defined by membership functions
- Given a temperature, we may want to determine if it is hot, warm or cold
- For fuzzy sets, **a value can belong to multiple fuzzy sets simultaneously**

- e.g. $t$ = 21 degrees
	- $Hot(t) = 0$
	- $Warm(t) = 0.2$
	- $Cold(t) = 0.8$

