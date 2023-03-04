[[COMP27112]]

- instead of interpolating ==colours== like [[gouraud shading (intensity shading)]], Phong shading involves interpolating ==normal vectors==
- we interpolate the normal vector along the scanline, and compute the illumination model for every pixel

### phong interpolation (in words)
- for each scanline
	- compute average normal for left from $N_A$ and $N_C$
	- compute average normal for right from $N_B$ and $N_C$
	- average between left and right along the scanline, computing the colour using the illumination model

the same optimisation applied to [[gouraud shading (intensity shading)]] by calculating an increment rather than every single colour can also be applied