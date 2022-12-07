[[COMP24011]]

- within feature detection, there are different types of features that interest us

## types of features
- **[[keypoint]]** - a singular point (or a small patch of pixels with the keypoint in the centre)
- **edges** - curves/line segments, normally used to represent boundaries

## feature detection
1. apply response function on image
2. identify all local minima/maxima of the function

## types of keypoints
- corner: a point at the intersection of 2+ edges: [[FAST feature detection]]
- blob: a pattern that differs from its close neighbours (in terms of intensity/colour): e.g. SIFT, SURF

after feature detection comes [[feature description]]