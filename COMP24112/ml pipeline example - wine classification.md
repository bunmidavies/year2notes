[[COMP24112]]

### ml pipeline example: wine classification
![](https://i.imgur.com/7mCL1Bs.png)


the wine must be made of one of the two grapes shown in the picture, but which one was actually used is unknown

- wine experts will identify this by smelling and tasting the wine
- chemists will know certain chemical quantities differ between wine types

*how can a machine learning system determine which wine type this is?*
machine learning systems will ==collect measurements== - the task at hand is to now recognise the grape type of a given wine sample based on its measured chemical quantities

in order for an ML system to be able to recognise this, wine samples for each grape type must have been collected beforehand - then each wine sample can be characterised by the chemical features it contains (the example shows 13 different chemical features, 30 samples)

now, a mathematical model can be created to predict the grape type (controlled by 14 different parameters in the example)

using the predicted grape types from the model, we compare them to the real grape types. How close/correct the model was can be the ==objective function==

once this 'training' process is done, unseen bottles of wine can now be identified once the measurements are collected