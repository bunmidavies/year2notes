[[COMP27112]]

### intro
- to understand why many different image formats exist, we'd want to think about what we want to store in an image file first:
	- image data (pixels)
	- colour palette
	- different size versions
	- transparency information
	- camera data
	- location (lat/long)
- many different formats exist since they need to serve many different purposes:
	- proprietary formats
	- open standards
	- level of colour being stored
	- bit depth
	- new info to be stores (e.g. camera info/location)

### portable bit map (.pbm)
- after thresholding an image, every pixel is either black or white - therefore, each pixel can be represented by a single bit
- the portable bit map format rather than storing each pixel as a byte, stores it as a single bit for the reason above, so we're able to pack eight pixels into one byte
![|450](https://i.imgur.com/6MvZVLa.png)

### 16-bit per channel formats
- TIFF = Tagged Image File Format
- PNG = Portable Network Graphics
- JPEG2000
- HDMI

### GIF
- GIF = The Graphics Interchange Format
- GIF has 8-bits per pixel, even for colour - the way it does this is through using only 256 colours from the 24-bit RGB colour space, and saving that constricted palette in the image file (table on the right)
![](https://i.imgur.com/FYHFQEh.png)

### 8-bit colour
- GIF has shown how to use 8 bits to represent a colour pixel, but another popular way is to pack the colour into 8 bits without using a palette
- this is done by using:
	- 3 bits for red
	- 3 bits for green
	- 2 bits for blue
- this is popular in embedded LCD displays

### windows icon file (.ico)
- the windows icon file can store multiple different size images in a single file, to allow the OS to choose an appropriate one, to make sure all of them look good at any resolution

### transparency
- transparency is enabled within images by using an ==alpha channel== - an alpha channel in an image file says how 'see-through' a pixel should be
- .png has the ability for transparency, while .jpeg does not