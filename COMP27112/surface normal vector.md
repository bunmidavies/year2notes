[[COMP27112]]

- The surface normal is a vector which is ==perpendicular== to the plane of a polygon
- The surface normal is used to distinguish a 'front' and 'back' of a polygon
- It is also used to describe the ==orientation== of a polygon in a 3D space
- most graphics libraries will usually find the surface normal for you, so you dont really have to calculate it

- the ==cross product== of two vectors returns a vector which is perpendicular to them ([[essential vector geometry]])

### finding the surface normal
1. choose a pair of sequential edges $E_1$ and $E_2$ and compute their vectors
2. invert the direction of the first so they now emanate from their shared vertex (you invert the direction by making the vertex ==negative==)
3. their cross product gives the surface normal $N$
$$N = E_2 \times -E_1$$
4. $N$ is then normalized in order to make its length 1
![](https://i.imgur.com/c3X6UyS.png)
