[[COMP24112]]

### ~ components of an ML system
an ML system is comprised of the following components:
- Data
- A mathematical model / function
- Objective function (i.e. [[loss function]], error function)
- Training algorithm (which ==uses the objective function==)

The training algorithm is what ==optimises the parameters== for the function, unlike the objective function which is only able to judge ==how well== the parameters are set, without actually changing the parameters

==the final model with predetermined parameters is your 'final product'==

The pipeline for building a machine learning system essentially comprises of 2 main components: ==construction== and ==training==. But there is also a final evaluation part
![ | 500](https://i.imgur.com/CKOnZYA.png)


### model construction
- model construction involves preparing ==experience E== in some preferred data format
- the task at hand needs to be characterised by a ==parametric model== (i.e. how the task is completed, depends on its parameters)
- the performance metric, which is essential for [[ML optimisation]] needs to be characterised by some ==objective function== aka [[loss function]] ($O(\theta)$, where $\theta$ are parameters fed into the model)


### training
- Training/learning involves determining what model parameters should be used, by finding the parameters which ==optimise== the objective function (i.e. minimizing/maximizing)
- we also know this as the parameters obeying the [[optimality condition]]


### evaluation
- The determined model / parameters are evaluated using some performance metric
- Machine learning research builds on optimisation theory, linear algebra, probability theory etc.


### [[ml pipeline example - wine classification]]