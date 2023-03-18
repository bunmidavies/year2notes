[[COMP23311]] `week 12`

### What is a software architecture pattern?

Software architecture patterns are very similar to [[software design patterns]]
Instead of being a ==design solution==, architecture patterns are ==system-level patterns== and provide a system layout/application framework for some software

There are 5 common software architecture patterns covered by COMP23311

### <span style="background-color:#ca8ed4;padding:3px;border-radius:5px;">Layered Architecture Pattern</span>

The ==number of layers== in a layered architecture pattern isn't fixed

The ==typical layers== include:
- presentation layer: responsible for user interaction
- application layer: handles functional requirements
- domain layer: responsible for algorithms/underlying programming components
- persistent database layer: responsible for handling any stored data

==Typical applications== include:
- General desktop applications
- E-commerce
- Enterprise/business apps

### <span style="background-color:#9ea360;padding:3px;border-radius:5px;">Client-Server Architecture Pattern</span>

Client-server architectures consist of a central computer server, connected to one or more client computers over a network

==Typical applications== include:
- Email service providers
- File-sharing services
- Online banking
- Online games

### <span style="background-color:#615643;padding:3px;border-radius:5px;">Peer-to-Peer (P2P) Architecture Pattern</span>

In a P2P pattern, each system acts as both a client and server

==Typical applications== include:
- File sharing
- Instant messaging
- Voice communication
- Blockchain apps
- Collaboration software


### <span style="background-color:#456143;padding:3px;border-radius:5px;">Publish-Subscribe (Pub/Sub) Architecture Pattern</span>

Also known as a ==messaging pattern==, publishers categorise published messages into classes, without knowledge of who is actually 'subscribed' to them

Subscribers express interest in 1+ classes of messages, and only receive messages that are of interest, without knowledge of the publishers

![](https://i.imgur.com/5K6skA4.png)


==Typical applications== include:
- asynchronous messaging within ==message-oriented middleware== systems

Example: [Google Cloud Pub/Sub Messaging Service](https://cloud.google.com/pubsub/)

### <span style="background-color:#634144;padding:3px;border-radius:5px;">Model-View-Controller (MVC) Architecture Pattern</span>

The MVC pattern clearly separates ==business logic==, ==UI logic== and ==input logic==

![](https://i.imgur.com/cP4xbJf.png)


- ==Model== = the backend containing core functionality, business data and state of the application
- ==View== = the frontend / UI, which displays app data and supports user interaction
- ==Controller== = the brains of the application which controls how data is displayed

Note that an application can have ==multiple views and controllers==

A common ==variant of MVC== is ==Spring MVC - A Java framework for web apps==
It has an MVC architecture but also implements all core features of a core spring framework
![](https://i.imgur.com/OxxRLxU.png)


==Typical applications==:
- Web apps
- Javascript applications
- Desktop GUI interfaces
- Libraries for programming languages