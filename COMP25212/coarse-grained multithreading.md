[[COMP25212]]

### definition
- in coarse-grained multithreading, instructions are issued from a ==single thread==
- as opposed to [[fine-grained multithreading]] where thread switches happen every few cycles, a thread switch here only takes place in the case of:
	- an ==expensive operation== (e.g. cache miss / data miss)
	- the ==quantum== of execution, which could typically be a few ms

- the main difference between coarse-grained multithreading and [[fine-grained multithreading]] is that ==short stalls== (e.g. [[data hazards]], [[control hazards]]) are ==not solved== by coarse grained multithreading
- therefore, coarse-grained multithreading is most useful for reducing the penalty of ==high cost stalls==
- ==minimal pipeline changes== are required, since thread switches happen not-so-often
- the thread switching mechanism must be faster than reaching a cache line, but not necessarily instantaneous

![ | 450 ](https://i.imgur.com/y5Cpz3U.png)
![ | 450](https://i.imgur.com/jWbtSL7.png)
[ note that the width in these threads represents how many instructions the superscalar pipeline can issue at the time ]