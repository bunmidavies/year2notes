[[COMP25212]]

### definition
- snooping protocols are used within multicore processors - each cache 'snoops' for activity concerned with any address in its cache - it changes its status and reacts adequately when needed (==all caches are aware of all events==)   
- this protocol requires a ==communications structure== (for instance, a [[bus]]) so that all communication is seen by all caches
- this communications structure is also the main downfall of snooping protocols ==scalability sucks==
- [[directory based protocols]] provide a solution to this drawback

### write update vs write invalidate
- ==write update== = the core sends out new written data so that all other cores snooping in can update their caches  
- ==write invalidate== = the core lets other cores know that whatever address is now invalid, and those cores need to now go get the data themselves (which they can do whenever they want)  
- update looks the most simple and obvious, but some tradeoffs include that:  
	- messages are longer (since an address + the new data must be provided)  
	- write updates would have to be sent out with each new write - if the other caches arent even using the data at the time, whats the point?
![](https://i.imgur.com/szFY50A.png)
![](https://i.imgur.com/Oi8joXs.png)
