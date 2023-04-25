[[COMP24112]]

### definition + steps
- gradient descent is an iterative approach to minimising the [[loss function]] within a model:
	1. start with a random guess (the ==initial state==) $\Theta$, and apply a change to the guess
	2. this changed $\Theta$ aims at leading to a reduced value of the loss function
![ | 550 ](https://i.imgur.com/OP69rft.png)

- the question is how to change the state - this change is made based off the definition of a derivative:
- ==the gradient of a function indicates the direction in which the function ascends the fastest==
- since we are trying to ==minimise== the loss function, we want to change the state in the ==opposite direction== to the gradient:
![ | 450](https://i.imgur.com/cUgoxo0.png)
![ | 200](https://i.imgur.com/SUN5rbs.png)
- $\eta$ essentially decides how much change you would like to apply per update - a high learning rate will make big changes, which can result in unstable training behaviour. Meanwhile, a low learning rate can result in a slower algorithm and potentially suboptimal solutions

### gradient descent example with learning rates
![](https://i.imgur.com/jhvDKif.png)

### gradient descent for least squares
- we take the loss function that we obtained within [[linear least squares]], and then derive the gradient, and plug it into the updating function as shown above 
![](https://i.imgur.com/kh6upkk.png)
