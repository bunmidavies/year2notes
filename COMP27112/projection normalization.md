[[COMP27112]]

- the main problem with a projection matrix which transforms a 3D point to a 2D point (where $w = 1$) is that we ==lose information regarding an objects z coordinates== - they all get set to $d$ ([[perspective projection]] / [[parallel projection]])
- this is unhelpful because we want to keep the z-depth in order to perform hidden-surface removal ([[viewing pipeline]])
- we define a new transformation which preserves depth information - projection normalization

1. start with a perspective transformation with frustum $F$ and matrix $M$
2. it can be shown that $F$ can be distorted into a cube using transformation matrix $PN$ (based off $M$)
![](https://i.imgur.com/lCURVF8.png)
3. we can then transform our model by $PN$, and take an orthographic projection ([[parallel projection]])

- this produces the same result as performing the original perspective transformation, but now the z depth values are ==preserved==, and we can use them for hidden surface removal
- OpenGL automatically creates $PN$ for us
