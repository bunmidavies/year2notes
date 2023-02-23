[[COMP27112]]

- specular reflection are the curved, shiny highlights you get on objects
![](https://i.imgur.com/CedCR6a.png)
- very few surfaces are perfectly specular ([[reflection]]), and imperfect specular reflection involves a bunch of rays of light which aren't at a perfect angle being reflected
- we want to calculate how much light is reflected towards the viewer, not caring about other rays of light which should bounce off
![](https://i.imgur.com/YnBrVu7.png)

specular reflection depends on:
- the angle between the reflected ray of light and the vector towards the observer, $\phi$ - if there is no difference in the angle between these two, then the ==observed specular== would be no different, i.e. its 100% of the reflected ray
- the incident angle $\theta$ and wavelength $\lambda$

therefore a function to calculate the amount of specular light reflected uses these 3 variables
$$I_{specular} = S(\phi,\theta,\lambda)$$

- as the angle between the reflected ray and viewer vector change, the amount of specular light seen will also change - this can be approximately modelled as $F \approx cos^n\phi$
- $F$ is known as ==Phong's specular function==, and is a bit different to the approximation above (hence why its an approximation)
![](https://i.imgur.com/QUV3nF4.png)
- using the approximation, we can say:
	- $I_{specular} = I_pcos^n\phi$ which can be turned into
	- $I_p(\hat{R}\cdot\hat{V})^n$
- $n$ is usually between 1 and 200
![](https://i.imgur.com/6yCkADw.png)
- $F$ can also be approximated as $k_s$, at a cost of quality, but in favour of performance
![](https://i.imgur.com/fOFUo6I.png)
![](https://i.imgur.com/m8u3m8s.png)

### incorporating colour
- it is easy to incorporate colour within surfaces, simply by expressing light colour as a triple of RGB intensities, and then expressing ==ambient and diffuse reflectivity== for the surface colour
![](https://i.imgur.com/AJb3st1.png)
![](https://i.imgur.com/ddpHtJC.png)


### multiple lights
- for working with multiple lights, simply sum the illumination intensities together
![](https://i.imgur.com/DoUXhHn.png)
- note that ambient doesn't need to be summed since ambient is a uniform colour anyways