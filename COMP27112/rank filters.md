[[COMP27112]]

### intro + difference to convolution
- a rank filter can be used in a manner like [[convolution]] does with its kernel filter, but the main difference is what the centre pixel is set to 
- in convolution, the underlying centre pixel for a kernel filter is just a weighted average over all surrounding pixels
- in a rank filter, the output value for the centre pixel is selected based on an ordering of all the surrounding pixels

### types of rank filter
- there are a number of different rank filters, including:
	- median - output pixel is set to median value of sorted surrounding pixels
	- max - output pixel is set to max value pixel in the filter
	- min - output pixel is set to min value pixel in the filter

### benefits of rank filters
- the main benefit of rank filters are that they can suppress noise within an image, for instance:
![ | 450](https://i.imgur.com/sSWChxz.png)
