*as taken from [the lecture](https://video.manchester.ac.uk/lectures/827834b4da3cb0ffc76bd7a4c8f4b14b/f1425505-ab41-4f54-85a3-d3c856ef8fad/)*

following on from [[bayes networks]]:

- A Bayes Network is a finite directed acyclic graph whose vertices are variables $X_1,...,X_n$, together with a conditional probability table $p(X|\pi(X))$ for each vertex (where $\pi$ gives the parents of a given vertex). The tables define a joint probability distribution on the Boolean random variables $X_1,...,X_n$, given by the equation:

$$p(X_1,...,X_n) = \prod^n_{i=1} p(X_i|\pi(X_i))$$
