[[COMP23412]]

more annotations can be used in spring in order to indicate relationships between fields in a table:

taking the venues example from [[data modelling and persistence in Spring]]:

### @OneToMany
- A venue can host many events

### @ManyToOne
- An event has one venue (this is many to one because there are many events which exist, and these can still take place in one venue)

### @OneToOne
- A venue has a manager (this is truly one to one, as there aren't multiple managers for a venue, and a manager won't manage multiple venues)