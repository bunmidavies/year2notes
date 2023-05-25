[[COMP27112]]

==Uniforms==:
- sent to vertex and fragment shaders
- these stay ==constant throughout a single frame==
- typically ==single values== i.e. material colour, shininess

==Attributes==:
- values applied to ==individual vertices== - therefore if you had an array of attributes, you would want to have enough such that there is one array value per vertex
- available only to the vertex shader
- each vertex can have an array of attributes

==Varyings==:
- variables declared in the vertex shader, and shared to the fragment shader
- i.e. the main way of passing data from vertex shader to fragment shader
- the varying variable must be declared wtih the same name and type in both shaders

example vertex shader
```HTML
<script type="x-shader/x-vertex" id="vertexshader">
	uniform float amplitude;
	attribute float displacement;
	varying vec3 vNormal;

	void main() 
	{
		vNormal = normal;
		//multiply displacement by amplitude
		//amp gets animated so we have animated displacement
		vec3 newPosition = position + normal * vec3(displacement * amplitude);

		gl_Position = projectionMatrix * modelViewMatrix * vec4(newPosition,1.0);
	}
</script>
```

example fragment shader
```HTML
<script type="x-shader/x-fragment" id="fragmentshader">

	// same name and type as vertex shader
	varying vec3 vNormal

	void main()
	{
		// calc the dot product and clamp
		// 0 -> 1 rather than -1 -> 1 ?
		vec3 light = vec3(0.5,0.2,1.0);

		// ensure its normalized
		light = normalize(light);

		// dot product
		float dProd = max(0.0,dot(vNormal,light));

		// feed into frag colour
		gl_FragColour = vec4(dProd, dProd, dProd, 1.0);
	}
</script>
```

the actual code which creates the material and uses the shaders:
```JavaScript
var attributes = {
		displacement: {
			type:"f", // a float
			value: [] // an empty array
		}
};

var uniforms = {
		amplitude: {
				type: "f",
				value: 0
		}
};

// create sphere material
var shaderMaterial = new THREE.MeshShaderMaterial({
	uniforms: uniforms,
	attributes: attributes,
	vertexShader: $('#vertexshader').text(),
	fragmentShader: $('#fragmentshader').text()
});

// create sphere mesh
var sphere = new THREE.Mesh(
	new THREE.Sphere(radius, segments, rings),
	shaderMaterial
	);

var vertices = sphere.geometry.vertices;
var values = attributes.displacement.value;
for (var v = 0; v < vertices.length; v++)
{
	values.push(Math.random() * 30);
}

// add the sphere to the scene
scene.addChild(sphere);

var frame = 0;

// draw
function update()
{
	uniforms.amplitude.value = Math.sin(frame);
	frame += 0.1;
}
)

```

- the important part to note is how the shaderMaterial - i.e. the material of the sphere mesh - defines is vertexShader and fragmentShader
- it essentially takes the function names as attributes, and these end up being the actual shaders used for that mesh material