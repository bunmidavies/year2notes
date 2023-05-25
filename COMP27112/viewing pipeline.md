[[COMP27112]]

the viewing pipeline turns vertices and polygons in world coordinates into vertices in pixel coordinates - this is done via ==scan conversion==

the main algorithm used to perform scan conversion for a vertex is ==Bresenham's algorithm==. It simply approximates the true geometry of a line by finding the closest pixels possible (remember that ==everything in computer graphics is an approximation==)

### Bresenham's algorithm
- $y = mx + c$ is the vector we want to draw
- as we move horizontally $x$ changes by 1 pixel, so $y_{n+1} = y_n + m$
- $y_{n+1}$ is rounded to the nearest pixel, and the according pixel is coloured in
this algorithm was developed in the 60s and is still used today

```
y = mx + c //vector
for (x = x1; x <= x2, x++)
{
	y += m;
	write_pixel(x, round(y), colour);
}
```

### scan converting a polygon
- as explained above, Bresenham's has been the main algorithm for scan converting vertices for a while. There are many different approaches to scan converting a polygon
- when scan converting any polygon, we scan convert its edges (i.e. individual vertices) first - then the pixels inside the polygon need to be filled in
- the ==sweep-line== algorithm is more commonly used for this, rather than going row by row through all pixels - it uses bresenham's but in the opposite direction. $y$ is incremented so that the difference in $x$ can be observed, and the distance between two vectors can be filled in with pixels

### hidden surface removal
- when viewing the world from a particular viewpoint, there are obviously things which you aren't able to see since they're blocked by other objects
- there are two main ways to figuring out which objects we're actually able to see:
	- working out the geometry in the ==3D world space==, and drawing the result
	- working in the ==2D display space==, and determining whether some other 3D object which is nearer to the eye maps to the same pixels when performing scan conversion
- working in the 2D display space is the standard approach

### Z-buffer
- the z-buffer is a data structure used when performing hidden surface removal. It's used to keep a record of the z-value of each pixel (i.e. the ==depth== of any given pixel)
- for every pixel in the display memory, theres a corresponding entry in the z-buffer
- the algorithm for figuring out what is stored in the z-buffer is as follows:

1. initialise each pixel to desired background colour
2. initialise each z-buffer entry to `MAXDEPTH`
3. for each pixel $P$ generated during scan conversion:
   - if z-coordinate of $P$ < z-buffer[P] then compute colour of $P$, store colour in $P$, and store z-coordinate of $P$ in z-buffer[P]
   - else do nothing

- in the if statement we simply check if the current pixel being coloured will be coloured closer to the eye than the current pixel in the z buffer. If this is the case then we want to 'overwrite' whatever pixel is in the z buffer. If the pixel colour is further away from the eye than the current pixel in the z buffer, then the viewer will never see this, so we wouldn't want to overwrite the z buffer

- ==z-fighting== is an issue where objects look like they're stuck inside eachother / the images bleed into eachother