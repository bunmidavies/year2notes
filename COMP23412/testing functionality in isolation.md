[[COMP23412]]

- its important to test things in isolation, in order to ensure that no other implementations are being relied on in order to test a singular class
- test doubles allow you to test certain parts of an application, without having the need to use the real implementation of other things which may be relied on
- test doubles were covered in [[COMP23311]] ([[design for testability]]), but to recap
	- ==dummy== - passed around but never used
	- ==fake== - works as expected, but has shortcuts inside its functions not suitable for full prod.
	- ==stub== - provides a canned answer to a particular invocation
	- ==mock== - a test double with preprogrammed expectations of how it will be called, and what happens internally when called

### mocking example
"A venue cannot be deleted if it has one or more events"

- return an empty list of events from a mocked venue:
```java
when(venue.getEvents())
	.thenReturn(Collections.<Event> emptyList());
```

- return that venue instance from the mocked venueService:
```java
when(venueService.findOne(1L).thenReturn(venue));
```

- do the delete operation:
```java
mvc.perform(delete("/venues/1")
		   .accept(MediaType.TEXT_HTML))
		   .andExpect(status().is(302));
```

- verify the behaviour of venueService:
```java
verify(venueService).delete(1L);
```