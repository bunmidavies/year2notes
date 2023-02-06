[[COMP22111]]

==CMOS = Complimentary Metal Oxide Semiconductors==

[[CMOS circuit technical issues]]

COMP22111 doesn't look at the underlying physics of electronic circuits, but some basic knowledge is required to understand CMOS and how MOSFET is used - [[voltage, current and resistance]]

n[[MOS]] and p[[MOS]] transistors have different characteristics which can be combied to form logic gates which ==work efficiently== when passing a 0 or 1

CMOS circuits consist of:
- ==pull-up network== - a network of pMOS transistors
- ==pull-down network== - a network of nMOS transistors
- pull-up network being connected to the power supply
- pull-down network being connected to the ground

if both the pull-up and pull-down network are on, the output is $X$ - indicating this is an invalid condition

the pMOS pull-up network implements the required logic function - so when ==the logic gate is true==, this network switches on, connecting the output signal to the power

the nMOS network just does the opposite, for when the logic gate is ==false==

saying the logic gate is true/false just refers to whether the signals actually result in the logic gate returning true - i.e. are both signals 1 for AND

the output of CMOS circuits are where ==the pull-up and pull-down network join==

different CMOS circuits include:
- the inverter - explained within [[MOS]]
- ==NAND== gate - two pMOS transistors ==in parallel== for the pullup, connected with two nMOS transistors ==in series== for the pulldown
- ==NOR== gate - two pMOS transistors ==in series== for the pullup, connected with two nMOS transistors ==in parallel== for the pulldown

therefore, an ==AND== gate is simply implemented with a ==NAND + inverter==