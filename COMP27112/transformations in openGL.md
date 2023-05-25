[[COMP27112]]

openGL maintains two transformation matrices internally:
- ==modelview matrix== - used for transforming the geometry you draw
- ==projection matrix== - used for controlling the way the camera image is projected onto the screen

therefore:
$$P_{drawn} = \text{Projection Matrix} \times \text{Modelview Matrix} \times P_{\text{specified}}$$