[[COMP24011]]

the minimax algorithm is used wtihin [[adversarial search]]/2 player game problems, as it determines the ==worst-case== outcome for both players, by assuming both players play ==optimally==

for games, in this example each ==daughter== is a ==move== 
![](https://i.imgur.com/v07YsRB.png)

![](https://i.imgur.com/ewYNzXQ.png)


the main problem with minmax is that the number of states it has to examine is ==exponential== with the depth of the tree - the solution to this is being able to ==prune== certain nodes ([[pruning]]) - a technique involving this is called [[alpha-beta pruning]]

### minmax limitations
- the minmax algorithm is extremely effective for simple games like othello. But for more complex games like go or chess, the basic minmax algorithm has a lot of limitations and would require a number of refinements, for instance:
	- games like chess have a number of standard openings - the basic minmax algorithm wouldn't know this, thus wastes a lot of time repeatedly over chess openings which could be extremely common
	- due to the minmax algorithm only executing to a certain depth, there is a chance that a move which looks promising up to a certain depth has a devestating counter 1 move after. This is known as the **horizon effect**. A known method of combating such an effect is searching further depending on the activity on the board
	- static evaluation functions are also inappropriate for games like chess, since simply counting the number of pieces can't always be representative of who is really winning / losing. A way that this can be improved is through machine learning, and creating a board evaluation function which applies / adjusts weights to certain pieces on the board