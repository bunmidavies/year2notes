[[COMP23311]]

***

### risk

==software risk== is an event which ==has not happened yet==, and has ==negative== consequences for a software project

risks ==might happen== - any event that definitely will happen is not considered a risk

==risk exposure== is the measure of potential future loss resulting from some event. Risks can typically be measured by the product of their probability and loss if occurs

***

### mitigation

==mitigation planning== means taking steps to ensure risks are ==less likely== to occur, or to reduce the impact of such risks

***

### contingency

==contingency planning== involves setting up a plan of action for when some severe risk occurs. ==It has no effect on the likelihood of the risk occuring==

Resources can be set aside to cope with severe risks occuring, preventing any time from being wasted if the risk occured without preparation beforehand

***

### git for risk management

git mitigates/removes a number of possible risks when developing software:
- loss of data on local device
- loss of work when one file overwrites another file

***

### continuous integration servers for risk management

==CI servers==(i.e. pipelines in gitlab) can mitigate one of the main risks in software development - accidentally pushing buggy code which doesn't work. Continuous integration can run automatic builds on feature branches, to prevent branches which fail tests from being able to merge into a main branch

==Automated test suites== achieve a similar goal
