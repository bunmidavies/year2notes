### intro
Privacy by design has been a legal requirement from 2018 - it enforces that privacy requirements are taken into account right from the start and throughout the system development lifecycle. How to apply it in practice is covered by 8 following design strategies.
The design strategies are oriented over two different categories:
- data oriented - focused on the privacy-friendly processing of data
- process oriented - focused on the processes surrounding the handling of personal data

### data oriented strategies
##### Minimise
==Limit as much as possible the processing of personal data== - this can be broken down into a few main tactics:
- Select only relevant people and relevant attributes, only processing data that satisfies the selection criteria
- Exclude irrelevant people/attributes in advance, and do not process that data if received
- Strip - remove any data (including partial data) once its no longer necessary - ensure automatic deletion of data once its no longer required
- Destroy - completely remove personal data as soon as the person is no longer relevant, ensuring it can't be recovered
In 2014, ING (large Dutch bank), offered third parties the opportunity to target ad their bank account holders - this was considered a huge breach of trust. A company should think about their purpose and stay away from any use of data which strays from that purpose

##### Separate
==Separate the processing of personal data as much as possible== - there are two main tactics for this:
- Isolate - collect and process personal data in separate databases/applications
- Distribute the collection/processing of personal data over different physical locations - try to use the equipment of the data subject as much as possible (if possible at all)
Social networks with centralised architectures e.g. twitter, facebook, mean that a central server may hold a lot of value for these apps. A more privacy-friendly way of processing data in a distributed style is through using secure multiparty computation - arbitrary functions which operate using private inputs distributed over many different devices. The approach has been used to perform privacy-friendly auctions in Denmark, where only the highest bid is known, and the rest are secret.

##### Abstract
==Limit as much as possible the detail in which personal data is processed== - minimising focuses on whether to process a piece of data at all, while abstract focuses on the level of detail to which some data is processed. The following tactics apply:
- Summarise detailed attributes - for instance, turn addresses into postcodes, and DOBs into age categories
- Aggregate information, by compiling group profiles with average info concerning members in those groups
- Perturb - don't process the exact value of some item, instead use an approximation, or adjust it with some random noise. For instance, reporting someone's location with added noise
Homomorphic encryption is an approach which encrypts data without learning the real unencrypted data. The $k$-anonymity principle demands that a piece of data is cloaked such that it could apply to at least $k$ different people, so $k-1$ people including yourself if the data belonged to you.

##### Hide
==Protect personal data, or make it unlinkable/unobservable. Make sure it doesn't become public or known== - the following tactics apply:
- Restrict access to personal data, by ensuring its properly protected through control policies
- Obfuscate data through encryption, so it is not understandable if wrongfully accessed anyway
- Dissociate any correlation between events, persons and data, by removing identifying data
- Mix personal data and anonymise it 
Attribute-based credentials (ABCs) can be used to prove one possesses such an attribute without revealing any other sensitive attributes - they can't be linked to one another

### process oriented strategies
##### Inform
==Inform data subjects about the processing of their personal data in a timely and adequate manner== - the aim is to provide transparency about which personal data is being processed, to allow users to make better informed decisions about using a system, and allow society as a whole to verify whether organisations are processing personal data responsibility. Transparency can be achieved through:
- supplying info on which personal data is processed, how, and why, as well as how long it is retained for, and any third parties the data is shared with
- explaining which personal data is processed and why (similar to supplying info) - make this clear and easy to understand for all groups of people
- notify users when personal data is processed, shared, leaked, through clearly defined procedures
A personal privacy dashboard which clearly shows users how data is collected is preferable - iOS also shows notifications whenever apps access location services - this is an example of an 'ambient notification'.

##### Control
==Provide data subjects adequate control over the processing of their personal data== - the following tactics can give users a say on how their personal data is used/shared:
- ask users explicitly for consent to the processing of their personal data, and explain how it will be used/processed
- still offer users basic functionality if they don't consent to the processing of their data
- offer users the means to update and review how their personal data is collected/used (through a dashboard)
- always offer the means for a user to delete their personal info from the system
Consent isn't always required, if there is a legitimate interest to process it (always consent a lawyer). Prefer to provide the option to opt-in, rather than opt-out (i.e. don't use pre-checked checkboxes). Customer managed relations is where organisations offer users the ability to store personal data themselves, which the app can access under the control of the user.

##### Enforce
==Commit to processing personal data in a privacy-friendly way, and adequately enforce this== - this should be done through a clear privacy policy, which can be achieved with the following tactics:
- create a privacy policy, determining the goal of each process involving data and whether it is a legitimate interest or not
- maintain the policy with necessary technical/organisational controls
- reverify the privacy policy regularly, and adjust it as necessary
The privacy policy should be aligned with the overall business plan and mission statement, and consistent with any other policies. A common approach is to implement a system similar to the plan-do-check-act cycle from the information security management standard. Sticky policies are policies attached to a particular data item, so processes will automatically verify policies which accord with the data provided. Registering 'unusual' activity and blocking access when necessary is also a common tactic.

##### Demonstrate
==Demonstrate you are processing personal data in a privacy-friendly way== - organisations should demonstrate compliance through the following tactics:
- document all steps taken with data, as well as decisions made + system logs
- audit the logs regularly, as well as organisational processes
- report the results of audits to the Data Protection Authority, or keep them for later reference
Getting certified against a recognised standard for privacy friendliness, and performing a data protection impact assessment (DPIA) can also be helpful for demonstrating data processes.

### applying privacy design strategies
The system development/deployment process is a cycle with multiple phases:
- ideation
- definition
- design
- development
- deployment
- operation
- evaluation
- decommissioning
Make sure all stakeholders involved with the project, as well as the end users, are represented, in order to take the perspective of both the data controller and data subjects into account. Apply the strategies one by one, and put more emphasis on applying strategies which are more suitable to a given context. Consider personal data as well as metadata (inadvertently collected data)