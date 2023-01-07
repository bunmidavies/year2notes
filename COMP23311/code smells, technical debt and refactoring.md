[[COMP23311]] `week 8`

COMP23311 has covered 2 main types of software change up to this point:
- ==Perfective change== i.e. adding features
- ==Corrective change== i.e. bug fixing

There are other types of change which also exist:
- ==Adaptive change==, which involves changing some implementation such that it works in a ==different technical context==
- ==Preventive change== keeps the software specification as was, so the same behaviour is retained, but the implementation has changed somehow - these changes typically ==prevent== future issues

This week mainly covers preventive change. To understand the change better, it's important to understand the 2 main types of requirements within software:
- ==Functional Requirements== (FR): the features a system should implement
- ==Non-functional Requirements== (NFR): quality criteria not related to functionality

Preventive change involves ==no change to any functional requirements== - the observable behaviour of the system ==must stay the same== after the change

The first 3 types of change will typically ==increase the cost== of making future changes (i.e. they become harder to do), meanwhile preventive change will ==reduce the cost== of future changes

However, the first 3 types of change typically ==increase value== of the software, while preventive change may ==reduce the value== of software in the ==short term==

For these reasons, the ==modern approach to code quality embodies== the following:
- keeping costs low by keeping scale of preventive changes small
- using tools to reduce costs/risks
- using a comprehensive test suite to reduce risk
- using knowledge of common patterns to reduce costs and risks

### Code smells
A code smell is a code pattern that may suggest the presence of ==poor code quality==

Examples include:
- methods with too many parameters (primitive obsession is a common example)

### Technical debt
In practice, development teams may face dilemmas - for instance, they may have to deliver to a customer on time by deploying less than perfect code

Technical debt is the idea of introducing poor quality code (i.e. ==code smells==) in order to meet delivery goals. Technical debt is repaid by finding and removing code smells - this is known as ==refactoring==

### Refactoring
Software refactoring is known as a change to code that improves some ==non-functional requirements==, but does not cause functional regression

Refactoring is only safe on ==large projects== with the security of a comprehensive test suite

Examples of refactoring include:
- Renaming a method / class
- Converting a variable to a constant
- Converting a local variable to a field
- Moving a method up to a superclass, or to another class altogether

The software refactoring workflow is as follows:
- ==Run tests==: No tests should be failing initially
- ==Apply refactoring==
- ==Run tests==: No tests should be failing, as before the refactoring


## Week Summary
- Software quality declines over time unless the effort is put in to maintaining it
- Small scale regular quality improvements (e.g. finding and fixing ==code smells==)
- Core skill: refactoring within IDEs