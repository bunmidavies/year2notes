[[COMP25212]]

### ~ definition
- hamming codes work using parity ([[memory reliability]]) - you take the parity of a subset of bits being transferred / stored, and add 'check' bits to each of these groups so that you have a known parity for each group

### ~ 4-bit word example
![](https://i.imgur.com/YOLzbGO.png)
- D0-D3 is the data being transmitted / stored
- originally, within each of the circles, an initial parity is declared
- after the data is transmitted / stored, each of the circles are checked again - if there is an error in one of the bits, at least ==2 circles== will have the incorrect parity, while one circle will be undisturbed
- using this info, the faulty bit can be pinpointed
- e.g. D2 has an error - circles {C2,D1,D2,D3} and {C1,D0,D2,D3} will be disturbed, but {C0,D0,D1,D3} wont - therefore D2 has an error and can be corrected (flipped)

### ~ overhead
![ | 450](https://i.imgur.com/eOxCcnF.png)
