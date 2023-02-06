[[COMP23311]] `week 7`

[notes reference](https://software-eng.netlify.app/reviewing.html)

==code review involves 1 person's code being inspected by another person/group==

the core idea behind code review is that it is is easier to spot problems in code written by ==someone else==, than your own code

*the reason for this relates to the fact that after we write some code, the idea of what the code should be doing is fresh in our minds. It can be difficult to see the discrepancies between what we think the code should be doing and what its actually doing*

studies have shown that code review can find up to 60% of defects, while unit testing only finds 25%. Code review is more expensive in terms of time compared to unit testing, but can find a wider range of defects in code in comparison to testing

code review also helps to spread knowledge of the code base + coding styles throughout a team when people review other peoples code - this reduces the occurence of some piece of code existing which only one person is an expert on (further problems arise if they ever end up leaving)

==typical code reviews 100-200 lines of code/hour for experienced professionals== 

==in a typical team, one can expect to spend 1-5 hours a week reviewing code==

When performing a code review, the following aspects of code can be commented on:
- Possible defects
- Possible flaws in testing
- Design issues
- Naming issues
- Coding style issues
- Presence of code/test smells
- Use of Git
- Comments on the build
- Effect on team metrics (e.g. code coverage being affected)
- Examples of good practice

There are ==3 main types== of code review

### Buddy Review

- ==informal review==, involving coders with the same status in a team, done on an as needed basis

### Team-Based Review

- Many teams will require the code in a feature branch to be reviewed by another team before it can be merged in 
- A common technique is the 'walkthrough', which is a meeting with affected team members, where 1+ members presents what has been done and how it works

### Formal Review

- Work is inspected by an ==external team==
- Mainly only really performed in large companies, involving extensive documentations and presentations

### <span style="background-color:#797ca3;padding:3px;border-radius:5px;">Good Practice for Code Reviewers</span>

- Code reviewers should adopt a neutral tone
- Balance out negative points with positive comments
- ==promiscuous reviewing== - buddy pairings should change over time, to avoid bias and any kind of "revenge reviews"