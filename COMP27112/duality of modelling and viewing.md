[[COMP27112]]

*The duality of modelling and viewing says that we can get the same view by transforming the camera by T, or the object by $T^{-1}$*

the default camera is at $(0,0,0)$, looking down the z-axis ([[camera coordinate system]])

this is simple to do in graphics APIs - `camera.lookAt(x,y,z)` computes all the transformations to be applied to the objects in order for the camera to 'look' at this point

==it is impossible to tell by looking at two images whether the camera has moved or if the model has==

graphics APIs will allow the user to use a camera, as the idea is familiar, but in reality this should be noted:
- ==there is no actual camera in computer graphics. Only transformations==
- we obtain the same view from a 'camera' at a certain location/orientation by transforming the model