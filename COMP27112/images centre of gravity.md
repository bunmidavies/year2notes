[[COMP27112]]

### definition
- the centre of gravity is useful within image processing for multiple purposes, and uses the notion of moments from physics to calculate an x and y moment
$$M_{\alpha\beta} = \sum_{\text{image}}x^\alpha y^\beta I(x,y)$$
- for binary images, $I(x,y) \in \{0,1\}$
- by letting $\alpha,\beta = (1,0)$ and vice versa, one can obtain the sum of x/y values for a regions pixels - setting these to 0 just sums over all pixels, since $x^0/y^0 = 1$
- therefore, $M_{00}$ returns the number of pixels in a binary image 
- the following gives a regions centre of gravity as $(x,y)$
$$(\frac{M_{10}}{M_{00}},\frac{M_{01}}{M_{00}})$$

![](https://i.imgur.com/JGscMKY.png)
*example coloured calculation included for clarity*


### central moments of area
- the original moments of area equation can be altered to give a version for the moment from any point of an image
$$M_{\alpha\beta} = \sum_{\text{image}}(x-\bar{x})^\alpha(y-\bar{y})^\beta I(x,y)$$
- $(\bar{x},\bar{y})$ is the centre of gravity in the image - since everything is relative to the centre of gravity in the image, the region could also be moved, and as long as the centre of gravity updates, then the central moment wouldn't change
- the orientation of a region is given by $\theta = \frac{1}{2}\tan^{-1}(\frac{2M_{11}}{M_{20} - M_{02}})$ 

### order of moments
- moments can be defined for all values of $\alpha$ and $\beta$ - but only a certain number are useful
- lower order moments can be used to make higher order moments invariant to:
	- position
	- orientation
	- size of region