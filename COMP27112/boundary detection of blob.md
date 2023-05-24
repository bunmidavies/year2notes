[[COMP27112]]

### boundary detection
- given we have an object in an image which we want to find the boundary pixels of, the following steps can be taken
1. scan the image pixels from left to right, top to bottom
2. once the first object pixel is found, we save this as $O_0$ - since up to this point we've been scanning from left to right, we know that the pixel to the left is background, $B_1$
3. starting from $B_0$, scan pixels in a ==clockwise== direction (potentially across all 8 bordering pixels) to find the next object pixel - $O_1$ - the background pixel immediately before $O_1$ is $B_1$
4. this cycle is repeated from $O_1$ and $B_1$ to $O_2$ and $B_2$ etc. 
5. eventually, after reaching $O_0$ - check that the next object pixel found is $O_1$ to ensure the boundary continues off in another direction. If this is the case, the boundary is complete
![](https://i.imgur.com/cynqn9u.png)
![](https://i.imgur.com/7w0y26D.png)
