[[COMP27112]]

- a camera can only see objects which are within its field of view, which depends on the lens it is using - as well as this, certain objects which are too far away will not be visible, so in computer graphics a range is also considered with the fov
- the field of view of a camera can be defined with a 3D ==view volume== - only the parts of 3D objects which lie within the view volume are displayed
- all objects are ==clipped== against the view volume
![](https://i.imgur.com/xJcxRyt.png)
- the shape of this volume will actually depend on the type of projection you use (that is, whether you use [[parallel projection]] or [[perspective projection]])

### view volume for parallel projection
- for parallel orthographic projection, the view volume is a ==cuboid==
- the cuboid has a near plane (the projection plane - any object before this wont be rendered) and a far plane (any object past this won't be rendered). Both of these planes are orthogonal to the camera's $\hat{F}$ axis (reminder of U, F and S axis within [[camera coordinate system]])
- in three.js its simple to set up an orthographic projection:
```javascript
const camera = new THREE.OrthographicCamera(left, right, top bottom, near far);
scene.add(camera);
```
- left, right, top, bottom are coordinates to define the near/far plane dimensions, while near and far define the distance between the two planes and the camera
![](https://i.imgur.com/waxV1CB.png)


### view volume for perspective projection
- rather than a cuboid, the view volume here is a ==frustum== (truncated pyramid)
- the frustum also has a near plane and far plane, which are both orthogonal to the $\hat{F}$ axis
- three.js also makes it pretty easy to define a perspective projection
```javascript
const camera = new THREE.PerspectiveCamera(FOV, aspect, near, far);
scene.add(camera);
```
![](https://i.imgur.com/xYNNqbc.png)
- near and far is the same as defined in the orthogonal projection above, and FOV is clear to see - `aspect` defines the aspect ratio, which just defines the ratio between the width and height of the frustum