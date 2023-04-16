[[COMP25212]]

### ~ definition
- a bus is used to encompass the logical bundle of 'stuff' between a processor and other parts of a computer
- 'stuff' can probably be also thought as a pathway made up of electronic cables
- system architectures can get quite complex (i.e. many devices) - therefore, these devices can be interconnected with buses
- there are 2 main metrics involved with buses: latency and bandwidth
- though a bus may have a certain width e.g. 4 bytes, in some cases you may only want to transfer 1 byte (without overwriting 3 other bytes), and this can be possible with a bus

### ~ latency
- ==latency== - the time taken for a transaction/request to travel from source component to destination component over the bus

### ~ bandwidth
- ==bandwidth== - the amount of data which can be transferred over the bus in a fixed period of time
- bandwidth can be increased by cycling the bus faster (difficult in practice), or making the bus wider - however, this is most effective when the width of the data being transferred is known - for 'random' transfers, bandwidth may not necessarily be improved by just having a wider bus

### ~ interconnection
- single shared buses can scale easily, but ==bottleneck==
- crossbar buses offer ==parallelism== but can ==scale badly== ($O(n^2)$ crossbar buses where $n$ is the no of devices?). Comparable to an many-to-many type relationship
![ | 550](https://i.imgur.com/O5HW5Qd.png)
- Network on Chips essentially allow for devices to communicate with eachother through a tiny LAN network (like very small, order of cm$^2$) 
![ | 550](https://i.imgur.com/gr0cVxN.png)
- blue octagon = router, red pentagons = processors

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


