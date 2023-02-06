[[COMP24011]] / #comp24011 

an ==n-gram character== model is a type of language model ([[language models]]), which models a probability distribution over a ==sequence of characters==

example:
- P("the") = 0.027
- P("zgq") = 0.0000000002

an ==n-gram== is a sequence of $n$ characters:
- unigram = 1-gram
- bigram = 2-gram
- trigram = 3-gram
etc...

so an ==n-gram model== is a model for ==n-char== sequences specifically. They're defined as ==markov chains== of order ==n-1==

a markov chain ==order== means the number of previous states which are used to determine the ==current state==

example: a markov chain of ==order 2==:
- P($c_i$ | $c_{i:i-1}$) = P($c_i$|$c_{i-2:i-1}$)
i.e. chars $i-2$ and $i-1$ are used to determine $i$'s probability

the estimation of probabilities is based on counting character sequences in a ==corpus== (collection of text documents)

n-gram character models are used in:
- language identification
- spelling correction
- genre classification
- named entity recognition (i.e. finding chemical names in a scientific article)

the alternate to n-gram character models are [[n-gram word models]]
