[[COMP27112]]

openGL maintains two transformation matrices internally:
- ==modelview matrix== - used for transforming the geometry you draw
- ==projection matrix== - used for controlling the way the camera image is projected onto the screen

therefore:
$$P_{drawn} = \textrm{ProjectionMatrix} \times \textrm{ModelviewMatrix} \times P_{specified}$$