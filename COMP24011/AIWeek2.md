# Week 2 Topics
- Adversarial Search
- Minmax algorithm (walkthrough + applications)
- $\alpha$ and $\beta$ pruning - what they are and how they affect the performance of minmax algorithms
- More problems / refinements of adversarial searches


- while evaluating nodes, the **maximizing node** is whichever nodes belong to white (i.e. it is whites turn) - i think this can otherwise be known as 'your go' or the go of whoever you are trying to find the best moves for
- the winning strategy within the algorithm is to pick the daughter nodes of white which result in the maximum value in the end
- perfect information games like chess, go, tic-tac-toe etc. are known as such because they comprise of features like players take turns, both are able to see the board, and there is no uncertainty as to what will happen after an action is taken
- thus these games can be represented using a tree. However, to calculate the entire tree for a game (i.e. all possible branches) is unfeasible for games like chess or go, so the minimax algorithm which aims to find the minimum and maximum value nodes can traverse just to a certain depth

## Minmax limitations

- the minmax algorithm is extremely effective for simple games like othello. But for more complex games like go or chess, the basic minmax algorithm has a lot of limitations and would require a number of refinements, for instance:
	- games like chess have a number of standard openings - the basic minmax algorithm wouldn't know this, thus wastes a lot of time repeatedly over chess openings which could be extremely common
	- due to the minmax algorithm only executing to a certain depth, there is a chance that a move which looks promising up to a certain depth has a devestating counter 1 move after. This is known as the **horizon effect**. A known method of combating such an effect is searching further depending on the activity on the board
	- static evaluation functions are also inappropriate for games like chess, since simply counting the number of pieces can't always be representative of who is really winning / losing. A way that this can be improved is through machine learning, and creating a board evaluation function which applies / adjusts weights to certain pieces on the board


## Alpha Beta Pruning

- The first thing to understand is that alpha beta pruning can be added to the already existing minmax algorithm, and **does not change the outcome** of the algorithm. It simply exists to speed up the process, and skip nodes which will not affect the outcome of the algorithm
- How alpha beta pruning actually works can be seen as moving on from a node as soon as it's known that no further nodes will affect the algorithms result. This works through:




## Video 2 - Search algorithm failures

- Standard search algorithms will fail or find many unneccessary moves for problems like the towers of hanoi. The key to writing an efficient algorithm is through understanding the search space
- For the towers of hanoi problem, the current state of the board can be represented through an array, **which is the same size as the number of discs**. Array[i] represents which pole the i'th disc lies on, where disc size increases with i (therefore Array[0] = position of smallest disc)
  ![[Pasted image 20221009154740.png]]

- The search space can be represented using triangles, and goes to show that in some cases it makes more sense to break down the problem over just bruteforcing