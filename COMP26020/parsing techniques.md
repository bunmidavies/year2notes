[[COMP26020]]

summary of parsing techniques, with more info in:
- [[top-down parsing]]
- [[bottom-up parsing]]

## top-down parsers
- top-down parsing typically refers to how human beings attempt to find derivations
- start at the top node of the parse tree, and grow towards the leaves, by trying to match the input in a ==depth-first== manner
- top-down parsers find a ==leftmost derivation== for the input string
- some grammars are backtrack free, which allow for top-down parsing

## bottom-up parsers
- the tree for an input string is constructed by starting at the leaves, and working upwards to the root
- bottom-up parsing uses a left-to-right scan of the input, but tries to construct a ==rightmost derivation== in reverse
- bottom-up parsing can handle a large class of grammars