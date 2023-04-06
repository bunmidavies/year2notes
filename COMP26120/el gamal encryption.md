[[COMP26120]]

### ~ intro + definition
- el gamal encryption builds on [[one way functions]], and is based on the observation that it is easy to compute a function $y$ which takes the form:
$$y = a^b\textrm{mod}p$$
- but in the average case, knowing $y$, $a$, and $p$, it is still hard to find $b$
- el gamal encryption uses the idea of ==public keys== and ==private keys==, to represent the values you can know, and others you can't know (and cannot figure out either)

### ~ encryption using el gamal
- to encrypt a message, take a random $k$ which is ==relatively prime== to $p - 1$ ($p$ being a prime from the public key), and compute $a^b\textrm{mod}k$ for various numbers (where the 'various numbers' are parts of your message)
- the [[fast modular exponentiation]] algorithm is used to do this - it avoids generating huge numbers from the $a^b$ part of the function

### ~ decryption using el gamal
- to decrypt a message, ???

### ~ creating public keys
- el gamal encryption creates public keys through picking a prime number $p$, and a primitive root $g$ ([[modular arithmetic]])
- the recipient of the message picks a private key, $x \in \mathbb{Z}_p^*$, the public key is:
$$(p,g,g^x\textrm{ mod }p)$$