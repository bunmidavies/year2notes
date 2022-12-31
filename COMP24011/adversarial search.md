[[COMP24011]]

==adversarial search== problems are also known as ==games==, which typically take place in deterministic, turn-taking ==two player games== of [[perfect information]]

these problems are typically interesting because they are ==too hard to solve== - there are more possible chess games than there are ==atoms== in the universe, so algorithms for chess games have to make use of the time they have, and search for moves which are feasible to compute

[[pruning]] is a technique typically used within adversarial searching to ignore portions of a search tree that won't affect the final choice - [[Heuristic Methods]] and ==evaluation functions== allow approximation of a state without complete searches

the [[minimax algorithm]] is used to determine the optimal strategy within a game tree under the impression that ==both players play optimally== from the current node to the ==end of the game==

