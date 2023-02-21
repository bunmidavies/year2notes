[[COMP24112]]

**Optimal** simply means best

==Mathematical optimisation== finds the inputs that can give the minimum or maximum output of a real valued function

In machine learning we are trying to develop an algorithm which can systematically choose the possible function inputs which give the 'best' output values

Optimisation takes a general form:
- min: $O(x_1,x_2,...,x_n),$
- subject to: $f_1(x_1,x_2,...,x_n) \leq 0,...,f_m(x_1,x_2,...,x_n) \leq 0$

$O$ is the ==optimisation objective function==, i.e. the loss function

$f_1,...,f_m$ are the ==constraints== - these restrict the sets from which the input variables can choose values from

![](https://i.imgur.com/tij3kpC.png)