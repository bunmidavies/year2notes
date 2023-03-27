[[COMP23412]]

- ==a high level definition of software testing is==: a process by which software functionality and quality is assessed


### categories of software testing
- there are two main categories of software testing:
	- ==validation== - have we built the right software, and does it fulfil the users requirements?
	- ==verification== - have we built the software correctly, and is it free of defects/failures?
- not all software defects are coding errors (for instance, scaling issues), and not all software defects result in failure (e.g. dead code)

- there are 2 main testing methods concerning whether the code is run or not:
	- ==static analysis== - code is not run, e.g. code review, inspecting the code line by line
	- ==dynamic analysis== - code is run, e.g. automatic test suite
- there are 2 main testing methods concerning whether the internals of a function are visible:
	- ==white-box testing== - internal functions are tested, and we care about ==how== something is doing what it does
	- ==black-box testing== - internal functions aren't of concern - ==what== something does is more important than how it does it

### levels of software testing

![ | 450](https://i.imgur.com/gvtQRlj.png)
- ==unit testing==: making sure the code itself works in isolation
- unit tests find problems early, making them cheap and easy to fix - they also provide documentation and allow for easier integration
- however, not everything can fully be tested with unit testing, due to the sheer size that the test suite would have to grow to. Things like non deterministic functions also cannot be tested

- ==integration testing==: making sure larger blocks of code work correctly, design to expose flaws in interactions between different units

- ==system testing==: making sure systems work from end to end
- there are many types of system test, and many are difficult to automate, e.g. performance, accessibility, security, load etc.


- ==acceptance testing==: testing from the perspective of the user
- user stories typically outline some type of requirement, and the aim is to make the system work for these users

- ==regression test==: catching bugs and defects, throughout development and maintenance

- the categories of software testing can then be identified as different levels

![ | 450](https://i.imgur.com/chbmjDQ.png)
