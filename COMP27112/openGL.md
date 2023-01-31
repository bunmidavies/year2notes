[[COMP27112]]

openGL was first released in 1992, and has origins from GL (by Silicon Graphics Inc), and is the open standard for ==portable== and ==language independent== graphics programming today

==openGL only generates pixels, it doesn't handle interaction devices==
the ==GLUT== library is used in COMP27112 to handle interactions

openGL's main features include:
- 3D graphics (points, lines, polygons)
- coordinate transformations
- a camera for viewing
- hidden surface removal
- lighting and shading
- texturing
- pixel operations

libraries like ==GLU== act as wrappers for openGL to draw more complex objects made of openGL graphics, as well as other utility functions

openGL functionality has evolved over time, originally having a fixed pipeline in v1/v2, then from v3+ extensible functionality/programmable pipelines were introduced

DirectX, owned by Microsoft, is a similar system which achieves the same thing. The main difference is that OpenGL is an open standard, owned by the ==Khronos Group== (a group of a bunch of big computer companies)

openGL is a library, so the openGL API sits between the application program and the hardware / input devices. Therefore the ==hardware is abstracted== when using the openGL API

![[Pasted image 20230131220201.png]]

Conceptually, all graphics systems will work the same - graphics software will typically run on a GPU. The software will output a set of pixels, which is written into ==frambuffer memory==, which maps to a screen memory

Graphics systems involve a ==graphics pipeline==, which will perform a set of algorithms / operations to some 3D vertices in order to get the pixels to be displayed

as mentioned above, there are two main types of pipeline:
- [[fixed graphics pipeline]] - as part of openGL v1, v2
- [[programmable graphics pipeline]] - openGL v3+

their pros and cons are covered in [[fixed vs programmable pipeline]]