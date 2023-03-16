[[COMP27112]]

in the camera coordinate system, we have the following axes: $\hat{U},\hat{F},\hat{S}$ - there are fixed to the camera, and are at an orientation which is defined by $C$ (the vector which the camera is facing towards). This means the origin of the camera coordinate system is $E$ (where the camera is located)

### calculating $\hat{F}$
- $F = E - C$, and $F$ is normalized in order to achieve $\hat{F}$

### calculating $\hat{U}$ and $\hat{S}$
- one could give the user the ability to define the 'up' direction (i.e. the users version of $\hat{U}$), called $V$, and the assumption that is made is that $V$ ==must be orthogonal== to $F$
- however, this is not a reliable assumption to make, and if a user was to define $V$ such that it is not orthogonal to $F$ then the whole derivation of the camera coordinate system would not work
- the solution to this is to just use the user defined $V$, and calculate an orthogonal vector based off $V$ and $F$ - this will be called $\hat{S}$
$$\hat{S} = \textrm{normalize} (\hat{F} \times \hat{V})$$
*(orthogonal vector is calculated using the cross product of the two vectors - [[essential vector geometry]])*
- now, $\hat{U}$ can be calculated by simply taking the normalised cross product of $\hat{S} \times \hat{F}$
- this now results in a camera coordinate system which ==makes no assumptions==, and is guaranteed to be correct

### viewing transformation
- there is a transformation $T_c$ which maps the $X, Y, Z$ coordinates of some object in the world into the camera coordinate system
- the ==inverse of Tc is what we actually want== - since this would translate and rotate the camera system into the XYZ system, it can be applied to objects in the world so that the camera views everything from $(0,0,0)$
![](https://i.imgur.com/Q6is0TS.png)
- this transformation is made up of a few steps, with the camera being used as a reference below:
	1. translate the camera to (0,0,0), i.e.e a translation by $-E$
	2. rotate the camera axes to be coincident with world axes
	   ![](https://i.imgur.com/gPtDBO4.png)
	   3. the overall transformation is just $T_2 \times T_1$