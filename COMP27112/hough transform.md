[[COMP27112]]

### definition
- the hough transform exists to detect ==lines== from what are otherwise just pixels in an image
- this is done through transforming the image into a ==parameter space== - the hough parameter space consists of equations of lines for all points, plotted onto one graph
![](https://i.imgur.com/trzPHVp.png)
- note that the graph has $m$ on the x axis and $c$ on the y axis - this is achieved by rearranging the regular $y = mx + c$ equation to get $c = -xm + y$
- for each point, we sub values of $x$ and $m$ in to get an equation for $c$ which varies with $m$
- if we are looking for lines which consist of at least 3 points, then the point at which these lines cross can be taken into a regular y=mx+c equation
- for instance: with above, 3 lines cross at m - 1, c = 0 - we sub this back into the regular line equation to get $y = -x + 0$. We've now detected a straight line from pixels

### performing hough transformation programmatically
- taking the same idea from above into account, we create a 2D array, using columns for values of $m$ and rows for values of $c$
- entries within this 2D array are incremented by using the hough parameter equations (the equations made from the points) for each point, wherever the line is crossing one of these points
- some rounding can be used where necessary
![](https://i.imgur.com/rryXeih.png)
- this is the same space as in the first example with drawn lines
- once this is done for all points, we can just choose the entries with values above whatever threshold we like - we then take the $c$ and $m$ values and rearrange them like above to get the resulting lines

### hough lines - polar coordinates
- one of the main problems with using ==cartesian== coordinates is that if a line in an image is vertical, then $m = \infty$ 
- the solution to this is to use ==polar coordinates==
- the equation of a line is now represented as $r = x\cos(\theta) + y\sin(\theta)$ 

### hough lines in OpenCV
```cpp
void cv::HoughLines ( 
					InputArray image,
					OutputArray lines,
					double rho
					double theta,
					int threshold	 
)
```

- rho = decides how many rows are in the matrix
- theta = decides how many columns are in the matrix
- threshold = decides how many counts are in the matrix we want to consider as a valid line