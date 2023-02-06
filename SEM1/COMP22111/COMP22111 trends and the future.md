[[COMP22111]]

==Moore's Law== has held up for over 50 years - this is due to geometrical shrinking every 18-24 months, and companies also 'believing' in Moore's Law as well

However, Moore's Law is expected to stop or slow down around ==2025==

There are a number of limits which affect whether Moore's Law can hold:
- Design / Physical: whether the new designs are needed, and if there is space for more transistors
- Manufacturing process / cost: it needs to be feasible to mass produce, and worth building in terms of cost

During the manufacturing process, certain ==manufacturing variations== can be more likely to occur as transistor size decreases. These main types are:
- ==line-edge roughness==
- ==random dopant fluctuations==
The effects of these variations can reduce transistor drive strength, increase wire resistance

Power dissipation needs to be controlled for 2 main reasons:
- battery life: too much dissipation means bad battery life
- cooling: too much dissipation can mean overheating, damage, unusable device

There are two main types of energy dissipation in [[CMOS]]:
- ==Static==: occurs when the transistors are in a ==steady== state (i.e. on or off). This is essentially ==leakage== within the transistors
- ==Dynamic==: occurs while ==switching== between on and off states

There are a number of different techniques to combat this dissipation:
- ==Clock gating==: turning off the clock signal to unused components in the circuit
- ==Voltage scaling==: lowering power supply, and slowing down the clock
- ==Glitch reduction==: preventing unnecessary switches in the transistors

==Three dimension assembly== has been a proposed solution for increasing computational ==density==. The benefits include:
- ==Smaller space== = lower system cost
- ==Shorter wires== = lower delays and power usage
- ==More connections== = increased bandwidth
- ==Greater flexibility== = can integrate chips from different processes

There are always drawbacks though, and these include:
- ==Increased complexity==, since you're now working in 3 dimensions
- ==More testing problems==
- ==Increased heat dissipation==