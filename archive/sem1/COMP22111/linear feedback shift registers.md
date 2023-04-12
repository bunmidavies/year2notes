[[COMP22111]]

when testing circuits, you may want to use random test patterns / data to have assurance when testing designs
LFSRs generate pseudo-random sequences, which can be used to test a chip with reliably random data

the two main types of LFSR are **maximal-length LFSRs** and **weighted LFSRs**

many chips may also have a **Built-in Self-Test** ability, by having a multiple-input signature register (MISR), a type of LFSR, built within itself

### how LFSRs work
there are different forms of LFSRs, but they generally use XORs while shifting a value repeatedly in order to generate 'random' bits
![](https://i.imgur.com/8CVp0K2.png)

with each line, the value is being shifted to the left, and an xor is being performed against the very left bit and the bit 1 over to the right of it