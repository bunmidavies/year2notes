[[COMP26120]]

### ~ intro + definition
- el gamal encryption builds on [[one way functions]], and is based on the observation that it is easy to compute a function $y$ which takes the form:
$$y = a^b\textrm{mod}p$$
- but in the average case, knowing $y$, $a$, and $p$, it is still hard to find $b$
- el gamal encryption uses the idea of ==public keys== and ==private keys==, to represent the values you can know, and others you can't know (and cannot figure out either)

### ~ encryption using el gamal
- to encrypt a number $M$, take a random $k$ which is ==relatively prime== to $p - 1$ ($p$ being a prime from the public key), using this we compute two separate values:
	- $a \leftarrow g^k\textrm{ mod }p$
	- $b \leftarrow My^k\textrm{ mod } p$
- where $g$ is a primitive root ([[modular arithmetic]])
- the message that is sent is $(a,b)$
- the [[fast modular exponentiation]] algorithm is used to do this - it avoids generating huge numbers from the $a^b$ part of the function

### ~ decryption using el gamal
- we decrypt messages using:
	- a private key $x$
	- a public key $(p, g, y)$ ($y = g^x\textrm{ mod } p$)
- we have received a message $(a,b)$ (definitions above) - but we do not know $k$ or $M$
- $y^k=(g^x)^k=g^{kx}\textrm{ mod }p$ 
- since $a = g^k\textrm{ mod }p$, $a^x$ = $y^k\textrm{ mod } p$ to find $(y^k)^{-1}$, in order to cancel out $y^k$, and return $M$
- therefore, $M = b \times (a^x)^{-1}$

### ~ creating public keys
- el gamal encryption creates public keys through picking a prime number $p$, and a primitive root $g$ ([[modular arithmetic]])
- the recipient of the message picks a private key, $x \in \mathbb{Z}_p^*$, the public key is:
$$(p,g,g^x\textrm{ mod }p)$$
- the third argument $g^x\textrm{ mod }p$ might sometimes be written as just $y$