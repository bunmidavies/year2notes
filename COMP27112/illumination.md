[[COMP27112]]

illumination models, like most things in computer graphics involve ==approximation== 

there are two main ways to model light-matter interaction in a scene
- ==local illumination== takes a direct light source and illuminates the according surfaces - however this light hits these surfaces is how the surface is rendered (i.e. coloured in)
- ==global illumination== takes into account indirect illumination - i.e. direct light hits some surface, then some light reflects off that surface and hits another surface. This is more accurate than local illumination

COMP37111 (year 3) looks at global models, meanwhile in COMP27112 we just implement local models

![](https://i.imgur.com/nm5afSV.png)

- as shown in the diagram above, a surface gets its actual colour from the small transparent layer with pigment particles, causing reflected light to pick up a colour

- there are different types of illumination for given light sources

### ambient illumination
- a light source which gives off rays of light which reflect around all of the scene, until the entire scene is ==uniformly illuminated==
- we call a monochrome intensity of ambient light $I_a$ - the amount of ambient light diffusely reflected from a surface is:
	  $I_\textrm{ambient} = k_aI_a$
- $k_a$ is the ==ambient reflection coefficient== which lies between 0 and 1
- seeing an example, we can see due to the uniform illumination, every object is made up of a singular colour
![](https://i.imgur.com/xnWatsH.png)

### directional lighting
- directional lighting takes into account how far away a given object is from a point light source
![](https://i.imgur.com/0hMMYKb.png)
- Lambert's Law states that $I_e = I_p cos\theta$, where $I_p$ is the intensity of the light source, and $I_e$ is the intensity of the light ray received
- diffuse reflectivity of a surface aka the ==diffuse reflection coefficient== of the surface is known as $k_d$
- the amount of the diffusely reflected light is:
	- $I_\textrm{diffuse} = I_pk_dcos\theta$ aka  $I_\textrm{diffuse} = I_pk_d(\hat{N}\cdot\hat{L})$

### combining ambient + diffuse
- $I$ = ambient + diffuse results in:
	$I = k_aI_a + I_pk_d(\hat{N} \cdot \hat{L})$
![](https://i.imgur.com/Nbe0Sz0.png)
