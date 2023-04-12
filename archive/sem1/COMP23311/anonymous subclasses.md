[[COMP23311]]

vaguely related to [[design for testability]], anonymous subclasses are useful in Java for instantiating classes on the fly, with specific methods overriden to do something you need

This is commonly used in stendhal testing to slightly override objects to provide the behaviour required to test something

for instance, the `test.games.stendhal.server.actions.admin.SummonActionTest.setUP()` method is written as follows:
```Java
public void setUP() {
		zone = new StendhalRPZone("testzone") {
			@Override
			public synchronized boolean collides(final Entity entity,
					final double x, final double y) {

				return false;
			}
		};
	}
```

as can be seen, within the `{ }` an already existing method within `StendhalRPZone` is overwritten with a hardcoded value
