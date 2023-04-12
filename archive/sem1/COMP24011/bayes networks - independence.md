[[COMP24011]]
A state description is a formula $\sigma$ taking the form
  $$\pm p_1 \land \pm p_2 \land ... \land \pm p_n$$
- where each $p$ is either $p$ or $\neg p$
- given there are $2^n$ state descriptions (for a given size $n$) - these state descriptions combined form a **partition**

- $a$ and $b$ are independent if 
  $$p(a|b) = p(a)$$
- $a$ and $b$ are positively relevant if 
  $$p(a|b) \gt p(a)p(b)$$
- $a$ and $b$ are negatively relevant if
  $$p(a\land b) \leq p(a)p(b)$$

- somewhat intuitively, $a$ and $b$ are conditionally independent given $\pi$ if
$$p(a\land b| \pi) = p(a|\pi)p(b|\pi)$$
or also if $p(a|\pi \land b) = p(a|\pi)$
conditional independence is used within the [[naive bayes]] equation, and is the idea that some variable may ==cause== other variables, but beyond that point these other variables are ==independent== to eachother