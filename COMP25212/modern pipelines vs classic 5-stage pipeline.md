[[COMP25212]]

- as shown within examples, the typical pipeline has consisted of 5 stages where all instructions flow across the same datapath
![ | 550](https://i.imgur.com/J65Ad15.png)
- it should be noted that processors today may have ==multiple execution paths== - this means that there is not a singular path which every single instruction travels down
![ | 450](https://i.imgur.com/XR9e1De.png)
- the different paths can be called ==functional units== - some of these can be pipelined, while others cannot
- the functional units which can't be pipelined only allow ==one instruction== to travel down them at any time - in the case that a functional unit needs to be used by multiple instructions at one point but is occupied, these instructions are essentially ==conflicting== with one another - these are called [[structural hazards]]

