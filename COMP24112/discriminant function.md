[[COMP24112]]

a discriminant function is a simple mapping function which maps ==an input to a class==

- discriminant functions are typically used for [[classification]]
![](https://i.imgur.com/UNfejcM.png)

- outputs can be converted to a class prediction simply by ==thresholding== - the example below shows binary classification involving two classes, A and B
  ![](https://i.imgur.com/WSCVUdn.png)

- the real number $t$ can be treated as a ==hyper-parameter==
- $t = 0$ is a common setting within discriminant functions
- a set of inputs which give $f(x) = t$ is called a ==level set== of $f$