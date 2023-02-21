[[COMP23412]]

there are many web app security risks that exists, and any of these can be exploited by any type of attacker to cause problems within a system - COMP23412 covers top risks from the ==OWASP top 10 security risks (2017)==
![](https://i.imgur.com/TiqQ0JP.png)

### Broken Authentication
- broken [[authentication]] is mainly to do with storing passwords in plain text in a database
- hash functions are typically used to stop storing plaintext, but hashing only the password still leaves the risk of ==dictionary attacks== open - therefore, hashing with a ==salt== is typically performed

### Injection
- Injection in general involves an attacker including ==untrusted input== which gets processed as part of a command or a query
- There are multiple types of injection: ==Cross-site request forgery (CSRF)==, ==Cross-site scription (XSS)==, ==SQL injection==, etc.
- Systems which are prone to injection typically have ==insufficient user input validation== - the main way to avoid this is to ==never trust user input== - restricting, controlling and monitoring any form of user input helps to avoid an application from getting hacked

### Implementing security in Spring
Spring supports all major web security practices, these are provided by the ==Spring Security project==:
- Authentication: form-based login via session cookies, HTTP basic
- Authorisation: role creation
- Cross-site Request Forgery Protection