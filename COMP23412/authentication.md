[[COMP23412]] - [[security in web applications]]

- ==Authentication== is simply the process of confirming the identity of a user, preventing user ==spoofing identity== attacks in an application 
- Authentication is ==different to authorisation== due to authorisation being concerned with the privileges an authenticated user may already have, as opposed to authentication which aims to make sure the user is who they say they are
- ==Credentials== are provided by users, and compared to those held in a secure user database. These can often be combined to form ==two-factor authentication (2FA)==
- There are 3 main types of credentials:
	1. Who we are - biometrics, fingerprints, face recognition
	2. What we know - username / password, PIN code
	3. What we have - RFID card, USB token, One-time password token
- ==Insecure authentication== typically involves storing anything in plaintext in a database - if a hacker gains access to this database, they know the exact credentials of all users, which isn't ideal
- [[hash functions]] can be used as a deterministic way to turn passwords into undecipherable text, meaning if a hacker gains access to the database, they still don't know the users passwords
- hash functions should be applied to the password with a ==salt==, in order to prevent dictionary attacks

- Example hash functions
	- MD5 - insecure
	- SHA1 - not recommended
	- SHA2 - secure
	- SHA3 - secure