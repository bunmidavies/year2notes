[[COMP24011]] / #comp24011 / #comp24011

## slam
- keeps track of the map of the environment
- the goal is to obtain a globally consistent estimate of the trajectory and map
- slam also detects when it returns to a location its already been at (**loop closure**), and does no further calculation - reducing drift

# vo
- recovers the trajectory only incrementally
- the goal is to obtain a locally consistent trajectory
- vo can be used within slam, as it is basically equivalent to slam before reaching loop closure
- global consistency is traded off for real time performance