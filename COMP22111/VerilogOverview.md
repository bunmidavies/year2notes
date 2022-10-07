# Verilog

- This page is made as notes for **Videos 1 - 4** for Week 2 of COMP22111
- A lot of this will be revision from COMP12111 (Year 1), but also introduce things which weren't explained last year

***

## Intro

- When we design a circuit, we're essentially designing a block of logic to perform some function $f()$
- We provide some input signals, and generate some output signals
- This is essentially what a module in verilog does and consists of


***

## Defining Combinatorial Modules

- Modules are defined in verilog using `module modulename` and `endmodule`
- Module inputs and outputs are defined at the start:
  `module example(input wire [3:0] a, input wire [7:0] b, output wire [7:0] c);`
- For behavioural logic / when we are using blocking assignments, we can use `reg` instead of `wire`
- For switch cases, we should always remember to `endcase` and add a `default` case where the output is set to X
- This is such that while testing we can point out any definite issues, or if we don't use all possible options within a switch case
- **We also need to make sure to give all `if` statements an `else` statement**. If this isn't done, a latch is implicitly created to hold the value until the if condition is met, which isn't desired for combinatorial circuits

***

## Designing sequential systems

- The most basic sequential device is a D-type flip-flop
- Basic sequential devices will always have a clock input, and perform operations when the clock goes high/low. Another important input within most sequential devices is a reset wire
- Outputs should be made a `reg` within sequential devices, due to non blocking assignments being used
- `always @ (posedge clock)` is a common thing to see within sequential circuits
- `<=` is **non-blocking**. `=` is **blocking**
- Within sequential circuits **it is okay to omit else statements**, as sequential circuits will typically have latches

***

## Designing a shift register example

- In verilog, you can technically implement complicated designs in fairly easy ways depending on what the specification for the circuit actually is
- For instance: a shift register has quite a complicated schematic, involving a d-type flip flop as well as a multiplexers and decoders for each individual bit, but can be written quite easily using verilog:

```
module shift_reg(input wire        clk, rst, ld,
				 input wire [1:0] m,
				 input wire [7:0] pdata,
				 output reg [7:0] sdata);

always @ (posedge clock)
	if (rst) sdata <= 4'b0000;
	else
		if (ld) sdata <= pdata;
		case (m)
			2'b00: sdata <= sdata;
			2'b01: sdata <= sdata << 1;
			2'b10: sdata <= sdata >> 1;
			default: sdata <= 8'h00;
		endcase
endmodule
```

- Note that because only one operation is being performed within the always blocks/ifelse blocks, separating symbols aren't actually needed

***

## Advanced Verilog features

- **Verilog tasks**: tasks are similar to functions, and can be called within modules. They are created using the `task <taskname>;` and `endtask` keywords
- Inputs/outputs/local variables are defined before the `begin` and `end` keywords which hold actual statements
- To call a task, we write `<task_name>(inputs, outputs);`
- **The task needs to reside within the module in order to be called within that module**

- **Verilog functions**: functions are more or less declared in the same way as tasks, using `function <func_name>;` and `endfunction`
- Functions have inputs and local variables, but **No output variables, other than a single variable which is of the same name as the function**
- Functions are called as such: `a = <func_name>(inputs);`, so as you can see it's different to a task which will assign to the outputs you write within the parentheses

***

## Structural Verilog basics

- Behavioural verilog describes how a circuit behaves (obviously), whereas structural verilog allows you to specify the actual design of circuits using logic gates and other modules in Verilog
- Outputs or variables that serve as inputs for other modules within a certain module need to be defined as a `wire` within the actual module (not at the start)
- **Implicit description** = following the order of inputs/outputs as defined within a certain module, such that if you order your inputs/outputs incorrectly you will receive an error / unexpected results
- **Explicit description** = use of `.parameter`, where `parameter` is the actual parameter within a module, to specify which inputs and outputs you are connecting to the module. This means that you can see where your connections are made, and don't have to follow the order defined within the module

***

## Testing / Testbenches

- Why is testing important? **The smallest of mistakes can have dire consequences**
- The typical regression testing model goes: Working design, modification, rerun existing tests, and check for errors
- A testbench consists of the following
	- DUT - The Design Under Test, the actual module we're testing
	- Test Stimulus - The values we provide to the DUT as inputs
	- Automated testing / waveform verification / terminal results - Any of these are used to verify that our module is working as expected
- Testbenches themselves are defined as modules - `module testbench()`. They do not need any input / output parameters

***

## Stump ALU example testbench

```
module Stump_ALU_test ();
	reg [15:0] operand_A;
	reg [15:0] operand_B;
	reg  [2:0] func;
	reg        c_in;
	reg        csh;
	wire [15:0] result;
	wire [3:0] flags_out;

	Stump_ALU ALU (    .operand_A(operand_A),
					   .operand_B(operand_B),
					   .func(func),
					   .c_in(c_in),
					   .csh(csh),
					   .result(result),
					   .flags_out(flags_out));

	// stimulus code
endmodule

```

we've instantiated a DUT within our testbench here, and provided the interal wires as needed - now we create a simulation, as well as some initial values

```
initial
begin
	func = 000;
	operand_A = 16'h0000;
	operand_B = 16'h0000;
	c_in = 0;
	csh = 0;

	// tests go here

	$finish; // simulation ends
end
```

we can then adjust the values as we like, but we need to make sure we add delays using the `#` symbol. This ensures that we can observe the changes (if no delay is implemented, all operations occur immediately and simultaneously)

```
initial
	operand_A = 16'h0001;
	#20 operand_A = 16'h0002;
	#20 operand_B = 16'h0010;
```

finally, we can write our results using a file handler if we'd like, our have a set of correct outputs we're expecting to see, and compare what our DUT actually returns to these values

***git st