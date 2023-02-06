[[COMP24011]]

path-consistency is similar to [[arc-consistency]]

a constraint network is ==directionally path-consistent==, if for any indices $i < j < k$, and any pair of elements $a_i\in D_i, a_j \in D_j$, such that $(a_i,a_j) \in R_{i,j}$ (i and j are valid in the network), ==there exists== $a_k \in D_k$ such that $(a_i,a_k) \in R_{i,k}$ and $(a_j,a_k) \in R_{j,k}$