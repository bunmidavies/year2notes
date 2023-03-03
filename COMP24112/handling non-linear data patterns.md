[[COMP24112]]

using linear models, we were able to create the ==separation plane== which allowed for binary classification - but this type of model is not applicable when our data follows a pattern in which a singular straight line does not separate the data accurately:
![](https://i.imgur.com/0W1siFv.png)


- the trick to handling this data is by ==mapping each data point to a new feature space==
- in this new feature space, we aim for the patterns to be linearly separable
- i.e. we map the data points in some way such that we go from the bottom right graph to the top left graph (from above)
![](https://i.imgur.com/CB9MqLU.png)

- we call this mapping function $\phi$, and a mapping function exists for each input:
![](https://i.imgur.com/YTBFniW.png)

- there are different approaches to creating these mapping functions

### basis functions

basis functions are created by ==directly formulating many nonlinear functions== ${\phi_i(x)}^D_{i=1}$
- these basis functions can be viewed as feature extractors
- there are many possible choices of basis functions:
	- Gaussian basis functions
	 ![](https://i.imgur.com/KFRXMzt.png)
	 - Polynomial basis functions

### kernel method

the kernel method differs to basis functions in that it doesn't directly define a mapping function $\phi(x)$, but defines the ==inner product function== in the new space using a kernel function

![](https://i.imgur.com/3FByWCh.png)
![](https://i.imgur.com/iYT4ClP.png)
![](https://i.imgur.com/iYT4ClP.png)


- the kernel method can be applied with a linear function in the new feature space induced by the kernel
![](https://i.imgur.com/Ztj18o2.png)
- the final linear function you get is just a linear combination of the kernel function (which is the 'inner product' of other functions) - which ends up looking very similar to the linear basis function
![](https://i.imgur.com/kzBAa0B.png)
