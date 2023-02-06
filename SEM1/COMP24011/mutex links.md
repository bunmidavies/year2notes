[[COMP24011]] / #comp24011 
mutex links are part of [[planning graphs]]

==mutex links== are used in action/situation levels to indicate actions / literals which ==contradict== eachother, and cannot happen simultaneously

mutex links hold between ==two actions== when any 3 are met:
- ==inconsistent effects==: one action negates the effect of the other
- ==interference==: one effect of one action is the negation of a precondition of the other action
- ==competing needs==: if one of the preconditions is mutex with the precondition of another - i.e. one action requires no cake, while the other action requires cake

mutex links hold between ==two literals== if one is the negation of the other, or if every ==possible pair of actions== to achieve these two literals are mutex - this is called ==inconsistent support==