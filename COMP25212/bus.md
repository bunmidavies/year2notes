[[COMP25212]]

Bus is used to encompass the logical bundle of 'stuff' between processors and memory

System architectures can get quite complex (i.e. many devices) - therefore, these devices can be interconnected with buses

These devices/structures can share buses:
- Single shared buses can scale easily, but ==bottleneck==
- Crossbar buses offer ==parallelism== but can ==scale badly== ($O(n^2)$ crossbar buses where $n$ is the no of devices?)

- [[Network on Chip]]s are increasingly common?

Bus carried information:

| content   | info                                                              |
| --------- | ----------------------------------------------------------------- |
| operation | no-op / data write/data read / instruction fetch                  |
| address   | may include byte selection                                        |
| data      | both directions                                                   |
| privilege | applications cant use all the space - some is reserved for the OS |
| ready     | sometimes memory is slow - applications may have to wait          |
| abort     | sometimes the transaction can be refused, so this has to be relayed                                                                  |

==Bus bridges== are useful for converting data from one protocol to another




### System bus organisation
