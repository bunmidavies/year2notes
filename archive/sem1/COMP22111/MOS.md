[[COMP22111]]

there are two main types of MOS transistor:
- ==nMOS==
- ==pMOS==

![](https://i.imgur.com/RhtikN3.png)

![](https://i.imgur.com/DFcb8Bp.png)


they are different in the way that they are fabricated, and what they do when a voltage is applied to their ==gate input== (below)

within a MOS transistor there are two main states - ==conducting/on==, or ==high impedance/off==

there are 3 terminal devices within both types of MOS:
- ==gate input== G
- ==drain== D
- ==source== S
the source and drain are referred to as the ==channel==, as current flows through it

for the nMOS transistor, there is a ==threshold voltage==, such that current will readily flow from the drain to source, switching on whatever device the transistor is connected to

the connection between the drain and source can be seen as a ==switch==
when a '1' is applied to the gate of an nMOS transistor, the channel becomes conducting, so the switch is ==closed==
if a '0' is applied, the channel is non-conducting, so the switch is open - this is the ==high impedance== state

the ==pMOS transistor== works ==opposite to the nMOS==
when a '0' is applied, the channel is conducting, so current flows between the drain and source. when a '1' is applied, the channel is non-conducting/high impedance

the other important difference is that the ==nMOS== charge carriers are ==negative electrons==, while the ==pMOS== charge carriers are ==positive holes==

the nMOS transistor is not very good for transmitting a '1', but is very good at transmitting a '0'. it is vice versa for the pMOS. a '1' or '0' is transmitted by providing the corresponding signal to the gate terminal, and this whole paragraph refers to the ability for the transistors to submit ==digital== 1s/0s

the notes cover ==two main applications== using nMOS and pMOS combined:
- ==transmission gate== by connecting nMOS and pMOS transistors in parallel, the gates from both transistors are used, but there is just one drain/source. The transmission gate solves the 'weak' transmission problem
- ==2-1 mux== - using the transmission gate, a 2-to-1 mux can be implemented. 2 transmission gates are combined with a ==NOT gate==, such that a signal $s$ can control which transmission gate will be conducting

[[CMOS]] circuits are made up of pMOS and nMOS transistors