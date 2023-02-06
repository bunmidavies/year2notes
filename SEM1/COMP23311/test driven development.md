[[COMP23311]] `week 5`

In an ==agile methodology==, multiple iterations take place, all taking the form of Design, Build and Test. These are designed to fail fast, and allow for quicker feedback

There are 5 main steps in the Test Driven Development process:
1. ==Decide Behaviour== - what behaviour should the program exhibit?
2. ==Write Tests== - Ensure tests compile, and use "wishful thinking" (imagine how you'd like to use the code) or "the perfect API"
3. ==Run Tests== - All tests should ==fail initially==
4. ==Write Code== - You should be writing the ==minimum amount of code== to pass the tests, and continue to make refinements until all tests pass
5. ==Refactor== - When all the tests pass, the program can be refactored if the design needs improving

[[unit tests]] test specific units of code, so these ==must pass==
meanwhile ==acceptance tests== are customer centric, and are OK to fail if the related parts haven't been implemented yet