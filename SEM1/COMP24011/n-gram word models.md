[[COMP24011]] / #comp24011 
[[NLP]]

==n-gram word models== have the same mechanisms as [[n-gram character models]], but there is a much larger ==vocabulary== within these models:

with character models, there are about 100 or less ==unique characters== in a language
with word models, there can be 10,000s - millions of words

an ==out-of-vocabulary word== is a word that was not seen in the training corpus. These words need to be explicitly modelled in the language model