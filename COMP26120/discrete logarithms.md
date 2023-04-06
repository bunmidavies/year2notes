[[COMP26120]]

### ~ definition
- the discrete logarithm of an integer $y$, base $b$, is the integer $x$ such that:
$$b^x = y \textrm{ mod } n$$
- this is the inverse of modular exponentiation, which can be calculated with [[fast modular exponentiation]]
- however, ==there is no fast algorithm for calculating discrete logarithms== - this is one of the reasons modular exponentiation is able to provide a one way function for [[el gamal encryption]]