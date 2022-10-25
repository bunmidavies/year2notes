- lab involves uisng the python constraints module

**logic puzzle**
- The following travellers are returning from their travels:
	- Claude
	- Olga
	- Pablo
	- Scott
- They are travelling from the following countries:
	- Peru
	- Romania
	- Taiwan
	- Yemen
- There are 4 different times for departing journeys:
	- 2:30
	- 3:30
	- 4:30
	- 5:30
- No two travellers return from the same destination, and no two depart at the same time
- **Constraints**
	- Olga leaves 2 hours earlier than the traveller from Yemen
	- Claude is either leaving at 2:30, or 3:30
	- Whoever is leaving at 2:30 is flying from Peru
	- The traveller from Yemen leaves earlier than the traveller flying from Taiwan
	- The four travellers are: Pablo, the traveller from Yemen, the traveller leaving at 2:30, and the traveller leaving from 3:30

- `AllDifferentConstraint()` within the constraint library seems to be used for establishing that solutions should consist of unique variables provided in the method?

constraint 2:
```
for person in people:
	problem.addConstraint(
		(lambda x,y,z: ())
	)
```