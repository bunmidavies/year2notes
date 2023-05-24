[[COMP27112]]

### intro
- to define whether a pixel belongs to the same group as its adjacent pixels, we use the idea of connectivity
- there are 2 main types of connectivity we consider

### 4-connected
![](https://i.imgur.com/otJBUV1.png)
- the main downside of 4-connected is that objects which join at corners may become disconnected
![](https://i.imgur.com/CwzNzsk.png)


### 8-connected
![](https://i.imgur.com/S2LyJal.png)
- the main downside of 8-connected is that thin objects - i.e. two objects which cross over each other - may now be considered to be one object
![](https://i.imgur.com/QKmodGI.png)
