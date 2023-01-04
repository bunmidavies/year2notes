# Stump

- This page is made as notes for ==**Video 3**== and ==**Video 4**== for ==Week 1== of COMP22111
- Stump has an ARM like ISA, but just simpler in design
- It's important to understand Stump for the labs

***
## The design of Stump

- Stump is a 16 bit processor, therefore has a 16 bit address bus and a 16 bit data bus

- The processor itself has the following internal registers:
	- IR = Instruction Register
	- Register Bank (R0 - R7)
	- R7 = PC (Program Counter)
	- R0 is always 0 (If you write to R0, **nothing happens**) - This is to allow the implementation of further instructions (e.g. ADD R2,R1,R0 works like a MOV instruction)

- Within the memory of the processor:
	- Each memory location comprises of 16 bits (to store data / instructions)
	- Each location is uniquely identified with a 16 bit address
	- 16 bit address = $2^{16}$ unique memory locations

- The instruction format for Stump is as follows (Bits 15 - 0):
	- Bits 15 - 13: Opcode. Specifying one of **8 possible instructions**
	- Bits 12 - 11: ?
	- Bits 10 - 0: Defines the instructions

- There are **3 types of instruction within Stump**:
	1. Two source registers
	2. One source register, one immediate value
	3. Branch instructions

***

## Addressing within Stump

- The following addressing types are used within Stump:
	- Immediate Addressing - Opcode + Operand (used directly in operation)
	- Register Addressing - Opcode + Register (value within register is used)
	- Register **indirect** Addressing - Opcode + Register (register holds address of value **in memory** to be used)
	- Immediate Offset Addressing - Opcode + Reg + Offset (Offset is added to address stored within register. So like indirect but with an offset)
	
	- Register Offset Addressing - Opcode + Reg1 + Reg2 (One register holds address, one register holds offset)
	  This would be written as `ST R4, [R2, R5]`, thus R4 is storing the value within memory address R2 + R5
	
	- PC Offset Addressing - Opcode + Offset (PC = PC + Offset)

***

## Instructions within Stump

- All maths within Stump is done with **2's complement**
- There are 8 different instructions within Stump, thus 3 bits being required to specify

- Type 1 instructions within Stump take the following format:
	- <span style="color:#5f9fb8">Bits 15 - 13: Instruction Code</span>
	- <span style="color:#bdbb44">Bit 12: 0 = Type 1 instruction. 1 = Type 2 instruction</span>
	- <span style="color:#bdbb44">Bit 11: Used within Load/Store operations, or to indicate updating of condition code</span>
	- <span style="color:#5bc25f">Bits 10 - 8: Destination register</span>
	- <span style="color:#5bc25f">Bits 7 - 5: Register A</span>
	- <span style="color:#5bc25f">Bits 4 - 2: Register B</span>
	- <span style="color:#e33b54">Bits 1 - 0: Shift parameter, used for Type 1 instructions, and applied to Register A</span>

- If the instruction is LDST (LoadStore). 
	- **STCC** = 1 if ST
	- **STCC** = 0 if LD
- **STCC** is bit 11 in the 16 bit instruction (i.e. the 12th but we start with 0th)

- If the instruction **is not LDST**
	- **STCC** = 1 if flags are to be updated
	- **STCC** = 0 if flags are not to be updated

- Type 2 instructions will have **Bit 12 set to 1**. Type 2 instructions use an immediate value (represented with 2's complement), using bits 4 - 0
	- <span style="color:#5f9fb8">Bits 15 - 13: Instruction Code</span>
	- <span style="color:#bdbb44">Bit 12: 0 = Type 1 instruction. 1 = Type 2 instruction</span>
	- <span style="color:#bdbb44">Bit 11: Used within Load/Store operations, or to indicate updating of condition code</span>
	- <span style="color:#5bc25f">Bits 10 - 8: Destination register</span>
	- <span style="color:#5bc25f">Bits 7 - 5: Register A</span>
	- <span style="color:#e33b54">Bits 4 - 0: Immediate value, stored in 2's complement</span>

***

## Shift operations in Stump instructions

- The shift operations (Bits 1 - 0) are as follows:
	- 00 = **No Shift**
	- 01 = **Arithmetic Shift Right** (Sign bit is copied to MSB)
	- 10 = **Clockwise Circular Shift** (Previous bit 0 is copied to MSB)
	- 11 = **Clockwise Circular Shift + Carry** (Carry is copied to MSB)

***

## Stump's condition code register

- If the instruction isn't LDST (Load or Store), then Bit 11 within the instruction is used to identify whether the condition codes will be updated.
- Within the actual instruction itself, the letter 'S' will be added onto the end i.e. ADDS, SUBS
- Bit 11 = 1 means **update condition code register**

- The Condition Code Register (CC) has 4 flags, each stored in a single bit
	- CC[3] = N - Negative flag. If result = Negative, CC[3] = 1
	- CC[2] = Z - Zero flag. If result = 0, CC[2] = 1
	- CC[1] = V - oVerflow flag. If overflow condition is met, CC[1] = 1
	- CC[0] = C - Carry flag. If a carry is generated, CC[0] = 1

***

## Stump's ALU

- Stump Inputs:
	- two input operands - Operand_A[15:0], Operand_B[15:0]
	- the carry from the CC register (c_in), and the carry from the shifter (csh)
	- func[2:0], the 3 bit instruction code

- Stump Outputs:
	- result[15:0] - Result of the operation
	- flags_out[3:0] - The values to be stored in CC register if the flag was set

- The ALU instructions are as follows:
	- **ADD** - result = operand_A + operand_B
	  N flag is set if bit 15 == 1
	  Z flag is set if result == 0
	  V flag is set if **MSB != Carry out bit**, or by looking at the **signs of the operands** (below)
	  C flag is set if carry is generated
	  
	- **ADC** - result = operand_A + operand_B + c_in
	  Flags are generated in same manner as **ADD**
	  
	- **SUB** - result = operand_A - operand_B
	  All flags other than C are generated in same manner as **ADD**
	  C flag is **the inverse of the carry generated**

	- **SBC** - result = operand_A + inverse of operand_B + inverse of c_in
	  All flags are generated in the same manner as **SUB**

	- **AND** - result = bitwise AND of operand_A and operand_B
	  N and Z flags are set as usual
	  V flag is never asserted
	  C flag should be set to csh (shift carry)

	- **LDST / Bcc** - result = ADD operation
	  Flags are never set for these instructions
	  (The flags must be set to something for these operations within the combinatorial logic, but they just have to not change)

- **Determining if ADD has resulted in overflow**
|      | +ive  | -ive  |
|------|-------|-------|
| +ive | check | v=0   |
| -ive | v=0   | check |

- The following table can be used to check whether the overflow flag needs to be set, where the columns represent operand_A and rows represent operand_B (or vice versa)
- In the cells which say 'check', the check required is that the result of the operation has the same sign as both the operands. If +ive + +ive has resulted in a negative value, or -ive + -ive has resulted in a positive value, you know an overflow must have occured

- **Determining if SUB has resulted in overflow**
|      | +ive  | -ive  |
|------|-------|-------|
| +ive | v=0 | check  |
| -ive | check  | v=0 |

- The following table can be used to check whether the overflow flag needs to be set, where the columns represent operand_A and rows represent operand_B (or vice versa)
- In the cells which say 'check', the check required is that the result of the operation has the same sign as the **value being subtracted from**. If +ive - -ive results in -ive, an overflow has occured, and vice versa if -ive - +ive results in +ive, an overflow has occured
