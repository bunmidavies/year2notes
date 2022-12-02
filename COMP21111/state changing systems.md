[[COMP21111]]

- the main interest is in modelling state-changing systems
- programs can be represented as state changing systems

- states of a program represent where all variables are assigned to some value
- another example are digital circuits, which have states correpsonding to the values assigned to each gate

- to reason about a state changing system:
	- a formal model of the state changing machine must be made
	- some logic is used to specify / verify properties of a system

## state changing system example - microwave

| variable | domain of values |
| --- | --- |
| mode | {idle, cooking, defrost} |
| door | {open, closed} |
| content | {none, burger, pizza, cabbage} |
| user | {nobody, student, vegetarian} |

- PLFD is a family of logics - each instance of PLFD has:
	- set $X$ of variables
	- mapping $dom$