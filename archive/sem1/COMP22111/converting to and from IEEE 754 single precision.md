[[COMP22111]]

there are 3 main types of IEEE 754 floating point formats:
- ==half precision== - 16 bits
- ==single precision== - 32 bits
- ==double precision== - 32 bits

COMP22111 is mainly focused on single precision, i.e. representing floating point values with 32 bits

### decimal to single precision

example: 45.45

the first step is to identify the sign. Since 45.45 is a positive number, the sign is ==0==

(0)(exponent)(mantissa)

the next step is to obtain the mantissa, which can be split into two parts
==obtaining 45==
45 = 32 + 8 + 4 + 1 so 45 = 101101 (do this with whatever method you want)

==obtaining 0.45==
the method to obtain the decimal part of a floating point number is different as in some cases, floating point can only be so accurate by recurring. The method is:
```
0.45 x 2 = 0.9
0.9  x 2 = 1.8
0.8  x 2 = 1.6
0.6  x 2 = 1.2
0.2  x 2 = 0.4
0.4  x 2 = 0.8
loop reached
```
it helps to keep the calculations in line so that you can extract the binary number at the end, 011100, where the ==1100== at the end is recurring, due to the loop (you always stop before you start a calculation you've done before)

so our full mantissa for 45.45 is:
$101101.01\overline{1100}$
where the point is the separator between integer and decimal

==obtaining exponent==
we have to shift our decimal point to the first 1 in our number, so we obtain
$1.0110101\overline{1100}$
after ==5== shifts, so our exponent is 5

in single precision, 8 bits are used to represent the exponent - in order to give a range of negative and positive numbers, there is an automatic ==exponent bias== applied to the values, of -127.

this means, whatever exponent we get by moving the decimal place, we want to ==add 127== so that the offset doesn't mess up the value we want

so we want to represent ==127 + 5 = 132== in binary
128 + 4 = 10000100

==piecing together sign bit, exponent and mantissa==

we have the sign bit, exponent and mantissa
the sign bit goes first:
$0$

followed by the exponent:
$010000100$

followed by the mantissa - ==the 1 to the left of the decimal point is REMOVED== i.e. you just take whats to the right of the decimal point
$01000010001101011100$

however, single precision requires ==32 bits==, and at this point we only have 20 - in order to fix this, we pad the mantissa. However, as we have a ==recurring== binary value for our mantissa, instead of just padding with 0s, we pad with the recurring part:

therefore, our ==final value== is:
$01000010001101011100110011001100$

![](https://i.imgur.com/cJIcrVe.png)


as can be seen, we gain the closest possible approximation given 32 bits
***
### single precision to decimal

example: convert $10001000100010001000000000000000$ to decimal in the format:
$1. ...\times 2^e$ 

the first step is to break the binary number down into the sign, exponent and mantissa

for single precision remember that:
- sign = 1 bit
- exponent = 8 bit
- mantissa = 23 bit
which all add up to 32 bits

sign = $1$
exponent = $00010001$
mantissa = $00010001000000000000000$

since our sign is 1, we know our number is negative

our expoonent gives a value of 17, but as we know we apply a ==bias== to the exponent, we subtract 127 and our actual exponent is -110

we convert the mantissa by the following idea: the first 0 represents $0 * 2^{-1}$, the second 0 represents $0 * 2^{-2}$, etc.

therefore, we have $1 * 2^{-4} + 1 * 2^{-8}$, which is equal to 0.06640625

since we know we always remove the first 1 before the decimal point when representing our mantissa, we add a 1 to this value:

1.06640625

now the final part is to put the correct sign and add the exponent:

$$-1.06640625 * 2^{-110}$$
![](https://i.imgur.com/digTsXR.png)


due to floating point accuracy this is as accurate as we can get to the value we want:
![](https://i.imgur.com/DjtA7sb.png)
