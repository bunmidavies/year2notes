[[COMP24112]]

the confidence interval is used to answer the question of *how good an estimate of the true error is provided by the sample error?*

Classification example
![](https://i.imgur.com/uEjq6OX.png)


this can be drawn as:
![](https://i.imgur.com/6YGqt24.png)

where the cross is the true error, and $[error_s - a, error_s + a]$ represents the interval this true error can lie within

- The goal is to have a small $a$ for a more precise estimate, and a higher $p$ for higher confidence
- $a$ itself can be calculated

$$a = z_p\sqrt{\frac{error_s(1-error_s)}{n}}$$
where as usual $error_s$ is the sample error, and $z_p$ is a constant based on the confidence level $p$
![](https://i.imgur.com/ZL0YTBj.png)


==given > 30 samples with the sample error not being too close to 0 or 1, the error interval works well==

z-tests can also be used for calculating confidence intervals between two models: [[z-tests for hypotheses]]
