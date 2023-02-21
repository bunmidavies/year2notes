[[COMP27112]]

we normally want to clip against the viewport when performing the [[2D viewing pipeline]] - this means removing the parts of the world which are outside the window, when going from world window to viewport

there exist standard algorithms for clipping lines and polygons

- in projection, clipping takes place inside the cube which is produced by projection normalization
- there are efficient algorithms for clipping in 2D and 3D
![](https://i.imgur.com/WhgJw0m.png)
