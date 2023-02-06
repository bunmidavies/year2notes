[[COMP24011]] / #comp24011

- within feature detection, there are different types of features that interest us
- there are a lot of feature detection algorithms, so none of them are gone into too much depth

## types of features
- **[[keypoint]]** - a singular point (or a small patch of pixels with the keypoint in the centre)
- **edges** - curves/line segments, normally used to represent boundaries

## general steps of feature detection
1. apply response function on image
2. identify all local minima/maxima from the result of the function (nonmaxima suppression is used to remove overlaps)
**example: [[FAST feature detection]]**

## types of keypoints
- corner: a point at the intersection of 2+ edges
- blob: a pattern that differs from its close neighbours (in terms of intensity/colour): e.g. SIFT, SURF

- corners are faster to compute, meanwhile blobs are slower but more distinctive

after feature detection comes [[feature description]]