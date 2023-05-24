[[COMP27112]]

### definition
- chain codes are used to describe the boundary of a region from a starting pixel, using a 'compass' with 8 possible directions
![|450](https://i.imgur.com/WdPUxeV.png)
- chain codes are ==not rotationally invariant== - if the shape is rotated, a different code will be produced - however, starting from any point of the boundary of the shape from the same orientation will result in the same code, just shifted 
- ==each direction can be stored within 3 bits==, so the amount of storage required to represent a boundary is typically much lower than storing the actual pixels themselves

### differential chain codes
- with differential chain codes, the compass directions are interpreted from the perspective of the red marker, rather than whoever is viewing it - for instance, looking at the compass the direction '2' appears as right, while this would be forward/up for the red marker, as that is the direction its pointing
![|450](https://i.imgur.com/8YQPoif.png)
- differential codes are now ==rotationally invariant== - as well as this, chain codes are cyclic, meaning by comparing codes you can compare shapes, just by cyclically rotating the codes
- the differential chain code given an ordinary chain code can be calculated:
$$d_n = c_n - c_{n-1} \text{(mod 8)}, n=0...$$
- taking the start direction as the first direction of the compass i.e. right = 0, then $c_{-1}=0$
