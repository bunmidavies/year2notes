[[COMP23412]]

the risks described are part of the ==OWASP top 10 security risks (2017)== shown in [[security in web applications]] 

many ==privacy design strategies== exist in order to obey GDPR, and prevent privacy risks

### Sensitive data exposure
- examples of sensitive data include:
	- banking information: account numbers, credit card numbers
	- health information
	- personal information: NI number, date of birth, address
	- user account / passwords
- this data is protected by the ==GDPR - General Data Protection Regulation==. It enforces companies to take serious measures while handling customer data

### Hoepmans 8 privacy design strategies
- The 8 design strategies are on a very high level but popular, and used by companies when enforcing privacy into their applications
- The privacy design strategies, taken from [The Little Blue Book](https://www.cs.ru.nl/~jhh/publications/pds-booklet.pdf) are in 2 categories follows:

Data oriented strategies
==Minimise== - limit the processing of personal data as much as possible
==Separate== - separate the processing of personal data as much as possible
==Abstract== - limit the detail in which personal data is processed as much as possible
==Hide== - protect personal data, or make it unlinkable / unobservable. It should never become public or known

Process oriented strategies
==Inform== - inform data subjects about the processing of their data in a timely / adequate manner
==Control== - provide data subjects adequate control over the processing of their personal data
==Enforce== - enforce and commit to processing personal data in a privacy-friendly way
==Demonstrate== - demonstrate that personal data is being processed in a privacy-friendly way