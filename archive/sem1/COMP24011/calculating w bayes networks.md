- we now know what a bayes network is ([[formal definition of bayes network]]), but the important part is retrieving information from a network
- the following example continues from the example within [[bayes networks]]

***
### calculation example
- original distribution
$$ p(X_6|X_3,X_4) \cdot p(X_7|X_4,X_5) \cdot p(X_3|X_1) \cdot p(X_4|X_1) \cdot p(X_5 | X_2) \cdot p(X_1) \cdot p(X_2)$$
- we have evidence that $\neg x_1$ and $x_7$, and want to find $p(x_3)$
- we fix these values into our calculation
$$ p(X_6|X_3,X_4) \cdot p(x_7|X_4,X_5) \cdot p(X_3|\neg X_1) \cdot p(X_4|\neg X_1) \cdot p(X_5 | X_2) \cdot p(\neg X_1) \cdot p(X_2)$$

- using our knowledge of [[Bayesian Updating]], we have $p(X_2,...,X_6|\neg x_1, x_7) =$
$$\frac{p(\neg x_1,X_2,...,X_6,x_7)}{p(\neg x_1 \land x_7)}$$
- thus $p(X_3|\neg x_1, x_7) =$
$$\sum_{X_2,X_4,X_5,X_6} \frac{p(\neg x_1,X_2,...,X_6,x_7)}{p(\neg x_1 \land x_7)} $$
- we can define the above as a function $f$, and we know this is the same as
$$\sum_{X_6,X_4,X_5,X_2}p(X_6|X_3,X_4) p(x_7|X_4,X_5) p(X_3|\neg x_1) p(X_4|\neg x_1) p (X_5|X_2) p(X_2) p(\neg x_1)$$
**summed in the order $X_6, X_4, X_5, X_2$.** More on variable ordering after the e.g.

- we can then simplify parts of above into sums, by going in our variable order
  $$\sum_{X_6,X_4,X_5}p(X_6|X_3,X_4) p(x_7|X_4,X_5) p(X_3|\neg x_1) p(X_4|\neg x_1) p(\neg x_1) \sum_{X_2} p (X_5|X_2) p(X_2) $$
- note that we removed $X_2$ from the overall sum on the left, and can now refer to it as a function
 $$\sum_{X_6,X_4,X_5}p(X_6|X_3,X_4) p(x_7|X_4,X_5) p(X_3|\neg x_1) p(X_4|\neg x_1) p(\neg x_1) H_2(X_5) $$
- we do this for $X_5$ (reordering then simplifying with function)
  $$\sum_{X_6,X_4}p(X_6|X_3,X_4)  p(X_3|\neg x_1) p(X_4|\neg x_1) p(\neg x_1) \sum_{X_5} p(x_7|X_4,X_5) H_2(X_5)$$
   $$\sum_{X_6,X_4}p(X_6|X_3,X_4)  p(X_3|\neg x_1) p(X_4|\neg x_1) p(\neg x_1) H_5(X_4) $$
- now $X_4$
 $$\sum_{X_6}  p(X_3|\neg x_1)  p(\neg x_1) \sum_{X_4} p(X_6|X_3,X_4) p(X_4|\neg x_1) H_5(X_4) $$
  $$\sum_{X_6}  p(X_3|\neg x_1)  p(\neg x_1) H_4(X,3,X_6) $$
- and finally $X_6$
$$p(X_3|\neg x_1) p(\neg x_1)  \sum_{X_6} H_4(X,3,X_6) $$
$$p(X_3|\neg x_1) p(\neg x_1)  H_6(X_3)$$

- so with this complete, we have the following (taken from the lecture)
![](https://i.imgur.com/LgGrGYy.png)

where the values in <span style="color:red">red</span> are stored in our bayes network

$$p(X_3|\neg x_1 \land x_7) = \frac{f(X_3)}{p(\neg x_1 \land x_7)}$$
- therefore
![](https://i.imgur.com/BKRvMzo.png)


- from what i understand, this process is necessary because **we don't know $\alpha$ beforehand
***
- calculations **always work** regardless of the ordering, but efficiency does vary depending on how you've ordered it
- in order to make a bayes network as efficient as possible, you should try and make it look like a **tree** as much as possible
- further optimisations are kind of over the scope of COMP24011