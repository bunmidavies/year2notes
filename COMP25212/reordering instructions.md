[[COMP25212]]

### compiler reordering + VLIW
- reordering can be performed by the compiler - in the cases when the compiler fails to reorder instructions, there still needs to be hardware to avoid issuing conflicts (hardware must stall)
- by relying on the compiler, expensive checking logic can be removed from hardware
- the principle of ==Very Long Instruction Words (VLIW)== is that the compiler reorders instructions, and adds NOPs where necessary
- however, there are limitations to the compiler handling reordering:
	- ==legacy binaries== - optimum code tied to certain hardware configurations
	- ==code bloat== - in VLIW, useless NOPs may have to be added
- instead of always having to rely on the compiler to reorder instructions, we can rely on hardware to do so if necessary - this is the purpose of [[out of order processors]]