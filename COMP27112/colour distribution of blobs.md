[[COMP27112]]

### definition
- the colour distribution of a blob is a useful characteristic, since it is independent of both ==area== and ==orientation==
- typically, the ==hue== and ==saturation== components of the blob are recorded

### blob tracking
- tracking how blobs move through some footage (i.e. multiple frames) can be challenging, since some invariant property is required to ensure the same blob from the last frame has been given the same label in the next frame
- ==the problem at hand==: if there are $N$ blobs in frame $t$, and $M$ blobs in frame $t+1$, which subsets of $N$ best match which subsets of $M$?
- ==predictive tracking== is a possible approach, since by predicting the location of a blob from one frame to the next, certain blobs can be compared with invariant properties to ensure they're the same. For each blob, maintain:
	- current location
	- current velocity (based on distance/direction moved from previous location)
	- invariants (e.g. colour)
- with all of these, some window of error/variance should be considered for the recorded values
- also, if a blob with no previous prediction is detected, this can be considered to be a new blob