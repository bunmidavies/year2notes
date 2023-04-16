[[COMP25212]]

### ~ bytes
- the 'byte' is usually the smallest ==addressable== unit
- quite stably defined as 8 bits

### ~ words
- ==word size varies== - it typically refers to the natural data size in an architecture
- its becoming increasingly common that a word is ==32 bits (4 bytes)==
- halfword = $0.5 \times$ word size, doubleword = $2\times$ word size

### ~ alignment
- since buses have particular widths, data transfers will follow these widths
- alignment (typically along word sizes) is important since misaligned operations can malfunction be much slower than an aligned operation
- in some processor architectures, code alignment may be ==enforced== - for instance, RISC has fixed length instructions
- meanwhile for other ISAs, there are variable length operations e.g. x86 - this makes alignment impossible in some scenarios