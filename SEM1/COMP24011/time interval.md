[[COMP24011]] / #comp24011

- The term **interval** is used interchangeably with **duration**
- There are two types of time interval:
	- Moment - an interval with zero duration (i.e. a point in time)
	- Extended interval - an interval with non-zero duration

***
## Allen's Algebra
- Allen's algebra is a popular set of predicates which are used to deal with intervals

- $Meet(i,j) \leftrightarrow End(i) = Begin(j)$
- $Before(i,j) \leftrightarrow End(i) < Begin(j)$
- $After(j,i) \leftrightarrow Before(i,j)$
- $During(i,j) \leftrightarrow Begin(j) < Begin(i) < End(i) < End(j)$
- $Overlap(i,j) \leftrightarrow Begin(i) < Begin(j) < End(i) < End(j)$
- $Starts(i,j) \leftrightarrow Begin(i) = Begin(j)$
- $Finishes(i,j) \leftrightarrow End(i) = End(j)$
- $Equals(i,j) \leftrightarrow Begin(i) = Begin(j) \land End(i) = End(j)$
![](https://i.imgur.com/ZFpnxGZ.png)

![](https://i.imgur.com/GQgfQ86.png)
