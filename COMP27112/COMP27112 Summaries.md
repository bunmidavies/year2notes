#### Lecture 1 - Course overview
#### Lecture 2 - OpenGL overview
#### Lecture 3 - Matrix transformations
#### Lecture 4 - Shaders
#### Lecture 5 - Polygons/scanning
#### Lecture 6 - Viewing
vid 1
- a 3d object has to be projected from 3d to 2d in our retinas, on cameras, displays etc.
- camera analogy: $\hat{U},\hat{F},\hat{S}$, $E$ is the centre of the camera, $C$ is where the camera points
- computer graphics viewing steps - modelview matrix ($C = V * M$), projection transformation, viewing transformation
- 3d viewing pipeline is the same as computer graphics general pipeline, but with clipping + perspective division. Output -> 2D pixel
- default view - z=0 plane gets mapped to display screen, and scan-conversion + z-buffer operations occur after
- the same view from a camera at some location/orientation can be obtained by transforming the object rather than the camera
- ==there is no actual camera in CG, just transformations== - duality of modelling and viewing
vid 2
- $\hat{F} =$ normalisation of $E - C$
- $\hat{V}$ = 'up' direction, ==assumed to be orthogonal==
- $\hat{S} = \text{normalise}(\hat{F} \times \hat{V})$, $\hat{U} = \text{normalise}(\hat{S} \times \hat{F})$, and $\hat{V}$ is forgotten
- $T_c$ maps XYZ -> $\hat{S}\hat{U}\hat{F}$ - the inverse is required to take objects from camera view ($T_c^{-1}$):
	- T1 = translate by $-E$
	- T2 = rotate camera axes to be coincident with world axes, $\hat{F}$ aligned with $-Z$ (antiparallel)
	- thus $T_c^{-1}$ = T2 * T1
vid 3
- use `camera.lookAt(x,y,z)` in three.js to compute transformations for the camera
- ==viewing transformation== - specifying the world coordinates (X,Y) to screen coordinates (U,V):
	- translate window to origin
	- scale window to viewport
	- translate to viewport origin
- this is $M_\text{view}$
- $P_\text{screen} = M_\text{view} * P_\text{world}$ 
- clipping = removing anything outside the viewport

#### Lecture 7 - 3D Projection
vid 1
- 2 main types of planar projection = ==parallel== (orthographic, oblique), ==perspective== (1 point, 2 point, 3 point)
- ==parallel projection - the projectors from an object are parallel to eachother==
- projectors are essentially just rays of light from some object
- orthographic projection = projectors are perpendicular to projection plane, plane is parallel to one of the planes in world coordinate system
- transforming 3D points to 2D projection plane matrix transformation
- axonometric is a type of orthographic projection
	- isometric = projection plane is symmetrical to (X,Y,Z)
	- dimetric = projection plane is symmetrical to 2 of (X,Y,Z)
	- trimetric = projection plane is placed arbitrarily 
- oblique projection - projectors don't have to be perpendicular to projection plane - introduces a lot of distortion
vid 2
- ==perspective projection has a centre of projection i.e. eye point - therefore projectors converge==
- n-point perspective corresponds to how many vanishing points there are
- simple transformation matrix for 1 point perspective
- transformation matrix for 3 point perspective
vid 3
- ==after specifying the position/orientation of the camera (projection transform) - the field of view of the camera must be defined with a 3D **view volume**==
- parallel projection = cuboid projection volume - near plane + far plane
- perspective projection = frustum projection volume - near plane + far plane
- since $z_p$ = d for any projected point, this is unhelpful since we want to keep z depth info for hidden surface removal - if you have two points on the same projector with different z values, how can you tell which one is the one that is to actually be displayed?
- projection normalisation for perspective projection:
	- transformation PN distorts frustum F into a cube
	- perform orthographic projection on cube
	- result is the same as original perspective transformation
- clipping exists for 2d windows and 3d view volumes

