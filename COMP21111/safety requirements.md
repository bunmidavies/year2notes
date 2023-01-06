[[COMP21111]]

- ==unsafe== is used to describe states which you want to ensure a system never reaches 
- typically, unsafe properties in [[LTL]] (linear temporal logic) can be described, then negated with the $\square$ operator, to indicate they should ==the negation should always hold==

- ==mutual exclusion== ensures two processes are not in the "critical" section

- ==fairness== is a property to describe certain properties which ==must hold== given some other property holding, e.g. $\square$(cusomter = student -> $\diamond$customer = prof)

- ==responsiveness== indicates that every request will be ==eventually acknowledged==, e.g. $\square$(request->(reuest$\mathcal{U}$acc))