[[COMP24112]]

### definition
- normal equations are used for solving linear systems when trying to reach the [[optimality condition]] for parameters in a given ML model
- we aim to solve the equation where the ==gradient of the error function is equal to 0==

 > in reality - these equations are not always solvable, or the computational complexity to solve them is so high that it is not feasible - this is why other methods like [[gradient descent]] exist

### single output
![ | 550](https://i.imgur.com/kJ2yWRb.png)
- we take the formula at the top and set it to 0, and can rearrange it to obtain the ==normal equation== for the least squares problem
![ | 550](https://i.imgur.com/mecsgCV.png)
### multi-output
- the same idea basically applies to multi-output - read [[linear least squares]] to see where the multi-output equation is from
![ | 550](https://i.imgur.com/dWjXL5E.png)

```mermaid
graph TD 

Biology --> Chemistry 

class Biology,Chemistry internal-link;
```
