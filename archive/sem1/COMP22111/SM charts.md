[[COMP22111]]

- The first step in designing a sequential system is to produce a state transition diagram (circles for states and conditional transitions between circles)

- The problem with these is that they become easily cluttered due to a lot of states
- State Machine (SM) charts can be used instead, and work like flowcharts
- SM Charts have 3 components:
	- ==State box== - A state box has a name, output list, state code, and one output path. It represents one of the finite states the system can exist within
	- ==Decision box== - Looks like a diamond. The box has 2 output paths, true or false, depending on the boolean condition / expression within the box
	- ==Conditional output box== - Entry path is always from a decision box, and has a single exit path. Certain outputs to be assigned are described within the box as a list (**Only available in mealy machines**)

- The SM chart is subdivided into SM blocks, which encapsulates the complete behaviour for a certain state. There can be multiple outputs from the SM blocks, but they must all be unique, and all possible conditions within the SM block must be covered

- Note that all components within an SM block **are evaluated simultaneously**. Contrary to how it may look (arrows implying data may flow from one block to another), everything that is determined within the sm block is done at the same time

- SM charts can be designed in multiple ways but actually give the same behaviour when implemented in hardware (thus being equivalent)

- **Link path extraction** - checking all the valid paths through the SM block are valid, and all boolean conditions are covered by the SM block

- Due to everything being processed in an SM block simultaneously, it also possible that you can design SM blocks in parallel or serially, and they will be equivalent