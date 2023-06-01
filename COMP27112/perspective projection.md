[[COMP27112]]

- in painting, 'perspective' only really started appearing during the [[italian renaissance]] (15th - 16th century) - before then, in things like medieval paintings, more important figures were just painted bigger
- the idea within most paintings which utilise perspective is that ==parallel lines will converge==
![](https://i.imgur.com/769VXyW.png)
- artists around that time also used 'perspective machines' which helped them draw with correct perspective

- in computer graphics, perspective projections are much more common than parallel projections due to their sense of ==realism==
- there are 3 main types of perspective projection: 1-point, 2-point and 3-point
- the points in these different types define how many ==vanishing points== there are in the perspective - this means that in a 1-point perspective, all parallel lines in the real world will converge to a singular point
- and therefore in 2-point, all parallel lines converge to 2 vanishing points, and 3-point perspective will have all parallel lines converging to 3 different vanishing points
![](https://i.imgur.com/UFWwyPO.png)

### computing perspective
- we create a projection plane which is parallel to the XY plane, and has a z coordinate of $d$
- we create the eye point at the origin
- any projector will end up having a z coordinate of $d$ as well, so what is left to calculate are its projected x and y coords, i.e. $x_p$ and $y_p$ 
- we can calculate these by creating similar triangles while in a ==top down view== of the plane and projector
- we create a small triangle, and a big triangle, and can use the ratios of these and rearrange them to find $x_p$ and $y_p$ - the example below shows calculating $x_p$, but for $y_p$ its more or less the same
![](https://i.imgur.com/BdJUOUq.png)
![](https://i.imgur.com/GiTlZpd.png)
![](https://i.imgur.com/vHuH8HT.png)
- we can again describe this transformation using a matrix - the matrix that does this is actually quite simple, because we alter the homogeneous coordinate, but because it needs to be 1 it means we end up dividing $x$, $y$ and $z$ as well in order to give us the correct $x_p$ and $y_p$ values
![](https://i.imgur.com/wC3xJXX.png)
- this returns us $(x,y,z,z/d)$ - we must always have $w$ (i.e. the homogeneous coordinate) $= 1$, therefore, we have to divide all the elements by $w$ ($z/d$) so that $w=1$ and we have the correct format
- this is ==perspective division==
![](https://i.imgur.com/Qo5A2QV.png)
- this matrix can be used to perform a 1-point projection where the projection plane is parallel to the XY plane
- we can also derive the matrices for 2-point and 3-point projections (details omitted in lectures)