#### Lecture 8 - Building local illumination model
vid 1
- Rendering essentially takes raw geometry (mesh model) and applies lighting/colouring
- ==Local illumination model== - only considers illumination from direct light sources
- ==Global illumination model== - considers indirect illumination i.e. light bouncing off non-light objects
- the interaction of light and matter is approximated. global > local
- ==diffuse reflection== - absorption and uniform reradiation, giving objects its colour
- ==specular reflection== - reflection at the air/surface interface
- diffuse = rough, perfect specular = smooth, single ray reflected, imperfect specular = multiple reflections
vid 2
- ambient illumination = uniform intensity $I_a$ 
- ambient light reflected $I_\text{ambient} = k_aI_a$ ($k_a$ = ambient reflection coefficient [0-1])
- light from a specific direction (no distance) - Lambert's law + derivation of lamberts law
- point source light diffusely reflected $I_\text{diffuse} = I_pk_d\cos\theta$ ($I_\text{diffuse} = I_pk_d(\hat{N}\cdot\hat{L})$
- $\hat{N}$ = surface normal, $\hat{L}$ = direction of light source
- Light intensity equation + approximated equation
vid 3
- few surfaces are perfectly specular, thus regular rough surface have multiple rays via specular
- what matters is the ==specular reflected light towards the viewer==
- function to model specular reflection depends on:
	- incident angle
	- light wavelength
	- angle between maximum specular reflection and reflection that hits the viewer ($\phi$)
- phongs specular function - $I_\text{specular} = I_p\cos^n\phi$ AKA $I_p(\hat{R}\cdot\hat{V})^n$
- varying effects of $n$ for phongs - higher n = higher intensity but less spatial extent
vid 4
- fresnel equation $F$ gives ratio of incident light that gets reflected:
	- $\phi$ = angle of incidence + reflected angle
	- $\theta$ = angle of transmission (i.e. angle between normal and absorbed ray)
	- $\mu$ = refractive index with respect to air
- $F$ typically replaced with single constant $k_s$
- local illumination model involving ambient reflection + diffuse and specular based on point source distance
![](https://i.imgur.com/UFInDw6.png)

- ==incorporating colour== just involves 3 models for each colour - $I_{pR},I_{pG},I_{pB}$, and using according ambient/diffuse reflectivity coefficients for each colour
- ==multiple lights== = ambient + sum of (diffuse + specular) from each light

#### Lecture 9 - Shading methods
vid 1
- flat (constant) shading - take one vertex from a triangle/polygon, calculate its surface normal, apply illumination model based on that normal and use that colour for all pixels in triangle/polygon
- flat shading = mach banding effect between polygons - human system perceives intensity changes more than they actually are
![](https://i.imgur.com/IFEc68y.png)
vid 2
- ==gouraud shading uses interpolation== to smooth out discontinuities between polygons
- gouraud algorithm (on paper), using interpolated normal vertices between adjacent polygons
![](https://i.imgur.com/VS4KqMI.png)
![](https://i.imgur.com/NNjvQ3e.png)
- implementing gouraud involves optimisations (computing Cright/Cleft incrementally) - specular highlights may 
- phong (aka normal vector) interpolation - instead of averaging colours like gouraud, average normal vectors across scanline
- ==phong = compute normal vector along scanline for every pixel, then apply illumation model==
- phong interpolation algorithm (on paper)

#### Lecture 10 - Surface detail (texture mapping + bump mapping)
- texture mapping is either ==image-based== (use image file) or ==procedural== (compute texture pattern)
- ==we only cover image based texture mapping, not procedural==
- textures are images, where pixels are called texels (using $u$ and $v$ for axes)
- map texels to each vertex of polygon, do scan conversion to interpolate texels to be used in between, then combine colour from illumination model to provide lighting on final pixel
![](https://i.imgur.com/UOE0Ywz.png)
- two main problems:
	- ==seams== - seeing where one rendering of a texture ends, and the next begins
	- ==resolution mismatch== - pixel resolution > texture resolution = pixel size < texel size, and vice versa
- resolution mismatch
	- smaller pixels than texels = no filter or bilinear interpolation filter
	- ==bilinear interpolation== - figure out fractional texel coords, find neighbours, average out texture value
	- smaller texels than pixels (texel res. > pixel res, causing aliasing/missing detail) = mipmap filtering
![](https://i.imgur.com/BH0MxVQ.png)
	- ==mipmap filtering== - generate a set of texture maps, selecting according map based on distance of pixel from viewer. Further away = more blurred
- ==lightmaps== - compute illumination of scene and save rendered surfaces as textures using a global model, so you can apply these textures 
- ==bump mapping== = deforming a flat surface by ==altering the surface normals== rather than colours, and applying the same illumination model to give the look of bumpiness on a surface
- $N' = \hat{N} + (b_U\hat{N}_U + b_v\hat{N}_V)$ (then normalise this final result)
![](https://i.imgur.com/zff1FBK.png)
- texel colours can be used to encode bumpiness, by calculating brightness gradients, based off neighbours
#### Part 1 summary
![|450](https://i.imgur.com/BC8IAFH.png)
- mesh model -> programmable/fixed pipeline -> pixels drawn on a screen


***

***

***


#### Lecture 2 - Colour/eye
vid 2
- with regular diagrams like the CIE colour diagram, ==equal dist. =/= equal perceived colour change==
- with perceptual colour spaces, ==equal dist. == equal perceived colour change==
- IHS (Intensity = weighted average of rgb, Hue = basic color (0-359), Saturation)
- segmentation using HSV (hue, saturation, value) - if you want a specific colour then use Hue and ignore saturation/value, so mask based on hue and set what you want to 255 and the rest to 0
#### Lecture 5 - region processing / convolution
vid 1
- Region processing = functions involving more than one source pixel
- Detecting vertical = $|I(x,y) - I(x,y+1)|$
- Detecting horizontal = $|I(x,y)-I(x,y+1)|$
- combining with city block (just add), euclidean, OR operation
vid 2
- convolution, where $W$ is filter kernel
![](https://i.imgur.com/odO4tX1.png)- ==convolution flips the kerne==l, while correlation doesnt, most image processing software will do correlation but call it convolution - just do $w0*i0$ if in doubt 
- normalisation exists to not get return value which is too large - either perform on result of convolution for a pixel or normalise the mask
- convolution is associative - therefore you can separate kernels to perform less multiplications/additions for efficiency gain
vid 3 - ==convolution applications==
- averaging kernel - box filter. 3x3 all containing $\frac{1}{9}$
- sharpening kernel to enhance discontinuities but amplify noise:
![|100](https://i.imgur.com/P20d2jA.png)
- ==laplacian==: same as sharpening ==but with 4 in centre== - only picks up edges since uniform areas will cancel themselves out
- ==noise is a deviation of a value from its expected value==
- salt and pepper = $x \rightarrow \{\text{max},\text{min}\}$
- noise reduction via smoothing (with/without box filter)
- $\sum(x) + \sum(n) \approx \sum(x)$ since noise is random and has a mean of 0
- adaptive smoothing (taking a smoothed value if it doesnt differ from original value too much)
![|200](https://i.imgur.com/SlTPGgX.png)
- 2d gaussian smoothing using filter
![|400](https://i.imgur.com/xwxOV77.png)
- ==median filter is a type of rank filter==- just takes median from values in each kernel - extremely noisy pixels have less of an effect on kernels by using a median
- other rank filters include: max, min

#### Lecture 6 - Edge detection cont.
vid 1
- ==edge = extended, significant, local change in image intensity==
- calculating gradient of a pixel (in horizontal/vertical direction) - do (next pixel value - current pixel value) to get current pixel gradient
- use gradient in x and y to calculate magnitude/direction of gradient vector
![|200](https://i.imgur.com/W8LEEEZ.png)
- edge normal = pixel gradient vector is perpendicular to edge its on
![|200](https://i.imgur.com/tfiBrjJ.png)
- roberts cross edge detector (not used very much)
![|400](https://i.imgur.com/4IxAwAX.png)
- prewitt operator (left for horizontal, right for vertical)
![|300](https://i.imgur.com/NuQkDBS.png)
- ==prewitt== filter reduces noise as it can be separated into two kernels, one of which is an averaging filter that smooths out rows, and the other is an edge detector
![|300](https://i.imgur.com/5mY6EuY.png)
vid 2
- ==sobel== filter - similar to prewitt, except 2 in the middle instead of 1, giving a weighted avg. rather than regular avg
![|300](https://i.imgur.com/5AIaiuj.png)
- ==canny edge detection main requirements==:
	1. accurately find as many edges in image without false detection
	2. accurately localise edge points on the centre of the edge (works with 3x3, not 2x2)
	3. given edge should only be marked once
- ==canny edge steps==:
	1. pick kernel and apply gaussian smoothing
	2. apply edge detection, and calculate gradient magnitude/direction for each pixel (since these are on edges, these are edge normals)
	3. classify edge normals (gradient vectors of edge pixels) as horizontal, vertical, 45 or -45, into image $\theta$
	4. non maxima suppression - contain thin edges in image by picking pixels from classified image $\theta$ where 2+ neighbouring pixels have same dir but higher mag
	5. use two thresholds $T_L$/$T_H$ on thin edges:
		- below $T_L$ = not an edge
		- between $T_L$ and $T_H$ = weak
		- above $T_H$ = strong
	6. create binary images of strong edges and weak edges (remove strong edges from the weak edges image, since you'd threshold above $T_L$)
	7. final binary image = strong image pixels + set any corresponding neighbour pixels which r set in weak image (connectivity analysis)
- $T_H$ should be 2x/3x higher than $T_L$
vid 3
- laplacian performs second derivative on image - a single kernel can be used, but noise gets highlighted
- ==laplacian of gaussian = gaussian blur -> convolution w/ laplacian==
- ==marr-hildeth = laplacian of gaussian with signed arithmetic, then mark edge pixels if signs differ for any opposing pixels in 3x3? (zero-crossing pixels)==
- difference of gaussian = gaussian blur with 2 sigmas, then subtracting one from the other
- template matching = finding smaller image within bigger image
- template matching is done with cross correlation (convolution equation but flipped, so actually using + symbols)
- normalise the result by dividing by region sum to avoid white area giving largest vals
- in short template matching trash - use feature detection instead

#### Lecture 7
vid 1
- **blob = set of pixels that share some property and are connected**
- blob finding is done with ==connected component analysis/region labelling==
- 4-connectivity/8-connectivity
- issues within connected component analysis can be solved via:
	- dilation
	- erosion
	- opening
	- closing
- connected component analysis steps:
	1. pass 1: work from left to right, top to bottom:
		- if 0 neighbours have a label, pixel receives next free label
		- if 1+ neighbours have same label, pixel receives that label
		- if 2+ neighbours have different labels, pixel receives 1, equivalence is recorded
	2. pass 2: work from left to right, top to bottom:
		- re-label all equivalent labels
vid 2
- moments refamiliarisation
- centre of gravity is just average of all distances from origin
- moments of area formal definition
- 
#### Lecture 8
vid 1
- why use different image formats to store:
	- image data
	- colour palette
	- size versions (icons)
	- different size versions
	- transparency info
	- camera data/location
- portable bit map uses 1 bit per pixel (black/white)
- camera aperture - more aperture = more light
- exposure time - longer time = more light
- bracketing = taking multiple photos at different exposure levels, thus splicing different exposures together
- file formats supporting up to 16-bit colour, allowing HDR = capture high level of detail of both dark and light in the same image
vid 2
- GIF stores coloured pixels in 8 bits by storing colour palette alongside
- you can also store coloured pixels using 8 bits by packing 3 for R, 3 for G, 2 for B
- transparency can be enabled through an alpha channel, which says how 'see-through' a pixel should be 
- run length encoding
- JPEG compression - 8x8 blocks, DCT, $\div$ quantisation, RLE, and reverse for decompression

#### Lecture 9 - Hough transform/lines
vid 1
- hough lines are used to detect actual lines in an image rather than just pixels which resemble a line
- y = mx + c -> c = -xm + y (where x and y = the coords of a point)
- example: (4,2) becomes c = -4m + 2
vid 2
- using polar coordinates for hough lines to solve vertical line issue

#### Lecture 10 - Binary morphology
- structuring element = any shape of pixels
- ==outputs from binary morphology must be drawn onto new image==
- erosion = turning object pixels into background -> makes object smaller than it was
- dilation = turning background pixels into object -> makes object larger than it was
- opening = separating objects, ==erosion -> dilation== - hole sizes remain the same
- closing = joining objects, ==dilation -> erosion== - holes get filled in

# Revise
![](https://i.imgur.com/aqXuD44.png)
