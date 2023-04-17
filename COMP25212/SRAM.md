[[COMP25212]]

### ~ characteristics
SRAM = static, volatile ram
- SRAM is good for ==genuine random access==, and fairly ==fuss free==
- quite compact
- low power (especially when not in use)
- volatile - retains data (only) whilst powered
- manufacturable on logic chips, meaning it can be made alongside processor chips
- multi-port SRAM is also possible, but not worth it - FPGAs already provide the same thing

### ~ applications
SRAM has multiple applications, and is used extensively today:
- working RAM in small processor systems (microcontrollers)
- cache memories in big processor systems
- buffer memories in interfaces (e.g. USB, ethernet)
- temporary storage in hardware FSMs
its pretty expensive which is why you wouldnt often find it as the main RAM component

==SRAM is a standard architectural component== - in COMP25212 we mainly only really care about the external properties of the memory - there are certain design decisions taken within the logic gate implementation of SRAM in order to save space

