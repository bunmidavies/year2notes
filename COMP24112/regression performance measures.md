[[COMP24112]]

as already covered, [[regression]] takes a very similar form to classification in terms of the sets involved:
- samples : ${x_i,y_i}$
- a feature vector : $x_i \in R_d$ (the ==input==)
- a class label : $y_i \in R^k$ (the ==output==)

there are multiple ways to measure how well a certain regression model performs

### regression error
regression error is simply the difference between the real and predicted output - using this, a number of regression performance metrics can be derived

these regression performance metrics are based off the core idea that you assess the error for each of the $n$ samples, and then for each of the $m$ output values, and average these errors

commonly used regression performance metrics:

![](https://i.imgur.com/G7oBLCy.png)

![](https://i.imgur.com/z360fpg.png)


- $n$ is the number of samples, and $m$ is the number of output values
