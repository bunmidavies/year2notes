[[COMP23311]]`week 2`

A unit test is an automated test which verifies a ==small piece of code== in an ==isolated== manner

The ==AAA== pattern is an approach which is used for writing unit tests:
- ==Arrange== = set up the objects to be tested (this is the System Under Test / SUT), and assign the required state to these objects
- ==Act== = any code that needs to be tested is now invoked - the output from this code should be captured / saved
- ==Assert== = the output from the code should now be verified, meaning you should check if the output is as expected

The AAA pattern should go in the order as above, and the Arrange section should be the longest. Typically, unit tests should be ==annotated== and ==avoid branching== i.e. no `if` statements 

In COMP23311 we write JUnit tests - [[JUnit Cheatsheet]]