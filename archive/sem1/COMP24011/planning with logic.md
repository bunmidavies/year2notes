[[COMP24011]] / #comp24011

- this section follows on from [[planning]]
- in planning with logic we use *general first order logic*

- an important part to note about the first order logic we use is that ==**we do not assume that unique constants imply different entities**==. We HAVE to specify that say $a \neq b$ within other statements if we'd like to introduce them as separate entities. 
- [[planning - the frame problem]] and [[planning - the qualification problem]] explain where possible reasons as to why logic in AI may be unsuitable

- plans typically involve **goals, a plan, and knowledge**

- if knowledge is $\Phi$ and a statement showing that a particular plan achieves a goal is $\gamma$, we can say $\Phi \models \gamma$ to express that our knowledge **guarantees** gamma will work
- contrary to [[propositional logic semantics]] logic and modelling, where $\models$ means **models**, we call it **entails** here 
- Essentially, your plan works if $\Phi \models \gamma$ 

- when making moves while planning with logic, its important to specify not just what moves do, but what moves **don't** do
- we can now represent a situation, our knowledge, and goals within first order logic. The part we actually care about is how do we find a plan which reaches our goal? [[planning - finding a sufficient plan]]