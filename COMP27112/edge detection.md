[[COMP27112]]

### intro to edges
- edges are important structures in images / image processing for 2 main reasons:
	1. the human visual system contains very specific edge detecting subsystems - the retina performs a low level edge detection operation, but higher level visual processes combine this info to detect different types of edge structure
	2. edges define the ==significant structures== in a scene - i.e. the outline of objects and parts of objects

- an edge can be defined as: ==a significant, local, extended change in image intensity==

### basic edge detection
- using [[region processing]], we can define the intensity of a pixel in our 'edge detected' image as:

$I'(x,y) =$ threshold $(|I(x,y) - I(x,y+1)| + |I(x,y) - I(x+1,y)|, T)$

- this works by combining ==horizontal== and ==vertical== edge detection into a single operation
![](https://i.imgur.com/9BoAm6g.png)


### convolution
- a better way of finding edges is through [[convolution]] - its represented using $\otimes$ or $*$
- a number of different edge detection operators are really just convolution with a specific kernel filter (described within [[convolution]]) - these are described below

### roberts operator
- the roberts operator uses a 2x2 kernel with convolution, computing the differences in adjacent pixels in the $x$ and $y$ directions
![ | 350](https://i.imgur.com/6pkBDic.png)
- its the simplest edge detector kernel, thus has a couple of downsides:
	- ==noise sensitive==
	- ==poor edge localisation== - edges are prone to be missed, and poor edge localisation itself means the detected edges arent aligned with the actual edges in the image

### prewitt operator
- the prewitt operator uses 2 3x3 kernels to approximate the gradient magnitude of an image 
- one kernel is used for vertical direction, while the other is used for horizontal
![ | 350](https://i.imgur.com/hwTOG0j.png)
- the prewitt operator is fast and provides good edge detection as well as robustness to noise, but also has its downsides:
	- ==insensitive to edges in non-cardinal directions== - i.e. diagonal edges or any edges not aligned with the x or y axis arent best detected

### sobel operator
- like the prewitt operator, the sobel operator uses 2 3x3 kernels for edge detection - just with slightly more weighting - giving similar results to prewitt
![ | 350](https://i.imgur.com/FKRia6k.png)
