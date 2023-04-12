[[COMP22111]]

testing as a whole is verified into 3 main parts:
1. verification - have you made what you intended to make?
2. validation - have you made something that fulfills the requirements?
3. testing - does what you made work? (**hardware only**)

## verification

VLSI verification - verification is done **before silicon development**, in order to check quality and fix any bugs. There are different types of verification, examples being:
- IP verification
- RTL verification
- timing verification

The main goal of verification is to prove some logic works as intended with as *little effort as necessary*. This can be done using [[simulation]] like we have done in the labs

## testing / validation

VLSI testing (validation - testing is done **at silicon level** to validate the quality of silicon. Any bugs found at this point means the silicon has to be recycled, which can be expensive

**by nature, some chips made with silicon will just be faulty by chance** - the percentage of chips that **do** work is known as the 'yield'. This should be expected to be around 80%+. Chips with a bigger area are more likely to be faulty
![](https://i.imgur.com/J9vm2BC.png)

in this picture, the big circle is a silicon wafer, and each square within the grids are individual chips

[[types of testing]] mentions more on the testing involved on chips