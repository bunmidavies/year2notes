[[COMP25212]]

- in a [[direct mapped cache]], there is no choice in terms of which tag should be evicted, since you can't store something else within that tag (if its storing a different memory address) - all memory addresses only have one location they can belong in
- if a cache is not direct mapped, or you are dealing with a [[set associative cache]], then a specific ==set== or entry will need to be picked:
	- ==Round Robin== - easiest to implement, simply loop around
	- ==LRU== - hard to implement quickly (in hardware), but provides good results
	- ==Random== - fairly easy to implement, and reasonably effective