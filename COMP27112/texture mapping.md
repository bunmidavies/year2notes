[[COMP27112]]

there are two main ways of performing texture mapping:
- image-based: the image is just wrapped onto a surface
- procedural: a texture pattern is computed as you render an object, and the pixel colour is therefore calculated while rendering ==(not as common or covered in comp27112)==

- a texture can simply be thought as an image, and each pixel in that image is called a ==texel==
- texels and pixel colours are combined along a scanline when performing scan conversion to render a polygon
![](https://i.imgur.com/mtFO3Je.png)

the main problems with texture mapping are as follows:
- ==seams==
- ==resolution mismatches== - there are two main cases for this:
	1. pixel resolution > texture resolution (pixels are smaller than texels): this can be solved by mapping multiple pixels to the same texel. The two main approaches for this is ==no filter== (simply select texels which pixels match to) and ==bilinear interpolation== (averaging the colour using neighbours from a fractional position in a texel)
	2. pixel resolution < texture resolution (pixels are bigger than texels): a main solution to this is ==mipmap filtering== (many things in a small place). it uses the idea that the further away from the viewpoint, the less detail is needed

1st case
![](https://i.imgur.com/CGBNzg8.png)

2nd case
![](https://i.imgur.com/rJ7wsBv.png)
