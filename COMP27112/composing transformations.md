[[COMP27112]]

matrices representing different [[geometrical transformations]] can be multiplied together to create one ==composite transformaiton==:
$$T_C = T_2 \cdot T_1$$
therefore
$$P'' = T_2 \cdot T_1 \cdot P$$
implies
$$P'' = T_C \cdot P$$

==matrix multiplication is non-commutative - order matters==
$$M_1 \cdot M_2 \neq M_2 \cdot M_1$$
![](https://i.imgur.com/3DV5gpY.png)


in the multiplication, the very right matrix is the ==first transformation== which will be applied - therefore undoing the effects of these transformations needs to be done in reverse order
![](https://i.imgur.com/XcMcpUj.png)


the product of two ==inverse matrices== is the ==identity matrix==, $I$
some matrices don't have an inverse, these are known as ==non-invertible==