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