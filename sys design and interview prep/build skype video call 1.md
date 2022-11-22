TCP is essentially built on UDP

udp is unordered
tcp is ordered

therefore for video calls, udp may not be preferable, because your video can come out more jumbled, and things will make less sense (unreliable)

tcp requires back and forth (syn, ack, ack ack) - the acknowledgement is required in order to send the packets in the correct order. Therefore more latency is involved, because you have to wait for every packet to return

**we dont want the unorderliness of UDP, but we dont want the overhead / latency of TCP, so we could potentially build our own protocol on top of UDP, which discards late packets**

REST is based on TCP, so instead we could use web sockets

Components
**Main Server**
**Web Sockets (Keeps a live connection to the server - so new connections dont have to be established, and can just be left open)**

Server needs to create an active room if a user sends a call request, and the recipient accepts

**look into sending packets as bytearray**

**datastore for lookup with the load balancer (redis, single core)