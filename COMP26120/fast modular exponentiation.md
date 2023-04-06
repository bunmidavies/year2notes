[[COMP26120]]

### ~ background
- the purpose of the fast modular exponentiation algorithm is to calculate $a^b \textrm{ mod } n$
- this method is used because it signficantly ==reduces the amount of computation== which would typically be required if you were to perform $a^b$, then the modulo operation
- [[Algorithm Design and Applications.pdf]] and [[intro to algorithms 4th edition.pdf]] present the fast modular exponentiation method in different looking ways, although they do the same thing - both work with binary in order to perform $a^b \textrm{ mod } n$, but intro to algorithms shows the binary in a more explicit manner

### ~ algorithm(s)
- from [[Algorithm Design and Applications.pdf]]
![ | 350](https://i.imgur.com/GmcGhZN.png)
- from [[intro to algorithms 4th edition.pdf]]
![ | 350](https://i.imgur.com/C4KIxr6.png)
