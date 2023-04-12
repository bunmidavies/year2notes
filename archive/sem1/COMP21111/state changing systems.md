[[COMP21111]]

- the main interest is in modelling state-changing systems
- programs can be represented as state changing systems

- states of a program represent where all variables are assigned to some value
- another example are digital circuits, which have states correpsonding to the values assigned to each gate

- **to reason about a state changing system we require:**
	- a formal model of the state changing machine must be made
	- some logic used to specify / verify properties of a system

## state changing system example - microwave

| variable | domain of values |
| --- | --- |
| mode | {idle, cooking, defrost} |
| door | {open, closed} |
| content | {none, burger, pizza, cabbage} |
| user | {nobody, student, vegetarian} |

- the microwave example can then be reasoned about using [[plfd]]

## building a formal model

- the actions that change the state of a system are called **transitions**

- building a formal model requires 3 things to be defined:
	- state variables
	- possible values for given state variables
	- transitions and how they change the values of state variables

- [[state transition systems]] can be used to formally describe our state changing system