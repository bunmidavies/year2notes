[[COMP23311]] `week 5`

Feature scoping finds its use when faced with introducing ==new software features== into a ==large existing system== while:
- the system is already in use
- not breaking something important
- not knowing entirely what the users want (large userbase)
Therefore, deploying new features within software can be said to have some ==risk== associated with it

There are 3 main ==risk management== strategies when implementing software:

### build on existing components
When working on critical parts of a codebase, the goal is to implement features with ==as little code as possible== - if the opportunity exists to build upon already tested + in use code in the codebase, then this is the number 1 option. Avoiding adding new code written from scratch reduces the chance of ==functional regression==, where certain functionality within software stops working due to new code

In short, adding lines of code introduces ==risk== of something breaking - functionality should be implemented with the ==minimum amount of work==

### incremental releases
Additionally, when introducing features, it is preferable to make ==incremental releases== - e.g. in Stendhal, pets were firstly introduced as stupid sheep which couldn't do anything, then cats which could eat food, then dragons which could fight for the player. At each stage player feedback was received, so according changes could be made before the next release

### controlling the scope
When implementing a feature, the following things can be considered:
- Which types of object are affected?
- Which existing functions are affected?
- Which user groups are affected?
By ==minimizing the scope==, the chance of many different areas of some piece of software being broken reduces. For example, in Stendhal the newer features may only be released to long term players first, before the general public, or just for one zone/NPC
