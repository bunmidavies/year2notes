[[COMP26020]]

- The key point which allows this to work is the fact that regular expressions are fundamentally made up of ==four different operations== - and each of this can be turned into an NFA
![ | 450](https://i.imgur.com/A4rOXnZ.png)
- Relating to [[building scanners]], the next step after creating the NFA is to create the DFA - [[NFA to DFA]]

### example
![ | 450](https://i.imgur.com/0ezj2bh.png)

- note that the pattern for `b|c` gets embedded within the pattern for any $*$ formula, shown in the key idea slide


### links
- [regex to NFA](https://cyberzhg.github.io/toolbox/regex2nfa?regex=YXxi)