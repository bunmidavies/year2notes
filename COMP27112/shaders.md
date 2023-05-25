[[COMP27112]]

### definition
As already mentioned in previous weeks, there is a [[fixed graphics pipeline]] and a [[programmable graphics pipeline]]. Shaders are basically just functions which run on a GPU, and a large number of them will typically run in parallel. There are two main types of shader:
- vertex shaders - a shader function is applied to each vertex from some scene
- fragment shader - a shader function is applied to each fragment (pixel)
The vertex shader program (which is the first part of the programmable pipeline) as well as the fragment shader program (second to last) ==must be provided by the user==, and is written in [[GLSL]]

==All shapes are made of vertices== - the vertex shader program receives each of these in turn, does some processing, and then sets a value for where the vertex will appear onscreen (gl_position, a `vec4`). When any material is created in three.js, it will create shaders which you can modify (meaning if a shader is omitted, it is automatically created anyways)

The ==fragment shader== determines what colours are given to pixels, by setting a value for gl_FragColor (another `vec4`), and represents the final fragment colour

In between the vertexShader and fragmentShader processes occurs the ==rasteriser== process, which interpolates across all triangles to generate actual pixels (fragments)

in order to transfer data to and from vertex/fragment shaders, [[uniforms, attributes and varyings]] are used