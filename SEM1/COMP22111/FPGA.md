[[COMP22111]]

==Field Programmable Gate Arrays==

FPGAs can be seen as a target technology, or as a processing device. They can be reprogrammed in order to hold any kind of logic circuit (as long as it is within capacity)

FPGAs work by using look-up tables as the basic building block. Instead of having the actual logic being stored within the circuits, you have the outputs corresponding to certain inputs stored within a table

==Look-up table (LUT) - a means of translating an input pattern into an output pattern. For combinatorial logic, this is essentially a truth table==

The main ==advantage== of look up tables is that it is convenient, and the access time for **any** input will be constant, as they're all in the same table

The main ==disadvantage== of look up tables is that it scales badly - think of how for a truth table, you need $2^n$ rows given $n$ inputs. Multipliers, RAM blocks etc would be very difficult/expensive to implement with LUTs

FPGAs are then built up using LUTs, switch matrices and I/O cells

The main comparisons that can be made for FPGAs against [[ASIC]]s include:
- 18x in area
- 3-4x slower than ASIC
- 5-10x more power used than ASIC
- FPGA is mass produced, making it typically cheaper than ASIC
- Uses less power than ASIC, making it have a reasonable power/performance

[[CPU vs GPU vs FPGA]] talks more about when an FPGA would be suitable over a CPU or GPU