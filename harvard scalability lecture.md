this lecture is from CS75 in 2012 so some of the technology mentioned might be outdated i guess, but since its still recommended im guessing the content is still all fine
[link](https://www.youtube.com/watch?v=-W9F__D3oY4)

- web hosts: look at recommended web hosts used these days
- web hosts should hopefully use SFTP over FTP (encrypts password data)

- VPS vs public webhost - a VPS allows you to have a certain slice of hardware (data is not secure from web hosting company)

- How do you go about scaling a site with potentially static/dynamic resources, some kind of database, when no of visitors increases by an extreme?
- **Vertical Scaling** - the easiest solution. Get a better CPU, better RAM, better resources. Disk scaling (Higher RPM). Vertical scaling obviously has real world constraints (there is a limit to server performance)
- **Horizontal Scaling** - using cheaper hardware in comparison to vertical scaling. Using multiple servers, which can be managed with some kind of **load balancer**. The load balancer can have its own ip, then route requests to servers (which could now have private addresses), using things like round robin, least busy, least load etc.
- Load balancers may communicate between servers using TCP/IP
- Round robin downsides - doesnt take into account load, so just by luck servers may keep getting heavy requests. Another bad case is that if your session exists on one server, and youre then sent to another server by the load balancer and your session data is gone
- A possible solution to the session issue above, is storing session data somewhere in common with the server - sessions could go on the load balancer (downside - a new single point of failure)

- Load balancers can exist in hardware, or can exist in software
- **Popular software option** Amazon's Elastic Load Balancer (ELB)
- Hardware solutions for load balancers are probably **much more expensive**

- RAID (RAID0, RAID1,...) technology - RAID assumes you have multiple harddrives, and allows you to write data across multiple harddrives, such that youre effectively doubling your writing speed. Other examples include replicating each file that is written

- Sticky sessions are the idea of sessions being saved for a certain user, regardless of how many times they make requests to a server (thus potentially being forwarded to different servers via the load balancer) - We could solve this problem potentially using cookies (to store server IDs)

- *Talking about PHP acceleration, because PHP is interpreted, but i dont know how useful or relevant this is today bc PHP is fucking ancient lol*

- Caching can very often be considered - Memcached is mentioned and is still popular today i think. The instance of memcahed will exist on a server, and essentially stores cache within RAM
- When cache starts to get full (obviously size constraints exist within ram), **eviction** should be used (think about LRU cache, diff eviction strategies)
- MySQL query cache - query caching will allow recently executed query results to be retrieved

- Database replication - Master Slave
- There is a master database, which is read to / written from - then there are a number of slave databases, which tries to get every copy of a row from the master database
- In theory, the slaves should all be identical to the master - this improves availability (in the case of the master going down, you have x amount of replicas which should be doing the same thing)
- You could also potentially load balance across the master and slaves, since they should be storing the same data 
- For very read heavy websites, you could technically just read from slaves, and only use write queries on the master server (thus balancing read requests) - the downside of this is that there can be downtime in between setting up a new master etc. potential solution includes a master-master setup

- Given the ideas above about slave-master replication and read heavy websites, we could technically set up two load balancers - one for the web servers, then another load balancer for the slave databases (perhaps just for read operations)
- Single points of failures can typically be seen as well defined - in a diagram, just find things of which only 1 exists
- active / passive load balancers ? (basically just have multiple load balancers) - remember **that load balancers are fucking expensive**

- Geography based load balancing - if system is to be on a large scale, this is a real thing that happens in global coorporations

- Partitioning / Sharding
- Load balancers could be partitioned (e.g. A-M users in one DB, N-Z in another) into clusters, or the databases themselves could be as well (sharding)

- Traffic between components
- TCP on specific ports from users to load balancers
- Load balancers to webservers using tcp
- Web servers to databases - SQL queries (or NoSQL Queries) - Therefore more TCP requests (MySQL uses TCP)
- Learn about: TCP ports
- Security wise, firewalls may only allow certain ports