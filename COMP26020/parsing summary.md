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

### LR(1) parsers
- LR(1) parsing is a subset of bottom-up parsing which is faster and more efficient, using certain tables in order to perform actions
- the main downsides to LR(1) is that large working sets are required, and poor error messages may be outputted by the algorithm

- there are other table construction algorithms (to be used in parsing) which exist, which will produce smaller tables in comparison to LR(1), but these algorithms come at the cost of larger space requirements