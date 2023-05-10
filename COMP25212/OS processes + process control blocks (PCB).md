[[COMP25212]]

### definition
- processes within an OS can have a number of different states, and typically will jump between these states
- a process control block / PCB stores info related to the state of an 'alive' process being handled by the operating system ([[software multithreading]])

a range of information is stored within these blocks:
- process ID
- process state
- PC
- stack pointer
- general registers
- memory management info
- open file list with positions
- network connections
- CPU time used
- parent process ID