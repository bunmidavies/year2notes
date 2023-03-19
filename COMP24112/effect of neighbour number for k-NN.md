[[COMP24112]]

neighbour number i.e. $k$ is known as a ==hyper-parameter==

a hyper-parameter is a parameter which needs to be chosen in advance of the actual training of a model - determining which $k$ to use in this instance is known as ==hyper-parameter selection / model selection==

for binary classification ([[classification]]), setting k to an even number is ==bad== - when k is an even number it creates the possibility of the k nearest neighbours being perfectly split between both classes. This makes it ==impossible to reach a decision==

- small k = ==we may model noise==
![](https://i.imgur.com/kwpuPIn.png)

as can be seen on the right, some of the regions are now being turned into incorrect regions - this is due to a k of 1 which is capturing this 'noise' i.e. wrong samples

- large k = neighbours will include too many samples from other classes, which can reduce accuracy of the prediction
![](https://i.imgur.com/A5E98E7.png)

in this example, k=35 which causes too many samples which aren't nearby to be considered, which can cause unwanted results