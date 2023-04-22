[[COMP25212]]

- as discussed within the previous weeks, various mechanisms exist to improve the performance within a single-core processor, at the architecture level:
	- [[caches]] - minimise memory access impact
	- [[pipelining]] / superscalar - increase parallelism supported by the processor
	- [[out of order processors]] - increase the number of independent instructions per cycle
	- [[branch prediction]]
- however, all of these methods have ==limited scalability== - scaling up beyond a certain point is not practical - hardware, power and cost increase more than linearly while performance does not improve at a linear rate
- the obvious solution to this is ==putting multiple cores on a single chip==, which can be used in parallel

### reasons for slowdown
- [[power wall]] - power density (i.e. watts per unit area) increasing has made cooling a serious problem
- ==ILP wall== - applications have a limited amount of parallelism
- [[amdahls second law + memory wall]] - memory does not get faster at the same rate as processors
- architectural innovation reaching ==design complexity problems==
- unreliability within smaller transistors