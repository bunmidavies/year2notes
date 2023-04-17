[[COMP25212]]

### ~ soft errors
- soft errors refer to errors caused by things like cosmic rays / alpha particles, interfering with the stability of memory cells, resulting in corruption / altering of data in memory
- theyre known as 'soft' since they dont cause permanent damage, and also are relatively rare - but their occurence increases as memory density increases, and computer systems become more complex and operate at higher speeds
- in short theyre rare, but as memory gets bigger the probability increases, and they can become a genuine concern

### ~ parity
- parity is a simple method of error checking in data transmission / storage
- an additional bit aka a ==parity bit== is added to a group of bits being transmitted / stored:
	- ==even parity== - set parity bit accordingly to make number of 1s even
	- ==odd parity== - set parity bit accordingly to make number of 1s odd
- during transmission / storage, the expected parity bit is calculated using the received group of bits, and compared to the received parity bit
- if expected parity bit $\neq$ received parity bit, ==an error has occured==

### ~ error correction codes
- ECCs build on from parity, by providing a way to ==correct== errors, rather than simply detect them
- there are various ECC techniques, but the basic idea behind all of them is to introduce ==redundancy== in the data, i.e. extra bits which help to detect and correct errors
- [[hamming codes]] are a common ECC technique