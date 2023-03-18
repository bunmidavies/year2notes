[[COMP24011]] / #comp24011 

probabilistic models are another method of [[information extraction]], used in [[knowledge acquisition]] for NLP

the most common example of a probabilistic model is the ==Hidden markov model (HMM)==

![](https://i.imgur.com/8Tmn3b2.png)


the HMM models a progression through a sequence of ==hidden states== with an ==observation== at each step

==observation== = word in the piece of text
==hidden state== = which part of the attribute template the speaker is currently in:
- PRE = prefix
- T = target
- POST = postfix

HMMs are somewhat ==preferable== to [[finite state automata]] (RegExp), as it can tolerate some ==noise== within text (RegExp needs text to match ==exactly== as specified), and can be ==trained on data==