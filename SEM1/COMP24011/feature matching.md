[[COMP24011]] / #comp24011
following on from [[feature description]]

- feature matching is the strategy where you look for likely matches in a number of images/files
- the main strategies include:
	- *euclidean distance* - a threshold is set arbitrarily for maximum distance
	- $t1$ is threshold 1, and $t2$ is threshold 2. t1 is the solid circle surrounding 1/2, and t2 is the dashed circle surrounding 1/2
	  ![](https://i.imgur.com/cjynjIO.png)
	  ![](https://i.imgur.com/XxjKpkN.png)

	- *nearest neighbour* - simply take the nearest neighbour, but sometimes thresholds can still be used
	- *nearest neighbour distance ratio matching* (NNDR) - $d_1/d_2$, where $d_1$ is the distance between target descriptor and nearest neighbour. $d_2$ is the distance between the target descriptor and the 2nd nearest neighbour


## tracking

- tracking only searches a small neighbourhood around a detected feature in the next images

- error metrics include - sum of squared differences, normalised cross correlation
- affine motion models are used for feature tracking, e.g. Kanade-Lucas-Tomasi (KLT) tracker