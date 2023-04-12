[[COMP23311]] `week 1`

There are various steps involved when building and testing open source software, or any kind of software that may belong to a company

==Acquiring the Source Code== - This is typically done by ==cloning== a remote repository. In eclipse the option to do this exists in `File > Import > Git > ImportFromGit`, 

==Build the Object Code== - Building is ==not the same as Compiling==, as there may be additional processes that take place within a build
We ideally want ==1 build process== with the options to deploy to ==dev==, ==test==, or ==live== - Build automation tools like Maven, Ant, make etc. help to make the process easy and repeatable

In the COMP23311 workshops, we use Ant - typically any kind of Ant build is run using the `Run As > Ant Build` option - Ant build files and results are typically written in ==XML==

==Running tests== - Most release pipeline gateways include code review, documentation, and automated tests

==Test coverage== is also used to indicate how many instructions within a package have been tested
