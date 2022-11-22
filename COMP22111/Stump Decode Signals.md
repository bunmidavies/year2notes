<span style="color:purple">
- fetch <br>
- execute <br>
- memory <br>
</span>
reg_write - whether to write to dest[2:0]
dest[2:0] - the destination register from ALU operation

shift_op[1:0] - set to 0 when you just want data to pass through

opB_mux_sel - whether to pick IR or regB for second ALU operand

mem_rd - set to 1 for fetch because we're reading from memory
mem_wr - set to 0 for fetch because we're not writing to memory

use Testbranch to determine whether a branch should be taken or not

