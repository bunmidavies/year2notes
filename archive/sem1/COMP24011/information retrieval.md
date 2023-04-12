[[COMP24011]] / #comp24011 

==information retrieval / IR== is an example of [[knowledge acquisition]]
given a user's ==query== (some information they want), relative documents are retrieved based off this query

examples include ==search engines== (google / bing)

components of an IR system include:
- ==corpus== of documents
- ==query==, expressed in some kind of query language
- ==result set== - the documents returned from the query
- ==presentation of result set== - e.g. ranked list of documents, network

the earliest approach to an IR model was the [[boolean keyword model]]
the main drawback of this model is that since it uses boolean expressions as ==queries==, the entire resulting set is just documents which returned ==1== from the expression. This makes it hard to rank these documents by relevance

[[BM25]] is one of the ==most popular== information retrieval approaches today. It is based on a scoring function

[[PageRank]] is also a very popular IR algorithm used in search engines

methods for [[evaluating IR systems]] are also used in ML approaches

==refinements==:
- case folding i.e. "cOuCH" -> "couch"
- stemming i.e. "couches" -> "couch"
  *this may hurt precision, i.e. system may do "stocking" -> "stock" causing irrelevant documents to gain higher scores*
- recognising synonyms i.e. "couch" $\approx$ "sofa"
*also may hurt precision, e.g. Couch as a name isnt equivalent to sofa*