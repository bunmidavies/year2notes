[[COMP24011]] / #comp24011

- Modal Logic is used to represent beliefs, i.e. **A knows P**

$$K_AP$$
- $K$ - used to indicate that this is **knowledge**
- $A$ - an agent
- $P$ a sentence

- Accessibility relations are used to connect **possible worlds** together, where a world contains some statements which may contradict with another world
$$Acc(K_A, w0, w1)$$
- This indicates that world $w1$ is accessible from world $w0$ with respect to $K_A$ if and only if everything in $w1$ is consistent with what $A$ knows in $w_0$
- **An agent's belief is only true in a world $w$ if and only if their belief is true in every world accessible from the world $w$**
- We use the notation above to indicate which worlds are accessible from a given world