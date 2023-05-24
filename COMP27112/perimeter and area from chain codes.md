[[COMP27112]]

### perimeter
- the perimeter can only be calculated from ==ordinary chain codes== ([[chain codes]])
- odd chain codes are the hypotenuse of a right angle triangle with sides equal to 1 (since you move from pixel to pixel), therefore:
	- ==odd chain code length== = $\sqrt{2}$
	- ==even chain code length== = $1$
- thus:
$$\text{Perimeter} = E + \sqrt{2}D$$

### area - shoelace algorithm (polygons)
- the shoelace algorithm from the start takes $(x_1 * y_2) - (y_1 * x_2)$, and repeating this going down a table, taking the sum as you go along - its generally defined for polygons with vertices rather than images with pixels
- the final area is half of the absolute of the sum, i.e.
$$\text{area} = \frac{1}{2}|\sum (D)|$$
![|550](https://i.imgur.com/OISxIrC.png)

### area - shoelace algorithm (chain codes)
- by calculating the corresponding x/y values of a pixel from chain code values, the area of a blob/region can be calculated
![](https://i.imgur.com/zpHnGtO.png)
- this is an ==estimate== since the area is based off the polygon within the object - adding on the areas of a bordering pixel outside the polygon on top of the area calculated would result in the correct area
- this discrepancy between the estimate and real area becomes less noticeable on larger areas