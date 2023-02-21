[[COMP27112]]

parallel projections can be split into ==orthographic== and ==oblique== projections

- 'rays of light' that are parallel to eachother will project onto the projection screen and still be parallel
![](https://i.imgur.com/wSkWyQc.png)
- particular points of the building end up on the projection plane, and an undistorted view of how the building looks from the front is returned - this is ==orthographic== (this means the projection is perpendicular to the projection plane, and the plane is parallel to one of the planes in the world coordinate system)

### orthographic projections
- as said above, the projection plane must be parallel to one of the planes in the world coordinate system - in the example below, the projection plane is at z=0, and parallel to the xy plane
- the projector (i.e. what is being projected) must now be orthogonal to the projection plane, i.e. perpendicular to the XY plane thus parallel to the Z-axis
![](https://i.imgur.com/E8qgXSa.png)
- this projection of the blue point to red point can be defined with a matrix. The transformation is the same as ==scaling== by (1,1,0) - this matrix is ==singular== as it has no inverse ([[essential vector geometry]])
![](https://i.imgur.com/LJsU2Ew.png)
- because the matrix is singular and has no inverse, this means that once the point has been projected, you cannot regain its z-value i.e. where it once stood in real world coordinates

- ==axonometric== projection is another type of orthographic projection, but differs to the top front and side projections where the projection plane is perpendicular to a certain axis
- there are 3 main types of axonometric projection:
	1. isometric - projection plane is symmetrical to (X,Y,Z) - this means from a viewpoint where the ==angle between all the axes is 45== 
	2. dimetric - projection plane is symmetrical to 2 of (X,Y,Z) - same definition of symmetrical is used here
	3. trimetric - projection plane is placed arbitrarily

### oblique projections
- the most general case of all parallel projections - there are no constraints on the projection plane being perpendicular to the projector
- this means that the projection plane can have any angle with the projector points, which can result in situations as shown below
![](https://i.imgur.com/9FgVQsG.png)
