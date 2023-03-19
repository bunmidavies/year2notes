[[COMP26120]]

==6th feb - need to go over this again==

the [[loop invariant]] technique is used to prove the correctness of these algorithms again, like for [[bellman ford]]

assume $s \in F$ and for all $u \in F$
- $D(u) = \delta(u)$ (precise)
- $\forall v, D(v) \leq \delta(u) + weight(u,v)$ (u relaxed with precise D(u))
- $\forall u \in V . D(u) \geq \delta(u)$ 

F = $\emptyset$ holds initially, and in the first iteration $s$ is relaxed and $D(s)=0$ is precise

now v can be relaxed, with the minimal $D(v)$
in the diagram below we can see that $s$ and $u$ are already ==finished==
![](https://i.imgur.com/uBuQuXc.png)


we show that $v$ is the correct node to relax i.e. D(v) is precise by showing another path cannot exist
![](https://i.imgur.com/SeWPSUT.png)

this shows that introducing a new $v'$, that $D(v) \geq D(v') \geq D(v)$, which can't possibly hold - therefore, this proves correctness (?)

==using the correctness of dijkstra's, it can be extended to A*==

the idea for this is that ==A* is equivalent to a run of dijkstra on a modified graph==
- a new function is used for weights:
  $w'(u,v) = w(u,v) + h(v) - h(u)$
- initialization = $D'(s) = h(s)$
- Dijkstra's using $w'$ and $D'$ will now relax the same nodes as A* on $w$ and $D$
- This means that these runs are equivalent, therefore ==A* is correct==