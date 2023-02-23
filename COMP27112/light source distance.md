[[COMP27112]] - related to [[illumination]]

- Light intensity falls of with the square of the distance travelled by the light - thus after travelling $d$, the original intensity $I_p$ turns into $I_e$:
$$I_e = \frac{I_p}{4\pi d^2}$$
- this is how it works in real life, but as the $d^2$ term changes too rapidly, we introduce our own ==approximation==
$$I_e = \frac{I_p}{k_c + k_ld + k_qd^2}$$
- where $k_c, k_l$ and $k_q$ are all parameters that we finetune for the best results

- when building a local [[illumination]] model, we can incorporate both ambient lighting and distance:
![](https://i.imgur.com/Ayr8Y1H.png)
- $d'$ is the denominator of our 'new intensity' equation above, i.e. $k_c + k_ld + k_qd^2$