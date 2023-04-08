[[COMP26020]]

### ~ definition
- mutual exclusion is a basic coordination principle for threads ([[concurrency]])
- it is the requirement that one thread can never enter a ==critical section== of code, while another thread is currently accessing the same critical section
- for this reason, critical sections are effectively ==atomic==, and mutual exclusion makes reasoning about the behaviour of a program with multiple threads easier

### ~ creating critical sections
- a ==preprotocol== and ==postprotocol== are required before and after critical sections of code - the former being executed before the critical section, and the latter being executed after
- the one requirement for a critical section is that it must ==always complete== - in the event that it cannot complete, this is known as ==starvation==
- its preferable that critical sections do try to perform an operation which is atomic, such that the waiting time for the critical section isnt very long
- a typical method of achieving mutual exclusion can be done with ==CAS== (compare-and-swap) - you probably wont ever need to write the code shown below since it is provided by libraries
![ | 550](https://i.imgur.com/4rJP4us.png)

### ~ locks
- locks are also known as ==mutexes==, and typically control access to critical sections
- a thread will typically try to acquire a lock through some method - if the corresponding critical section is already occupied, the thread goes to sleep until its no longer occupied
- when a thread leaves a critical section, it 'releases' the lock, waking up other threads which were put to sleep from trying to acquire the lock
- low-level mutual exclusion would essentially keep on trying to access a critical section until its possible, meanwhile the use of sleeping + locks allows for better utilisation and energy efficiency
- [[monitors]] make use of locks, but also provide other features

### ~ semaphores
- semaphores are able to limit the number of threads which access a specific resource, through the use of a counter
- if the counter is currently 0 and a thread wishes to access the resource, the thread will go to sleep - if the counter is greater than 0, it can be decremented and access can be granted
- when a thread releases the resource, the semaphore can wake up a thread (if threads are waiting), or increment the counter

### ~ links
- [wikipedia - Mutual exclusion](https://en.wikipedia.org/wiki/Mutual_exclusion)
