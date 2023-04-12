[[COMP24011]]

[[updating degrees of belief]]

- Bayesian updating is built off of Bayes' theorem

- Bayes' theorem:
  $$p(\varphi|\psi) = \frac{p(\psi|\varphi) \cdot p(\varphi)}{p(\psi)}$$
  
- And if $\varphi_1, ... , \varphi_n$ form a partition, by using the [[partition rule]]:

$$p(\varphi_i|\psi) = \frac{p(\psi|\varphi_i) \cdot p(\varphi_i)}{p(\psi|\varphi_1)\cdot p(\varphi_1) + ... + p(\psi|\varphi_n)\cdot p(\varphi_n)}$$
- where $\varphi_i$ is a singular proposition
- This is all under the assumption that $\varphi$ and $\psi$ ==don't have 0 probabilities==

- **it is important to be careful when revising probabilities - [[monty hall problem]] aims to demonstrate why**
