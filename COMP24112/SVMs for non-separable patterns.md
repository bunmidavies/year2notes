[[COMP24112]]

### definition
- the hard margin SVM ([[support vector machines (SVMs)]]) essentially only works for data patterns which are fully separable, since the constraints are set in stone - in reality, data will often not be able to meet these constraints
- for a ==non-separable linear data pattern==, we use the ==soft-margin SVM==, which uses a slack variable in order to relax the hard constraints 
- the new constraints are shown below
![](https://i.imgur.com/zuvxDsg.png)
- with hard-margin SVM, all the datapoints were on either side of the two margins, only on the outside
- with soft-margin SVM, datapoints are allowed to stay within the margin
![](https://i.imgur.com/1gA1I72.png)
- now, a new optimisation problem and dual problem is introduced (similar to the hard margin problems)
- since the problem is slightly altered, the definition of a ==support vector== in this case is also slightly altered - support vectors now satisfy $y_i(w^Tx_i + b) \leq 1$
- these support vectors either fall within the margin, fall on the wrong side of the separating hyperplane, or sit along one of the two parallel hyperplanes

### kernel SVM
- the kernel SVM essentially maps inputs from a 2D space to higher dimensional feature space - a kernel is useful for patterns which are ==non-linear==
- see [[handling non-linear data patterns]] for more info on kernel functions
![](https://i.imgur.com/mzw4uE1.png)
