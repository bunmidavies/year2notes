[[COMP27112]]

### Run-Length Encoding (RLE)
- run length encoding will store how many times a pixel value repeats in an image as a pair, in an attempt to reduce the number of values stored
- this can work well if there is a lot of repeating data within an image, but can also introduce more overhead if this isn't the case - when there are lots of changes we can describe this as high frequency
![|450](https://i.imgur.com/4hX2l7x.png)
- simple run length encoding is an example of ==lossless compression== since the exact same image can be reconstructed
- file formats such as PCX and JPEG use RLE (but a lossy method)
##### JPEG compression
- JPEG uses discrete cosine transforms (DCT) to transform the values of pixels in an image
- these DCT values can then be divided by values in a ==quantisation table==, in order to reduce higher frequency coefficients
- RLE is then applied to the quantised DCT table in a zigzag pattern
- to decompress images, the values from the compressed version are put in a table and multiplied by the JPEG quantisation table, then have the inverse DCT operation applied
- the values are typically very close to the original, but not exactly the same - this makes this form of compression ==lossy==
![](https://i.imgur.com/YImxwI3.png)
- by reducing the quality (lower quality = more compression), the blockiness within DCT becomes more and more noticeable