[[COMP27112]]

as already mentioned in previous weeks, there is a [[fixed graphics pipeline]] and a [[programmable graphics pipeline]]

there are two main types of shader:
- vertex shader
- fragment shader

the vertex shader program (which is the first part of the programmable pipeline) as well as the fragment shader program (second to last) must be provided by the user, and is written in [[GLSL]]

==all shapes are made of vertices== - the vertex shader program receives each of these in turn, does some processing, and then sets a value for where the vertex will appear onscreen (gl_position, a `vec4`)

when any material is created in three.js, it will create shaders which you can modify (meaning if a shader is omitted, it is automatically created anyways)

the ==fragment shader== determines what colours are given to pixels, by setting a value for gl_FragColor (another `vec4`), and represents the final fragment colour

in between the vertexShader and fragmentShader processes occurs the ==rasteriser== process, which interpolates across all triangles to generate actual pixels (fragments)

in order to transfer data to and from vertex/fragment shaders, [[uniforms, attributes and varyings]] are used