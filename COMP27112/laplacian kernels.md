[[COMP27112]]

- following on from [[edge detection]] as the page started to get too big

### laplacian kernels
![ | 350](https://i.imgur.com/Ot4VspI.png)
- laplacian kernels are capable of detecting edges at different scales and operations, by performing the ==second derivative== of the image at each pixel
- this just means its able to calculate the rate of change of the gradient (of image intensity) at that pixel
- we are able to find edges using a ==single laplacian kernel==, compared to where we need to use 2 roberts, prewitt, or sobel filters (for each direction)
- the main downside of the laplacian kernel is that it ==highlights noise==

### laplacian of gaussian / marr-hildreth algorithm
- by blurring an image firstly with a gaussian, noise within the image can be reduced ([[noise + smoothing]]), such that you're performing the convolution with laplacian on a smoother image
- the ==marr-hildreth== algorithm is an extension of this, performing laplacian of gaussian first using ==signed arithmetic==
- in this case, pixels are only identified as edge pixels if there is a differing sign on any of its pairs of neighbours
![ | 500](https://i.imgur.com/1xKaxcA.png)

### difference of gaussians
- the difference of gaussians simply blurs an image with two different values for $\sigma$ (used in the gaussian distribution)
- one of these images are subtracted from the other, and the resulting image is returned