[[COMP24011]] / #comp24011
#ai

- odometry is the simplest form of localisation, originating from the greek words *odos* (route) and *metron* (measure)

- methods used by robots like wheel odometry are limited to ground vehicles, and are prone to many errors due to terrain conditions
- **visual odometry** is an alternative, other alternatives include GPS

## visual odometry (VO)
- a sequence of images of a robots environment are used to estimate a robots relative motion
- sufficient overlap between the images is required
- types: monocular (single-eye camera) vs stereo camera (two eyes)
- [[feature matching]] or [[feature tracking]] can be used as there are sequences of images

## problem formulation
- assume an agent moving within an environment and taking images at discrete points in time $k$
- monocular images = $I = \{I_0,I_1,...,I_n\}$
- stereo images = $I_{left} = \{I_{left0}...I_{leftN}\}$ and $I_{right} = \{I_{right0}...I_{rightN}\}$

- example: camera positions at times $k-1$ and $k$
- $T_{k,k-1} =$
  ${\begin{bmatrix}{R_{k,k-1} \ t_{k,k-1}}\\{0 \ 1}\end{bmatrix}}$
- $T_k$ is used to refer to ${T_k,k-1}$, and is formed by motion estimation (below)

- the set of transformations is referred to as $T_{1:n}$
- the set of camera poses relative to the frame at $k=0$ is $C_{0:n}$

- the current camera pose is just the concatenation of all transformations
- $C_n = C_{n-1}\cdot T_n$
![](https://i.imgur.com/o0SUfQD.png)


- the main task of visual odometry is to compute the transformation at every $k$ based on images $I_k$ and $I_{k-1}$
![](https://i.imgur.com/gIA9MjD.png)
![](https://i.imgur.com/K8BqrV3.png)


- VO recovers this path incrementally, with each pose

## visual odometry steps
- [[feature detection]]
- [[feature matching]] **OR** [[feature tracking]]
- motion estimation *(mostly out of scope for computer vision)*
- local optimization (bundle adjustment) - refinement over the last $m$ frames in order to reduce drift

- drift is important in understanding [[SLAM vs VO]]