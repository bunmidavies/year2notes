[[COMP27112]]

modelling rough surfaces follows on from [[texture mapping]], involving giving the appearance of a rough surface on an object

==the actual model is not changed in bump mapping==

### bump mapping
![](https://i.imgur.com/5mEblHl.png)
- the surface colour is not altered like with textures, but instead the surface ==normals== are altered
- note that ==the surface isnt actually changed, but gives the appearance that its changed==
![](https://i.imgur.com/YmWuqpw.png)

### altering the surface normal
![](https://i.imgur.com/bhl95jW.png)
- 2 vectors at right angles to the surface normal need to be created, then multiplied by a scalar in order to obtain $N'$, the new surface normal
- texel colours from a texture can be used to encode bumpiness

### encoding bumpiness from textures
- for each texel, compute its x and y ==brightness gradients== and use them as $b_u$ and $b_v$
![](https://i.imgur.com/geQGqOE.png)
