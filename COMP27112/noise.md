[[COMP27112]]

### definition
- noise can be defined as ==deviation of a value from its expected value==, and can come in a number of forms, including:
	- random changes $x \rightarrow x + n$ (following a random distribution)
	- salt and pepper - pixels are either the complete max or complete min
	- imaging artefacts - streaks and blooms, i.e. things affecting actual capturing equipment
![ | 500](https://i.imgur.com/XdDMbuF.png)

### sources of noise
- there are two main definitions as to where noise actually comes from:
	- anything ==within the imaging system== that causes a change (e.g. electrical interference)
![ | 350](https://i.imgur.com/AaEN1ua.png)
	- anything that ==causes a change== - thus including atmospheric disturbance
![ | 350](https://i.imgur.com/QqtnBta.png)

### noise reduction (smoothing)
- ==smoothing== is the general process of removing noise - convolution is a common method for smoothing ([[applications of convolution]]) - this is known as local smoothing
- =='stacking'== in astronomy is also a common technique, which involves averaging multiple images, and using the idea that $\sum(x+n) = \sum(x) + \sum(n) \approx \sum(x)$ 
- for stacking it should be noted that the earth is moving, so these images need to be aligned if you're trying to focus on a particular object

### more smoothing (adaptive + gaussian)
- ==adaptive smoothing== involves computing a smoothed value as normal, but only using this value if it is ==not too different from the original value== (determined using a threshold, $T$)
![ | 300](https://i.imgur.com/6nhopYY.png)
- ==gaussian smoothing== basically involves creating a filter kernel from the 2D gaussian function - the weights inside the actual matrix are derived from the gaussian distribution
![ | 300](https://i.imgur.com/K0xWkrr.png)
