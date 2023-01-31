[[COMP24112]]

an ML system is comprised of the following components:
- Data
- A mathematical model / function
- Objective function (i.e. loss function, error function)
- Training algorithm (which ==uses the objective function==)

The training algorithm is what ==optimises the parameters== for the function, unlike the objective function which is only able to judge ==how well== the parameters are set, without actually changing the parameters

==the final model with predetermined parameters is your 'final product'==

building a machine learning system is comprised of a few key stages:

### model construction

This involves preparing ==experience E== in some preferred data format
The task at hand needs to be characterised by a ==parametric model== (i.e. how the task is completed, depends on its parameters)
The performance metric, which is essential for [[ML optimisation]] needs to be characterised by some ==objective function== ($O(\theta)$)


### training

Training/learning involves determining what model parameters should be used, by finding the parameters which ==optimise== the objective function (i.e. minimizing/maximizing)


### evaluation

The determined model / parameters are evaluated using some performance metric


Machine learning research builds on optimisation theory, linear algebra, probability theory etc.


### ml pipeline example: wine classification
![[Pasted image 20230131141253.png]]

the wine must be made of one of the two grapes shown in the picture, but which one was actually used is unknown

- wine experts will identify this by smelling and tasting the wine
- chemists will know certain chemical quantities differ between wine types

*how can a machine learning system determine which wine type this is?*
machine learning systems will ==collect measurements== - the task at hand is to now recognise the grape type of a given wine sample based on its measured chemical quantities

in order for an ML system to be able to recognise this, wine samples for each grape type must have been collected beforehand - then each wine sample can be characterised by the chemical features it contains (the example shows 13 different chemical features, 30 samples)

now, a mathematical model can be created to predict the grape type (controlled by 14 different parameters in the example)

using the predicted grape types from the model, we compare them to the real grape types. How close/correct the model was can be the ==objective function==

once this 'training' process is done, unseen bottles of wine can now be identified once the measurements are collected