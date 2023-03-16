[[COMP27112]]

- point processing involves the idea of applying some transformation to every given pixel in an image, i.e.

For every pixel (x,y) in an image: $I'(x,y)=\mathcal{F}(I(x,y))$

- where $I$ specifies the intensity of a pixel
- example transformations inclue:
	- image negative - $I'(x,y) = 255 - I(x,y)$
	- increase brightness by $k$ - $I'(x,y) = I(x,y) + k$
	- thresholding - $I'(x,y) = 255$ if $I(x,y)\geq T$ else $0$