[[COMP27112]]

### intro
- convolution is a mathematical operation, with a variety of applications - [[applications of convolution]]

### process
- the equation for convolution is as follows:
$$I'(x,y) = W \otimes I(x,y) = \sum^a_{s=-a}\sum^b_{t=-b} W(s,t)I(x-s,y-t)$$
- $W$ is called the ==filter kernel== (filter template, filter mask), and is a matrix of values - typically ==odd-sized and square== (so it has a definite centre)
- the equation takes a summation through the elements of $W$, and we assume $W(0,0)$ is the origin of the matrix, i.e. in the centre - hence the $-a$ and $-b$
- ==each kernel weight is multiplied by the underlying pixel value== (which is what the summation does)
- everything gets summed, and the result is placed into the image pixel under the centre of the kernel
- once thats done, the filter kernel simply moves to the next pixel
![](https://i.imgur.com/TxJ0ukj.png)
- convolution can be applied to an image in openCV using `filter2D`

### corner problem
![ | 550](https://i.imgur.com/3vZxKzJ.png)
- there are a number of approaches for dealing with non-existent pixels:
	- zero padding - pad the edges of the image with zeros
	- valid convolution - only perform convolution where possible, resulting in a smaller image
	- circular padding - wraparound the image (i.e. above, the top right of the kernels underlying image pixel is the bottom left pixel)

### convolution vs correlation
- convolution and correlation are similar operations, but correlation slightly differs by flipping the kernel ==diagonally==
- ==most image processing software performs correlation while calling it convolution==

### composite convolution + separating kernels
- convolution is ==associative==, i.e. $A \otimes (B \otimes C) = (A \otimes B) \otimes C$
- kernels can also be separated - this can be useful in order to reduce computational complexity of certain convolutions (i.e. memory requirements). Consider this example:
	-  convolving an $M \times N$ image with a $3 \times 3$ kernel would take $9MN$ multiplications and additions (this is because for each pixel you multiply over all kernel values)
	- convolving an $M \times N$ image with a $1 \times 3$ kernel, then a $3 \times 1$ kernel takes $3MN + 3MN = 6MN$ multiplications + additions
	- because ==convolution is associative==, you get the same result, but with less calculations
- as you get larger kernels, it becomes much more efficient to split them up