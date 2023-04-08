[[COMP26020]]

### ~ definition
- inter-process messaging is a method of ==inter-process communication (IPC)== - data/messages are exchanged between different processes running in an operating system
- channels abstract the underlying implementation, allowing processes to have connections between each other - examples of channels include:
	- shared memory objects
	- network sockets
	- unix sockets
- there are ==3 main approaches== to inter-process messaging, offering different factors like flexibility, scalability, performance etc

### ~ remote procedure calls (RPC)
- the simplest approach to inter-process messaging, where a sender process sends a message, then ==waits== for a receiver to ==reply==
- with RPC, the sender process can call a function from another process as if it is its own function
- since RPC sender processes wait for a response, its simple to reason about but little concurrency is involved

### ~ synchronous messages
- the sender process ==waits== for the receiver to simply ==get the message==, but not necessarily reply
- synchronous messaging is used in programming languages like Go, and Python

### ~ asynchronous messages
- after the sender sends the message, it ==continues execution immediately==, without waiting for a response from the receiver process
- the main drawback is that there is no confirmation whether a recipient thread even receives the message sent, but the time required in comparison to the 2 other mechanisms is much shorter

![ | 550](https://i.imgur.com/rmkOFZE.png)
