[[COMP25212]]

### ~ definition
- cache lines exploit ==spatial== [[locality]] - several consecutive words from memory are stored within the data field for a given tag in cache
- some extra data needs to be stored for each line, but in reality organising data in lines will save a lot of tag storage
- the typical line size within a cache may be 4 or 8 words
- ==as the line size increases, tag size decreases==
![ | 500](https://i.imgur.com/lOQnWkK.png)


- each cache line typically has 3 fields:
	1. Address information - usually called a ==tag==
	2. Data - depending on ==cache line size==, this could contain several words of data (obviously including the data word required)
	3. Valid bit - indicates whether the line contains currently valid data

- there are many ways to organise and use the 3 main fields in a cache line - the main types considered in COMP25212 are full associativity, direct mapping and set associativity

cache lines also exploit spatial locality - instead of typically storing a single word of data within each tag, several ==consecutive== words are stored per tag

the consecutive words of data can be called a ==line== - typical line sizes in memory cache are 4, 8