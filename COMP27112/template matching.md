[[COMP27112]]

### definition
- template matching is a technique in image processing to find regions in an image which match a given template / pattern, where that template can just be a subimage

### process
- the main process in template matching, like [[convolution]] is to just move the template around the image
- the template pixels are multiplied with the corresponding image pixels, and the sum is stored in the centre pixels
- the image pixels are normalised under the template (by dividing each pixel by the region sum)
- the pixels with the highest (normalised) values will correspond to the closest match - they may not all have the same values, but they'll have higher scores compared to the rest of the image
- regular [[thresholding]] can just be used at this point in order to find the regions which closely mage within the image

### problems
- if the template is rotated slightly, certain matches may not occur
- much better results can be achieved with [[feature detection]] (ai link atm)