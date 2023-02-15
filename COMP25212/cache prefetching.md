[[COMP25212]]

cache prefetching is an attempt to reduce the number of cache misses by ==speculation== - predicting and fetching lines before they might be wanted

spatial [[locality]] typically helps with prefetching - these can be initiated by software 'hint' instructions, or potentially predicted by hardware

things like matrix column access are easily predictable by the processor