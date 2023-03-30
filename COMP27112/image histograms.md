[[COMP27112]]

- an image histogram just counts the ==frequencies== of specific greyscale values in an image - it can be represented using an array, for instance:
```C
int histogram[256] = {0};

for (int i = 0; i < pixels_in_img; i++)
{
	histogram[img[i]]++;
	//where img[i] stores the greyscale value
}
```

![ | 550](https://i.imgur.com/pcdWf56.png)

- in this example, the gaps show that there are a bunch of missing greyscale values, but humans are still able to interpret the image as being 'normal'
![ | 550](https://i.imgur.com/QU3bCYz.png)
