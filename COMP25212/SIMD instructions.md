[[COMP25212]]

### ~ definition
- SIMD = ==Single Instruction Multiple Data==
- essentially, ==vectors of operands== are processed by the same instruction, in parallel with minimal additional overhead
- modern CPUs / GPUs commonly use SIMD instructions, in order to increase parallelism, ultimately improving bandwidth
- ==SIMD instruction sets== e.g. MMX, AVX, AVX2, SSE, are ==instruction set extensions==, which are basically built on top of the existing assembly instruction set in a processor, and provide SIMD instructions to be used
![](https://i.imgur.com/TlARimQ.png)

### ~ MMX
- MMX was one of the original SIMD instruction sets, introduced in the late 90s to improve parallelism within multimedia / graphics applications
- MMX is technically officially a meaningless acronym - it's unofficially been said to stand for:
	- MultiMedia eXtension
	- Multiple Math eXtension
	- Matrix Math eXtension
- MMX provides 8, 64-bit wide registers, and only provides integer operations

### ~ SSE
- on intel processors, MMX has essentially been superseded by SSE - ==Streaming SIMD Extensions== - it became much more popular than MMX due to supporting floating point operations, thus having wider application
- SSE provides 8 128-bit ==XMM registers==, each of which can hold four 32-bit (single-precision) floating point numbers
- The XMM registers can be accessed directly through assembly code, and the 70 instructions SSE provides are used to take advantage of data parallelism where possible
- newer versions of SSE have come along, with SSE4.2 being used in many processors today

### ~ AVX/AVX2
- AVX, also created by intel, stands for ==Advanced Vector eXtensions==, and provide new instructions for processors from both Intel and AMD - AVX was proposed by intel in 2008
- AVX uses 16 256-bit ==YMM registers==, allowing maths on eight 32-bit floating point numbers, or four 64-bit floating point numbers, i.e. single precision and double precision
- AVX2 provides some extra functionality, e.g. fused multiply-add, support for 256-bit integer instructions, gather instructions (loading vector elements from non contiguous memory locations)

### ~ XMM vs YMM registers
- XMM and YMM registers mentioned above, are both SIMD registers which allow for parallel processing of data
- the main difference is that ==YMM registers are twice as wide as XMM registers== - XMM registers are 128 bits wide, while YMM registers are 256 bits wide
- instructions involving XMM registers can use the lower half of a YMM register, such that the upper half of the YMM register is unused, and can be used independently of the current XMM instruction 

### ~ links
- [MMX](https://en.wikipedia.org/wiki/MMX_(instruction_set))
- [Streaming SIMD Extensions (SSE)](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions)
- [Advanced Vector Extensions (AVX)](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)
- [xmm and ymm (stack overflow)](https://stackoverflow.com/questions/48139513/asm-x86-64-avx-xmm-and-ymm-registers-differences)