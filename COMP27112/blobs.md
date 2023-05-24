[[COMP27112]]

### definition
- a blob is a ==set of pixels== that:
	- share some property (for instance, have similar intensities)
	- are connected
- with previous techniques like [[thresholding]], grouping blobs together has been simple - pixels are considered to be from the same blob if they have the same value
- there are other ways to group pixels to make up a blob, including statistical tests - therefore, a classifier could be built to figure out which blobs exist