[[COMP24112]]
aka least squares fitting, ordinal least squares solution

- the linear least squares approach can be applied to [[linear models]], both ones providing ==single outputs== and ==multi-outputs==
- the linear model is applied to the training samples, and then the sum-of-squares error loss is calculated
- how this is calculated for single-output/multi-output systems is shown below

![|800](https://i.imgur.com/poPRAJU.png)

- we can see that the two basically dont differ, other than single output having a $w$ and $y$ vector, while multi-output has a $W$ matrix and $Y$ matrix - this also means that in order for the minimal error of zero to be achieved, the following linear equations have to be solved:
	- single-output: $\tilde{X}w = y$
	- multi-output: $\tilde{X}W = Y$

- where there are ==more== training samples than input features ($N>d$), the system is ==overdetermined==
- where there are ==less== training samples than input features ($N < d$), the system is ==underdetermined==
- if $\tilde{X}^T\tilde{X}$ is invertible, there is a ==unique== solution
- if $\tilde{X}\tilde{X}^T$ is invertible, there are ==infinitely many== solutions, but we want the one with the minimum norm:
![ | 350](https://i.imgur.com/biFTbxL.png)
- as can be seen, there is a repeated part within both of these equations, which is called the ==pseudoinverse== of $\tilde{X}$ - this can be calculated with ML libraries e.g. `numpy.linalg.pinv`
![ | 350](https://i.imgur.com/p0Dzcf3.png)
- [[normal equations]] are used to find the solution, as opposed to manually solving linear equations