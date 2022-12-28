[[COMP24011]] / #comp24011 

==text classification== is a method used for [[knowledge acquisition]] - it is used to decided which classes in a predefined set some extract of text may belong to

a typical example of this is ==spam detection==


the standard approach to text classifications is with a ==Bag of Words==

- input text is represented as ==feature-value== pairs
- e.g. ==feature== = a unigram, ==value== = no. of occurences
- word order is lost in a bag of words

==feature selection== is the process of removing features which you may not be interested in. For instance, removing extremely common words which appear in many spam/ham emails, because they're not ==informative==

==supervised learning== e.g. machine learning can then be applied, using this bag of words