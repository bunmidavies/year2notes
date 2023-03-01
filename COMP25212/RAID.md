[[COMP25212]]

RAID originally meant:
- ==Redundant Array of Inexpensive Disks== (or sometimes ==independent disks==)

The issues addressed by RAID are:
- Reliability
- Bandwidth

These issues are basically addressed by using several mechanically independent disk drives, ==virtualised== to look like a single device

### RAID 0
- Increases bandwidth by interleaving data - failure becomes more likely since any one of the drives can fail, but bandwidth is improved since parallel access can take place

### RAID 1
- Increases reliability by using 'mirroring': keeping multiple copies of the same data on different disks, meaning that any working disk can service reads, and cheaper individual disk units can still provide a service despite a fault occuring

### Other types of RAID
- Raid 2,3,4... etc.

### Disk interconnection
- Disks are typically. connected via ==SATA== (Serial AT* Attachment)
- Bus interface, meaning data is carried serially - the bandwidth of SATA is up to 6GB/s (translating to 600MB/s, since each byte takes 10 bit periods)