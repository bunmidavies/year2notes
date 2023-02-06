[[COMP24011]] / #comp24011
following on from [[feature detection]]

- the region around each detected feature is compacted into a descriptor

## example: SIFT descriptor
- you have a 16x16 pixel patch around a feature
- calculate orientation/magnitude of the gradient at each pixel (in the patch)
- divide the patch into 4 equal subregions
- compute a histogram for each subregion

- after feature description comes [[feature matching]] or [[feature tracking]]