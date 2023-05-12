[[COMP27112]]

### definition
- both [[convolution]] and binary morphology involve passing ==structuring elements== (SE) over an image, one pixel at a time
- different operations are applied to the images depending on the operation, covered below
- for all binary morphology operations, ==the output is drawn onto a new image== - i.e. the changes applied to a centre pixel are not taken into account for the following pixels

### erosion
- ==rule== - the structuring element i.e. the blue square, passes over the entire image - if a pixel which is part of the ==object== (in green) is found in the centre pixel of the SE, with ==any== other elements of the SE being background, this centre pixel gets turned into a background pixel
- ==this removes all border pixels of an object==, making objects smaller than they were

### dilation
- ==rule== - if the centre of the SE is over a background pixel, and any other pixels of the SE are over an object pixel, the pixel under the centre becomes object
- this will make objects larger than they were

### opening
- opening will get rid of bits which 'stick out' in an image, while also enlarging holes - this is achieved by first eroding then dilating:
- ==open(image) = dilate(erode(image))==

### closing
- closing will fill in holes and fill out bits which 'stick out', by dilating then eroding
- ==close(image) = erode(dilate(image))==

![](https://i.imgur.com/iUCQ1dF.png)
