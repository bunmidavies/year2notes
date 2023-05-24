[[COMP27112]]

### definition
- the aim of region labelling is to identify groups of contiguous pixels - i.e. to identify and label separate [[blobs]]
- one of the main problems with finding regions is the fact that objects can be incorrectly split up, or joined together - this is essentially an issue with the image thresholding
- thresholding issues can be fixed with different [[binary morphology]] techniques (e.g. dilation, erosion)

### connected component analysis algorithm
- the algorithm works in ==2 passes== - both algorithms work from left to right, top to bottom (in terms of pixels in the image)
- neighbours of the pixel can be determined using 4-connectivity or 8-connectivity ([[connectivity]])
##### 1st pass
- if zero neighbours have a label, the pixel receives the next free label
- if one or more neighbours have the same label, the pixel receives that label
- if two or more neighbours have different labels, the pixel receives one label, and the equivalence is recorded
##### 2nd pass
- all equivalent labels get renamed
![|500](https://i.imgur.com/jJgcvXR.png)
