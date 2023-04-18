[[COMP25212]]

### ~ definition
- RAID originally meant:
	- ==Redundant Array of Inexpensive Disks== (or sometimes ==independent disks==)
- the aim of RAID was to improve ==reliability== within some secondary storage system, by using redundancy for ==fault tolerance==, using cheaper parts 
- for instance, how a plane may have multiple engines (for multiple reasons, safety being one of them)

These issues are basically addressed by using several mechanically independent disk drives, ==virtualised== to look like a single device

### RAID 0
- increases bandwidth by interleaving data - ==striping==
- parallel access can potentially be implemented
- ==not redundant== - since each disk doesnt hold all the data, any disk breaking is critical

### RAID 1
- increases reliability by ==mirroring==
- multiple disks hold the same data, and any working disk can service reads
- for single requests, performance is not affected, and a higher bandwidth can be provided for simultaneous reads

### other types of RAID / nested RAID
- RAID 2,3,4... etc.
- RAID can also be nested, for instance RAID01 being a RAID1 array of RAID0 systems, or RAID10 being a RAID0 array of RAID1 systems

### disk interconnection
- disks are typically. connected via ==SATA== (Serial Advanced Technology Attachment)
- SATA is a bus interface, which carries data serially - it currently has up to 6 Gb/s bandwidth (about 600MB/s - for reference disk platters have about 100MB/s)