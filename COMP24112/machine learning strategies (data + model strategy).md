[[COMP24112]]

the typical ML strategy is the ==Data + Model== strategy:

Data: X $\rightarrow$ Model: $f(\theta,X)$

Data can also be described as ==experience==, $E$

the function $f$, is controlled by its parameters $\theta$, and provides solutions to a task $T$ - this is the actual ==model== itself. We can call it the 'prediction function', 'target function', or as said just a model

the actual task within machine learning is to find the best parameters, resulting in the best function, i.e. the ==best performance P of task T==

the ==Objective Function==, $O(\theta)$ computes the performance of task T - therefore, the ==optimisation== ([[ML optimisation]]) of this objective function is whats known as the learning/training process in machine learning

after learning/training is complete for some model, the final product is the ==trained model==:
$$f(\theta(D_{tr}),x)$$
the process of using the trained model on unseen data is ==inference==
$$\textrm{answer} = f(\theta(D_{tr},x_{query}))$$
