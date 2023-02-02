[[COMP25212]]

the 'byte' is usually the smallest addressable unit

==word size varies==. It typically refers to the natural data size in an architecture - but most typically a word is ==32 bits (4 bytes)==
*(Hence halfword = 16 bits, doubleword = 64 bits etc.)*

a [[bus]] will have a particular width (i.e. 32 bits, 64 bits) - we can describe operations as being ==aligned== or ==misaligned== depending on which data is being operated on

misaligned operations will be slower than aligned operations (and can malfunction)