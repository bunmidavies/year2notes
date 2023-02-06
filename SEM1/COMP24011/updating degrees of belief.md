[[COMP24011]]

- ==conditional probability==:
  *given $p$ is a probability assignment*
  $p(a\land b) / p(b)$ is known as the probability of $a$ given $b$, and is written $p(a|b)$

- in the lectures this is denoted as $p_b(a)$, and is another way of saying **the degree of belief $p$ would have in $a$ if he learned $b$**

- Proposal: Given after learning $b$, the probability of $a$ should become **equal** to $p(a|b)$

- Diachronic [[dutch book theorem]] argument is used to prove that this proposal is true
- This argument takes the notion that 
$p(a)$ (not updated after learning b) > $p(a|b)$
- The argument shows that a dutch book can be formed which shows that this statement causes irrational bets, and makes the agent lose in every case of the dutch book

- Therfore: assuming $p(b) \neq 0$
  $$p_b(a) = p(a|b)$$
  This is [[Bayesian Updating]], a ==belief-revision policy==