[[COMP23311]] `week 9`

Good software design is rooted by the idea of code being ==easy and safe to change==

Another idea which is somewhat controversial within the software community is the idea that ==code which is easy to test, is easy and safe to change==

Testability is a ==non-functional requirement== (explained in [[code smells, technical debt and refactoring]]), and we say ==testable code== is easy to put under test

==Design for Testability== is making sure that we can easily test what we build, by letting the need for testability ==drive the design== of production code

However, there are a number of situations where code can be difficult to test, or in other words is stopped from being ==testable==:
- Non-deterministic code (i.e. random behaviour)
- Hard-coding / hiding behaviour inappropriately 
- Static code / Constructors, which prevent inheritance
- Complex configuration requirements (i.e. having to access a database to test)
- Breaking the Law of Demeter (i.e. accessing objects through method chains)

A ==test double== is a version of a production code object which has predictable/controllable behaviour, which can be used when we faces problems to do with code not being testable

There are 4 types of test double:
- ==Dummies== - the simplest kind of test double. They're used when an object needs to be passed around in some method, but never actually used. The dummy basically just exists to ==fill parameter lists==
- ==Stubs== - similar to dummies, but we are able to hard code simple return values into the object's methods, removing randomness and unpredictability from it
  stubs in stendhal typically use ==anonymous subclasses== to define the behaviour they want for certain objects
  ![Uploading file...sh8wv]()

- ==Fakes== - doubles with working implementations, but some shortcuts are taken in comparison to the production object (e.g. a database object which actually just uses an in memory db rather than connecting to some real db)
- ==Mock objects== - test doubles created ==on the fly== with behaviour that matches the production object. Certain values can be controlled, and mocks can verify that certain behaviours occur