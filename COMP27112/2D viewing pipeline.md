[[COMP27112]]

- the first step when trying to view some part of the world within an actual display is to define a 'window' within the world, and a 'viewport' in the actual display screen, both in terms of their own coordinates
![[Pasted image 20230214221255.png]]
- Mview is the ==viewing transformation==, and transforms the window into the viewport
- Mview is found in 3 steps:
	1. translate by (-x0, -y0) to place the window at the origin
	2. scale the window to be the same shape as the viewport
	3. translate to the window position
- Mview is simply $M_3 \times M_2 \times M_1$ (remember that you multiply in the opposite order of which way you actually want the transformations to take place, so M1 will be happening first)

so to convert any point in the world to the viewport point, you just multiply the world point by Mview