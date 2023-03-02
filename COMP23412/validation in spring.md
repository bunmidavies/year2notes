[[COMP23412]]

simple validation can be provided to ==entities== in spring through annotations, for instance:
- `@NotEmpty`
- `@Size`
- `@Pattern`

validation can also be provided to the ==controller==, by stating which field you want to be validated, and providing parameters to capture errors