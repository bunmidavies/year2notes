[[COMP24011]] / #comp24011

Recommended reading is Chapter 14.1 - 14.4 [[r+n.pdf]]

- the robot example that was used in the lectures to describe [[Bayesian Updating]] would work, but has a problem - it would struggle sometimes with processing the amount of data (for instance a 3D array holding a probability distribution)
- **bayes networks** are the most important technique to solving scalability issues within bayesian updating

- State descriptions and a few other terms are covered in [[bayes networks - independence]]
- Using these definitions, the lecture moves onto actual bayes networks below
- The lecture follows on with how to calculate probabilities using bayes networks in [[calculating w bayes networks]]

## network example + explanation

- bayes networks are data structures which aim to store probability distributions in a more compact form
- we take $Y_1,...,Y_m$, where each $Y$ is either $y_i$ or $\neg y_i$

- $\pi$ shows the parents of a given node in a network
  ![](https://i.imgur.com/aPW9rlX.png)


- the joint probability distribution for a group of random variables is given as the **product of each variable, given its parents** (shown below)
  ![](https://i.imgur.com/8hIN6Ez.png)


- Given the example above, this means that
  $$p(X_1,...,X_7)$$
  is equal to:
  $$ p(X_6|X_3,X_4) \cdot p(X_7|X_4,X_5) \cdot p(X_3|X_1) \cdot p(X_4|X_1) \cdot p(X_5 | X_2) \cdot p(X_1) \cdot p(X_2)$$

- Where each $X$ is just a **possible** value of the given variable (in reality, it can be $x_i$ or $\neg x_i$)

- Using this info, we can create a [[formal definition of bayes network]]