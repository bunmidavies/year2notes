[[COMP22111]]

the LUMP processor stands for ==Limited Use Made-up Processor==

it is an extension beyond the MU0, and is a 16-bit RISC architecture (like STUMP)

it has ==3 buses== - 16 bit address bus to memory, 16 bit data_in and 16 bit data_out
![](https://i.imgur.com/U3NQXu4.png)


LUMP has 8 registers like Stump, however, unlike Stump it has a ==separate PC register== - this means that R7 is unused in LUMP

LUMP does ==not use the ALU for PC incrementing== it has its own "add1" logic block

there are ==2 types of instruction== within LUMP - branch, and non branch:
![](https://i.imgur.com/xphEHGk.png)


more is available within [[LumpOverview.pdf]]