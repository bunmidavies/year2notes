[[COMP25212]]

- an error correction code is used to get the desired information from data which may have been corrupted
- error correction codes are most commonly encountered in communications where its easy to envisage 'interference' on a radio link - however the principle is applicable and used for computer memory
- a simple error correction code is a ==Hamming code== - data bits are grouped into a different pattern. Check bits are then added to each group in order to force a known parity

- ==believing a certain bit is wrong means it can just be flipped, since bits only have two possible states==

- hamming codes are fairly cost effective for memory protection - the overhead grows with the $log_2$ of the word size