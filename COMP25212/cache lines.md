[[COMP25212]]

- each entry in a cache, comprising data and addressing information is a ==cache line==
- each cache line typically has 3 fields:
	1. Address information - usually called a ==tag==
	2. Data - depending on ==cache line size==, this could contain several words of data (obviously including the data word required)
	3. Valid bit - indicates whether the line contains currently valid data

- there are many ways to organise and use the 3 main fields in a cache line - the main types considered in COMP25212 are full associativity, direct mapping and set associativity

cache lines also exploit spatial locality - instead of typically storing a single word of data within each tag, several ==consecutive== words are stored per tag

the consecutive words of data can be called a ==line== - typical line sizes in memory cache are 4, 8