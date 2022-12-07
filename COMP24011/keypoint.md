[[COMP24011]]
[[feature detection]]

## keypoints
- keypoints are useful for finding corresponding locations between two images
- **correspondence methods** are what find these corresponding locations

there are two main feature based correspondence methods:
- **matching** = independently finding features in all images then matching them
- **tracking** = finding features in one image, then tracking these in succeeding images

## keypoint matching / tracking
1. search images for keypoints
2. convert region surrounding keypoints to compact representation
3. matching: search for likely matches in different images (could occur anywhere) **OR** tracking: search the next images around a small area within the existing features



