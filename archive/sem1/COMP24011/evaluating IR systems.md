[[COMP24011]] / #comp24011 
[[NLP]] - [[information retrieval]]


evaluating IR systems involves a table like such:

| | in result set | not in result set |
|---|---|---|
|relevant|30|20|
|not relevant|10|40|

==precision== = proportion of documents in result set that are ==relevant==
(false positive rate = 1 - precision)

==recall== = proportion of all relevant documents that are in result set
(false negative rate = 1 - recall)

==F1 score== = harmonic mean of precision and recall:
$$2PR(P+R)$$