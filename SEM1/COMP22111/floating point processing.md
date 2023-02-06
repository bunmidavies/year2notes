[[COMP22111]]

==floating point is needed to represent very large / small values (with accuracy) in a hardware efficient way (i.e. not using a huge number of bits)==

floating point is the solution to fixed point, where instead of having a fixed window of possible values you can represent, you specify the window with an exponent

in order for a floating point value to be normalised, the decimal point should be as close as possible such that shifting it one more will change the value being represented - [[normalised floating point form]]

many processors support floating point arithmetic, where a floating point value is represented by a word-load of bits, with different fields to represent different components of the value (depending on how you choose to interpret the bits)

==IEEE754== is the 32-bit standard format for floating point values. Used in the most common processors today

for most values there are 3 typical fields:
- ==sign== - 0 or 1, where 0 = positive, 1 = negative
- ==exponent== - the position of the binary point in the number
- ==mantissa/significant== - unsigned value

note that if the number is normalised, the point from which you start moving the decimal point is between the msb and 2nd msb e.g.
1 **.** 0100 if we had a 5 bit mantissa

#### multiplication
in order to perform floating point multiplication, you ==multiply the mantissas, and add the exponents== (while watching out for over/underflows)

#### division
the same as multiplication, except the exponents are ==subtracted== instead 

#### addition / subtraction
mantissa of the smaller value is shifted right until the exponents are equal
then the mantissas are added or subtracted