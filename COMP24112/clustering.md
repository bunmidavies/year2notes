[[COMP24112]]

### definition
- clustering is the task of ==grouping== a set of objects such that objects in the same group are ==more similar== to each other than those in other groups - each group is known as a ==cluster==
- clustering is [[unsupervised learning]] - there are no predefined classes, nor training data
- when the term 'similar' is used, this can mean a variety of things - since the objects usually have a set of features, corresponding to data points in a high-dimensional space, similarity can be the ==distance== between these pairs of data points ([[distance measuring for k-NN]])
- these similarities/distances may also just be provided

### key tasks
- the key tasks required to perform clustering can be summarised as such:
	1. define the appropriate ==distance measuring technique==
	2. identify the natural ==cluster number== - this is essentially a hyperparameter which must be selected
	3. find a way to group objects into ==sensible clusters==
	4. ==evaluate== the clustering output

### clustering example - animals
- an example of clustering is to take a set of animals, each with a single feature - whether they have lungs or not
- if the animal has lungs, this feature can be represented with a 1 (yes), otherwise a 0 (no)
![|450](https://i.imgur.com/k0B9lmW.png)
- a distance matrix can now be formulated using this info
![|450](https://i.imgur.com/hlkRq2Y.png)
- this matrix then gets reordered, which will leave you with your clustering
![|450](https://i.imgur.com/HQhpstW.png)


