[[COMP24011]] / #comp24011 - [[fuzzy logic]]

- Fuzzy Control is a method of creating control systems where **fuzzy rules** are used to map **crisp inputs** into **crisp outputs**
![](https://i.imgur.com/0z7HfFC.png)


- Crisp means real values

***
## Initialisation

- [[Linguistic variables]] are the input/output variables involved in a fuzzy control system
- Membership functions are used to map crisp values between linguistic terms
- There are a number of membership functions which can be used (Gaussian, triangular, singleton, trapeziodal)

- Fuzzy rules must be defined
- A rule has the following structure: \<antecedent\> $\rightarrow$ \<consequence\>
- Example rule base:
	- if service = poor $\rightarrow$ tip = cheap
	- if service = good $\rightarrow$ tip = average
	- if service = excellent or food = delicious $\rightarrow$ tip = generous

***
## Fuzzification

- Fuzzification involves two steps to evaluate a number of antecedents, i.e. taking the *rule base* above into account
	1. Evaluate each separate antecedent (if a rule has multiple antecedents)
	2. Evaluate the overall antecedent (i.e. conjunction, disjunction, negation)

***
## Inference + Defuzzification

- Inference = Determining the consequent of each rule, and combining them
- Defuzzification =  Using membership functions to obtain the final crisp values

- There are two main approaches to fuzzy inference:
	- [[Mamdami fuzzy inference]]: Each rule outputs a fuzzy set
	- [[Sugeno fuzzy inference]]: Each rule outputs either:
		- A linear function
		- A constant
	- Which are defined by **singleton membership functions** (a function which only has a value of 1 at a single point, and 0 everywhere else)