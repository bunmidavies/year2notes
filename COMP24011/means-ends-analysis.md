[[COMP24011]] / #comp24011

a ==hybrid approach== to [[planning]], but not a ==complete== approach. Described as historical as well, used in GPS (1959) and STRIPS (1971)

the problem with means-ends-analysis is that it plans in a straightforward fashion, which can undo other goals while achieving some goals - examples include the ==blocks world==, a ==non-linear== planning problem

the steps within means-ends-analysis are:
- take the initial situation and set of goals
- find an action $\alpha$ such that add-list($\alpha$) $\cap G \neq \emptyset$
- find a plan $\pi$ which will achieve the preconditions of $\alpha$ and compute the resulting situation from executing $\pi$ then $\alpha$
- now find a plan $\pi '$ which achieves $G \setminus$ add-list($\alpha$) in resulting situation
- the final plan is $\pi;\alpha;\pi'$ 