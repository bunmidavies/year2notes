[[COMP23311]] `week 10`

The Origin of Design Patterns (for Software) is often referred to as the ==Gang of Four (GoF) book==. 23 design patterns for object-oritented software design/development were introduced within this book, with each of them being described by a standard form.

### What is a design pattern?

*A design pattern is a ==reusable design solution== to a recurring design problem in a specific design context*

It can be described as ==distilled wisdom== for OOP programming. They support us in 2 ways:
- They allow solutions that have worked in the past to be ==reused==
- They provide a ==shared vocabulary== for talking about software design

==Experience is reused, rather than code==

Note that design patterns can also be ==overused== - it can be useful to refactor ==towards== a pattern, but under/overengineering a system should be avoided

### Design pattern categories

There are 3 main categories for the design patterns:
- ==Creational== - patterns concerned with the ==process== of object creation, providing solutiuons to instantiate objects in the most suitable way
- ==Structural== - patterns concerned with the ==composition== of classes/objects e.g. how classes/objects can be composed to form larger objects
- ==Behavioural== - patterns concerned with the way classes ==interact==, and the responsibilities they adopt e.g. how they communicate, how behaviour is distributed, how tightly objects are coupled

COMP23311 covers ==2 patterns from each of the 3 categories==


### <span style="background-color:#797ca3;padding:3px;border-radius:5px;">Behavioural</span> - Strategy

Intent: *"Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it."*

- A strategy pattern means creating a ==set of objects== that hold alternate algorithms to solve a problem
- Refactoring to the strategy pattern involves pulling out the algorithm from some class that contains it, and encapsulating the ==algorithm itself== as an object
- ==Algorithm = strategy==

![](https://i.imgur.com/nkJbM9I.png)


### <span style="background-color:#797ca3;padding:3px;border-radius:5px;">Behavioural</span> - State

Intent: *"Allow an object to alter its behaviour when its internal state changes. The object will appear to change its class"*

- State is similar to strategy, in which you create a ==set of objects== which hold alternate algorithms - for state, a different algorithm will be selected based on the current internal state of a containing object
- Refactoring to the state pattern involves ==replacing conditionals== within class methods with smaller classes sharing simpler versions of the methods

![](https://i.imgur.com/HoR0gBu.png)


### <span style="background-color:#c78da5;padding:3px;border-radius:5px;">Structural</span> - Composite

Intent: *"Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly"*

- Implementing a composite pattern involves creating a common base class to represent ==part of an object==, and the ==containing object as a whole==
- When data/code forms an ==implicit tree structure==, you should consider refactoring to composite

### <span style="background-color:#c78da5;padding:3px;border-radius:5px;">Structural</span> - Adapter

Intent: *"Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces"*

- Implementing an adapter patterns involves creating a ==wrapper class==, which can transform an incoming request for a piece of functionality into a format accepted by the code that can provide that functionality
- An adpater can be useful when working with ==legacy code== that can't be changed at the time 
![](https://i.imgur.com/3SRwc7z.png)

In this example the interfaces between ==target== and ==adaptee== are incompatible, and adaptee has a function which the target wants to use. The adapter allows adaptee's functionality to be implemented, and returns the output wanted by target in a compatible format

### <span style="background-color:#bfbc67;padding:3px;border-radius:5px;">Creational</span> - Factory Method

Intent: *"Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory method lets a class defer instantiation to subclasses"*

- The factory pattern means you ==create a class whose job is to create objects== - the object type is determined based on parameters passed at runtime
- The factory method can be useful when working with lots of subclasses which have a ==common base class==

### <span style="background-color:#bfbc67;padding:3px;border-radius:5px;">Creational</span> - Singleton

Intent: *"Ensure a class only has one instance, and provide a global point of access to it"*

- Implementing the singleton pattern means creating a class whose constructor ==can't be called in the usual way== - all calls to create a new object return to the same instance
- Refactoring away from a singleton pattern can be as valid as refactoring to one
- Example: there might only be one accounting system for a company - trying to instantiate a new one should return the already existing system
![](https://i.imgur.com/4cGPJ02.png)
