[[COMP23412]]

As already known, the core component of an app using the MVC pattern is the ==Model==

Data persistence is key if any data needs to be stored and used for later - this page explains how to build a model using Spring, which is the MVC framework for Java (so some of the info in this is Java/Spring specific)

The content is set in the context of creating an event app (as part of the team coursework)

A venue for an event can be represented using a ==Plain Old Java Object (POJO)==

```Java
@Entity
@Table(name = "venues")
public class Venue 
{
	private long id;
	private String name;
	private int capacity;

	public Venue() {}
}
```

getters and setters need to be named specifically in order for Spring to guess what they're called

to ==persist== a model in a database, i.e. save these venues, we just add the `@Entity` and `@Table(name = "venues")` as shown in the top of the snippet - the entity ==annotation== means that we want this object to be the base entity for some table, then used the table annotation to give this table a name (This annotation is actually ==optional==)

further annotations can be used to help Spring, i.e. an annotation for primary key, and an annotation to let Spring generate primary key IDs for you

the appeal in this is that ==Spring has abstracted all the details of an underlying database for us== - we now have stored the venues in some kind of database table to be used for later, but what type of database and how it is structured is unknown to us, saving time and effort

this abstraction can be shown as such:
![](https://i.imgur.com/9DMyrtv.png)

==The service layer holds the business logic==, and the venue repository simply talks to the database using SQL (which we don't have to worry about, as we only write Java) - this is largely what Spring actually does (but in reality is more complex than this in order to abstract all details away)

we can define our ==venue repository== as follows:
```Java
public interface VenueRepository extends CrudRepository<Venue, Long> 
{

}
```

- CRUD stands for ==Create, Read, Update and Delete==, and is the standard way of referring to the basic operations within a database
- By simply extending this interface, spring will now automatically generate the classes which are required for your venue repository
- The default implementation of this interface provides a few different database type methods e.g. `count()`, `findOne()`, `save()`, `delete()`

spring additionally allows the ability to automatically generate classes which provide the functionality required by an SQL query you specify, if you give the method that given query name:
```Java
public interface VenueRepository extends CrudRepository<Venue, Long> 
{
	public Iterable<Venue> findAllByName(String name);
	public Iterable<Venue> findAllByNameOrderByNameAsc(String name);
	public Venue findFirstByNameOrderByNameAsc(String name);

	public Venue findByNameContainingAndCapacity(String nameSearch, int capacity);
}
```

[more info on query methods](https://www.amitph.com/spring-data-jpa-query-methods/#using_spring_data_jpa_query_methods)
the Spring documentation also has more info on query methods

the ==venue service== implements a service interface - this can be a useful layer as although the venue repository provides all the functionality required, the venue service can apply more manipulation to queries, and we may not want to ==expose all venue repository functionality to the controller==. This means the controller can continue to be kept ==as simple as possible==

```Java
@Service
public class VenueServiceImpl implements VenueService
{
	@Autowired
	private VenueRepository venueRepository;

	@Override
	public Iterable<Venue> findAll()
	{
		return venueRepository.findAll();
	}
}
```