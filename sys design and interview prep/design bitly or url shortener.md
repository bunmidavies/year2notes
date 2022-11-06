[video](https://www.youtube.com/watch?v=eCLqmPBIEYs)

# video contents

## bitly use / why is it useful

- bitly can be useful to save characters in a tweet, or save space
- users are less likely to mistype shorter URLs
- optimise links, track individual links, hide affiliated URLs

## do not do this

- dont just describe load balancer with 2 functions, and a map
- the interviewer is looking for you to understand system design principles that have previously been discussed - the non functional requirements as well as the functional requirements. **therefore,** this means the interviewer wont like a basic solution which just maps short URLs to long URLs
- url shorteners should focus on durability and scalability

## database design

- URL table:
	- originalURL
	- expiryDate
	- userID

- User table (assuming you dont want anonymous users)
	- Name
	- Email
	- CreationDate
	- LastLogin

- You should clarify with the interviewer whether you want users to stay anonymous or not. **YOU COULD MENTION THOUGH**, that a malicious user can consume all URLs. To prevent this, users can be rate limited through some sort of API key

## non functional / database continued

- the service is read heavy
- in general, **relational databases e.g. SQL** are good when you expect to make a lot of complex queries
- **NoSQL** is worse at this (non relational, also worse consistency), but the tradeoff for this is that its faster for writes and simple key value reads
- We can go with NoSQL for now, as it can be easier to scale, and relational queries wont occur very often with our usecase

## functional / core features

- encodes a url into a 7 digit id key (e.g. thewebsite.com/8559327)
- as we are using digits between 0-9, we have base 10, and 10^7 = 10 million urls, which isnt a huge amount
- instead, if we use a base62 system ([A-Z, a-z, 0-9]), we get 62^7 = 3.5 trillion urls, this is much better
- we need a good balance between creating short URLs, but having enough URLs such that we dont run out

## hashing (solution 1)

- we compute a unique hash (MD5, SHA256) of a given URL, then encode using base62
- MD5(original URL) -> base62encode(hashed result) -> ABCD123...
- truncate the hash to the first 7 characters, which we end up using
- collision problem ? it is unlikely, but there **is still a possibility, and needs to be accounted for**
- we could use PutIfAbsent to solve this, but **this may not be supported by all NoSQL databases**

## hashing w/ out collision (solution 2)

- in this solution we are NOT encoding the URL
- we store a counter between 0-3.5 trillion (no of possible key-values we agreed on)
- each time a user requests a URL shortening, we give them current counter value and then increment the counter
- base62 encode this counter, and we will never get a non unique shortened URL!
- **single point of failure** - how is the counter being stored? if it is on some kind of server, and it goes down, we lose the ability across all services to be able to shorten URLs
- can the single counter server handle request spikes
- solution : distributed systems manager e.g. ZooKeeper - gives servers unused ranges, so they dont have to worry about accidentally incrementing the counter or colliding with another server, or even worry about the main counter going down (when range runs out, server asks zookeeper for increased range)
- However, zookeeper increases complexity, and can be a single point of failure? cost can be increased
- Generating URLs in a sequential manner can have security concerns - potential solution: add random characters at the end, but do we not kind of start to lengthen the URL again and lose the original point of the service?

## scaling solutions

- if we get 'hot links' i.e. certain URLs of our own which get posted on social media (e.g. becomes popular on reddit), if users keep making requests to the database, we now increase throughput heavily and can cause pressure on central servers
- potential solution is a distributed cache (redis? cant remember the name) - i guess cache expiry isnt a huge problem, can use something like an LRU cache which hasnt constant time operations
- this can increase cost / complexity

- load balancer - round robin approach to distribute incoming requests equally among backend servers. easiest to implement
- however, round robin doesnt take server load into consideration, therefore we may continue to forward requests to servers which are under serious strain
- other distributing methods include least connection, least response, least bandwidth

## interviewer guide ?? 

- *a poor candidate proposes a solution that uses a single id generator (single point of failure) or a solution that requires coordination among id generator servers on every request - single database server using auto-increment primary key*
- *acceptable candidate proposes a solution using an md5 of teh URL, or some form of UUID gen. that can be done independently on any node - while this allows distributed generation of non-colliding IDs, it yields larger "shortened" URLs* (contradicts the video because there should be some chance of collision?)
- *good candidate designs a solution which utilizes a cluster of id generators, which reserve chunks of the id space from a central coordinator (e.g. ZooKeeper), and independently allocate IDs from their chunk, refreshing as necessary*