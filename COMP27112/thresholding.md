[[COMP27112]]

- one of the main purposes of [[image histograms]] are for manually selecting correct ==threshold values==
- however, if lots of images are being processed, manually examining the histogram may not be practical
- there are a number of methods to ==automatically determine threshold values==

### percentile (P-tile) calculation of $T$
- if we know that an object should occupy a certain percentage of pixels in an image, we can automatically select $T$, e.g. a biscuit on a conveyor line should occupy 41% of the image
- the steps are as follows:
	1. Calculate no of pixels which should be object
	2. Create image histogram
	3. Accumulate frequencies until cumulative sum of pixels > expected object pixels
	4. Return current grey level as $T$
- in the following example, you basically start from 0 on the x axis, and add the values until the cumulative sum is > expected object pixels
![ | 550](https://i.imgur.com/vsKKD6L.png)
- P-tile calculation isnt affected by brightness adjustment, unlike if you were to be gauging the T value manually by eye

### finding a threshold between means of upper/lower parts
- the average intensity is calculated by using the number of pixels at specific grey levels at any point
- the algorithm to find the threshold is as follows:
	1. For $i = 1$ to $i = 255$, calculate average intensity below $i$ and above $i$
	2. midpoint for current $i$ = (average below $i$ + average above $i$) / 2
	3. final $T$ value = midpoint which is closest to corresponding $i$


### Otsu's method
- otsus method is named after Nobuyuki Otsu
- algorithm info is on [wikipedia](https://en.wikipedia.org/wiki/Otsu%27s_method)