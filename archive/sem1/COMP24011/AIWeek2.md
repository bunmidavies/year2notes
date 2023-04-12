# Week 2 Topics
- Adversarial Search
- Minmax algorithm (walkthrough + applications)
- $\alpha$ and $\beta$ pruning - what they are and how they affect the performance of minmax algorithms
- More problems / refinements of adversarial searches


- while evaluating nodes, the **maximizing node** is whichever nodes belong to white (i.e. it is whites turn) - i think this can otherwise be known as 'your go' or the go of whoever you are trying to find the best moves for
- the winning strategy within the algorithm is to pick the daughter nodes of white which result in the maximum value in the end
- perfect information games like chess, go, tic-tac-toe etc. are known as such because they comprise of features like players take turns, both are able to see the board, and there is no uncertainty as to what will happen after an action is taken
- thus these games can be represented using a tree. However, to calculate the entire tree for a game (i.e. all possible branches) is unfeasible for games like chess or go, so the minimax algorithm which aims to find the minimum and maximum value nodes can traverse just to a certain depth


## Alpha Beta Pruning






## Video 2 - Search algorithm failures

- Standard search algorithms will fail or find many unneccessary moves for problems like the towers of hanoi. The key to writing an efficient algorithm is through understanding the search space
- For the towers of hanoi problem, the current state of the board can be represented through an array, **which is the same size as the number of discs**. Array[i] represents which pole the i'th disc lies on, where disc size increases with i (therefore Array[0] = position of smallest disc)
  ![](https://i.imgur.com/cba6Obz.png)


- The search space can be represented using triangles, and goes to show that in some cases it makes more sense to break down the problem over just bruteforcing