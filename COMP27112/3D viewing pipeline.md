[[COMP27112]]

we only usually have 2D displays i.e. flat screens, so a 3D object has to be projected from 3D to 2D
in daily life we actually make 3D to 2D views using a camera, and our eyes ==reconstruct== the supposed 3D view from a 2D projection

### camera analogy to computer graphics

to generate scene views, a camera analogy can be used:
- models are arranged into a desired composition
- position the camera to point at the scene (there are various points associated with the camera) - there are certain ==image axes== to describe the location of where the camera is. The vector $C$ describes where the camera is actually pointing at
- choose a camera lens now that its pointing at the scene
- decide on the size of the final image

this analogy then translates into the computer graphics:

==starting point = 3D vertex==
- set modelling transformation $M$
- set viewing transformation $V$
- set projection transformation $P$
- clip to view volume
- perspective division
- set viewport transformation
==end point = 2D pixel==
in [[openGL]], $M$ and $V$ are combined into a single ==modelview matrix==, $C = V \times M$

### default view

- a point drawn by the user gets projected onto the $z = 0$ plane (i.e. 2D). This projection is orthogonal, meaning the projection of the point drawn by the user is parallel to the z axis and perpendicular to the $z = 0$ plane
- this means for simple polygons ([[polygons + polygon soup + mesh]]), openGL just projects the lines of the polygon onto the $z = 0$ plane
- this $z = 0$ plane gets mapped to the display screen and from there it gets scan converted with the z buffer applied ([[viewing pipeline]])
![[Pasted image 20230214212136.png]]
- you can move the camera around the scene, or you can move the scene around the camera while it stays still