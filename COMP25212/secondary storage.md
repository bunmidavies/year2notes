[[COMP25212]]

### ~ definition
- secondary storage exists outside of the main address space (i.e. the address space of the processor)
- it uses ==implicit addresses== e.g. filenames
- there are two main uses for secondary storage:
	- filing system
	- page store (to allow for more virtual memory)
- the most common technologies for secondary storage today are:
	- magnetic disk
	- optical disc
	- solid state / flash memory (SSD)
- the two main characteristics of any secondary storage is its ==latency== and ==bandwidth== - similar to a [[bus]]

### ~ magnetic disks
- magnetic disks usually exist as stacks, and both sides are used - they are read from/written to using an arm with magnetic heads (moving radially)
- bits are encoded on a magnetic disk using ==polarisation== of domains on the surfaces
- data storage is organised/indexed in blocks
- typical drives might provide ~20TB storage
- the ==latency== of the disk is the time to move the heads to the right track, and depends on the starting point and desired track (smart organisation would put important stuff close together)
- an average ==half a turn== is added onto this time for the disk to reach the start of the data - time to read the entire file is file size / data rate
- essentially, latency = time to reach track + time to reach sector
- the ==bandwidth== of a disk depends on disk rotation speed and areal density - in the case of fragmented placement, bandwidth is very much reduced
- ==disks aren't 100% reliable== (at the bit level), and historically used ==CRC== as a block code for error detection, but more recently has used error correction codes (e.g. reed-solomon, LDPC?) to accept and correct faulty bits ([[memory reliability]])
- bad sectors in a disc can be remapped to other parts of the surface which aren't being used

### SSDs
- permanent, non-volatile semiconductor store typically using flash memory
- the main advantages over a magnetic disk is that its robust and quieter (due to no moving parts)
- latency is lower for reading, and randomaccessis permitted
- however, the long term data retention is probably worse on an SSD, and there is a limited number of write operations (which are also already slow for flash memory)
