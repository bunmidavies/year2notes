==week 11== - robotics

- sensors: the robots location, the environment, the robots internal configuration, range finders: sonar sensors/stereo vision, modern range finders: optical range sensors, LiDaRs, radar sensors, tactile sensors, GPS, proprioceptive sensors, wheel odometry + its issues, [[degrees of freedom]], kinematic state, dynamic state, holonomic vs non holonomic, sources of power

- perception: perception = storing map sensor measurements into internal representations - can be difficult as sensor data is noisy, bayes networks, localisation, mapping, robot pose $(x_t,y_t,\theta_t)^T$, actions consist of translational velocity and rotational velocity, range scan, SLAM

***

### revision lecture notes

- ==exam is a mixture of numerical, multiple choice and mcq==
- just know how to do all the search algorithms on paper
- know some basic practical refinements for minmax, certain limitations etc
- be able to formalise sudoku as a CSP
- be familiar with frame problem and qualification problem
- make sure you understand factorizing bayes networks (turning a probability into the correct sum)

- the slides for part 2 are the points to really focus on
- for text classification, focus on ==bag of words==
- BM25 is ==provided==, but the variable definitions aren't provided
- IDF is ==not provided==
- you may have to create an IR confusion matrix ([[evaluating IR systems]])
- PageRank is ==not provided==
- information extraction questions may involve ==RegExp==
- ==feature matching== is the main focus for computer vision