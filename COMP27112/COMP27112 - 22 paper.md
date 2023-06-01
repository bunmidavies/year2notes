![](https://i.imgur.com/7DtPq2Q.png)
in the simple shading algorithm, the illumination model is applied to a singular vertex on a surface, and the a singular surface normal is taken from a surface in order to calculate the resulting intensities, thus the resulting colour. This colour is then applied to the entire surface - the obvious visual shortcoming of this algorithm will be that every surface has all its pixels set to one colour, taking away from realism and potentially causing very distinct changes in colour from surface to surface
gouraud shading addresses this by estimating the average normal for a vertex through calculating the surface normals for all surfaces which share the vector in question - at this point the illumination model is applied, and the pixel colours for each vertex can be determined. The big difference between gouraud shading and simple shading is that gouraud now interpolates the average pixel colour between vertices, and along scanlines will interpolate the average colour for each pixel. This gives for more detailed shading on a surface rather than one colour, but can also result in visual problems like the mach-band effect, as well as specular reflection potentially being averaged out on a surface

![](https://i.imgur.com/twEpEme.png)
Gouraud shading allows for more detailed shading on a surface rather through interpolating pixel colours along a scanline/between vertices, but can also result in visual problems like the mach-band effect - where differences in intensity between surfaces are perceived to be more than they actually are - as well as specular reflection potentially being averaged out on a surface. Phong shading is able to address these shortcomings through avoiding interpolating pixel colours, but interpolating the surface normals between vectors and along a scanline instead. This means for each pixel along a scanline, the illumination equation must be applied separately to calculate the resulting colour. This comes at the cost of many more calculations being required, but the mach band effect does not apply to phong shading, and specular reflections wont get averaged out

![](https://i.imgur.com/ZHGQhBR.png)
going from left to right
- the first matrix is a scale in the y axis by a factor of two
- the second matrix is the translation $(1,1,0)$
- the third matrix is a rotation 30 degrees anticlockwise around the z axis

![](https://i.imgur.com/hABYuOg.png)
the rotation happens first, then the translation, then the scale ?

![](https://i.imgur.com/3QyOnWI.png)
$b_vNv$ and $b_uNu$ respectively are the additional components which are added onto the regular surface normal $N$, in order to alter the overall lighting of the surface when the illumination model is applied, to give the appearance that the surface is bumpy without actually modifying the geometry
$b_u$ is the horizontal gradient which is calculated from a bump map, using a height map, and $b_v$ is the vertical component
it can be better to compute these values in advance if possible, since then they can just be added to the surface normal and have the illumination model applied as normal
precomputed bumpmaps may be useful for stationary objects which are supposed to look rough - live bumpmaps may be more suitable when a surface is dynamic in some way, or it is possible for the surface to look more deformed overtime, thus the surface normals would have to be additionally altered

![](https://i.imgur.com/VnmZNNX.png)
- ground resolution measures the number of pixels which may be mapped to some real area in metres, thus for instance 5metres$^2$/pixel could be a possible spatial resolution
- angular resolution involves field of view, thus can be expressed for instance as 0.2degrees/pixel
- intensity resolution is used to describe colour depth and the number of bits which are used to represent colours in an image - the most common type may be 8-bit greyscale/24 bit colour depth
typically, a higher resolution may result in more accurate images, for instance nyquists theorem suggests that in order for a periodic signal to be fully replicated the sampling interval must be at least half the period - this can apply to resolution through object detection (i.e. an object can be detected if at least 2 samples i.e. pixels capture its longest dimension). a higher resolution in the context of ground resolution would mean less metres squared per pixel

![](https://i.imgur.com/ILhcLNw.png)
1. iterate through from left to right, top to bottom:
	- ignore background pixels
	- if current pixel is an object pixel and there are no adjacent object pixels which are labelled, give the current pixel a new label
	- if current pixel is an object pixel and there is an adjacent object pixel which is labelled, give the current pixel that same label
	- if the current pixel is an object pixel and there are multiple adjacent object pixels which are differently labelled, give the current pixel one of those labels (not important which) and note the equivalence
2. perform a 2nd pass, iterating in the same manner
	- if current pixel is object pixel where equivalence was noted, give all pixels with the equivalent labels 1, singular label - in short, just relabel all equivalent labels

![](https://i.imgur.com/LxevIll.png)
 assuming this is greyscale
 create empty array of size 256 to store 0-255 greyscale values
 iterate through image pixels, increment the according index in the histogram (the greyscale value of the pixel)
 display the histogram with the greyscale value on the x, and the frequency of each value on the y
 this histogram can then be used to calculate a suitable threshold to identify foreground from background

![](https://i.imgur.com/RnbYuMd.png)
clipping is the process of limiting/restricting values which a pixel can take - when performing certain operations on pixel values, if clipping is not used, this may result in overflow/underflow within values, which cant be displayed or can cause erroneous image calculations further down the line

![](https://i.imgur.com/IE3GYqL.png)
convolution with a kernel involves the centre of the 3x3 kernel being placed on a pixel within an image, each value of the kernel being multiplied by the centre pixel value being added to a sum, and the resulting sum being stored in a new image - this operation cannot happen in place, since when moving onto the next pixel, the previous pixel should not have been altered
3x3 kernel to perform blurring
![](https://i.imgur.com/gin9w0C.png)
kernel to find horizontal edges (prewitt)
![](https://i.imgur.com/z2qCvbN.png)

![](https://i.imgur.com/yKMjYl2.png)
using cartesian coordinates
1. create accumulator array, with c on y axis, m on x axis, and establish hough threshold
2. rearrange y = mx + c to get c = -xm + y
3. for each pixel in image, take (x,y) to form c equation
4. increment according values in accumulator array by incrementing m
5. once all pixels have been plotted, take corresponding (m,c) values where accumulator array value exceeds threshold
6. plug (m,c) into y = mx+c to get according line made up of pixels
![](https://i.imgur.com/Zeru3AB.png)
![](https://i.imgur.com/DxVY6Ey.png)
