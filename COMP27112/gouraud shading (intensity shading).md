[[COMP27112]]

- Gouraud shading uses ==interpolation== to smooth out the discontinuities between polygons
- this involves essentially estimating the surface normals of polygons, then interpolate a surface normal for vertices between polygons
![](https://i.imgur.com/2r1XgOD.png)

### gouraud algorithm (in words)
- compute average vertex at normals $A$, $B$ and $C$
- compute pixel colours $C_A$,$C_B$,$C_C$
- for each scanline:
	- avg colour $C_{right}$ from $C_B$ and $C_C$
	- average between $C_{left}$ and $C_{right}$ along the scanline
![](https://i.imgur.com/sAKzqtv.png)

![](https://i.imgur.com/eaB7CSU.png)

### implementing Gouraud
- the computation needs to be optimised as much as possible
- instead of calculating each colour from scratch along a scanline, an increment can be calculated, then just applied along the scanline

### problems with Gouraud
- specular highlights may be distorted or averaged away altogether (since Gouraud shading averages between ==vertex== colours)
- as well as this, ==mach banding== ([[flat shading (constant shading)]]) may still be visible
- the solution to this is to ==tag specific edges== to 