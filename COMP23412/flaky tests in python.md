### Definition of flaky test
A flaky test is a test that causes spurious failures without any code changes. These hamper regression testing, increase maintenance cost, can shadow real bugs and reduce trust in tests. Research showed 59% of flaky tests were due to order dependency, 28% due to test infrastructure problems, and 13% due to network/randomness APIs being used. A 95% confidence that a passing test case isn't flaky requires 170 reruns on average.

Some test frameworks support making tests as flaky, thus running them repeatedly before reporting them as actually failed. The problem is that this may mask actual bugs, and wastes resources. Google reportedly spends 2-16% of resources re-running flaky tests.

### Types of flakiness
Luo et al. introduced 10 main categories of flakiness:
- Async Wait
- Concurrency
- Test Order Dependency (one test needs to pass before the other can pass, vice versa)
- Resource Leak
- Network
- Time
- IO
- Randomness
- Floating Point Operations - doesn't apply to python as FP math is always deterministic
- Unordered Collections - whether collections are ordered or not frequently changes in python
There are 5 extra categories:
- Too Restrictive Range
- Test Case Timeout
- Platform Dependency
- Test Suite Timeout
- Infrastructure Flakiness
All categories other than Test Order Dependency can be categories as non-order-dependent

### Test order dependency
When a test $p$ running before another test $t$ disturbs the execution of $t$, we call $p$ a polluter, and $t$ the victim.
When a test $t$ requires test $s$ to run before it, we call $s$ a state-setter, and $t$ a brittle. When $t$ is a victim it can run independently, but will fail if it is a brittle, and the required state isn't set up.

### Mitigating flaky tests
Existing tools for automatically detecting flaky tests include:
- Deflaker - analyses coverage information and test verdicts, thus avoiding retesting
- IDFlakies - applies a smart random-order rerun strategy, allowing it to potentially classify the root cause of flakiness
- PraDet - detects order-dependent flaky tests through dataflow analysis
- IFixFlakies - automatically fixes order-dependent flaky tests by user other test code
- Rootfinder - collects information about test execution to classify non-order-dependent flaky tests

### Aims of the paper
The paper aims to answer the following questions:
1. How frequently does flakiness occur in Python?
2. What types of flakiness are prevalent in Python?
3. What is the degree of flakiness of flaky tests in Python?


### Results + Conclusion
1. Using a dataset of 22352 python projects from PyPI (10% of all projects), 1006 projects had flakiness, with a total of 7571 flaky tests (0.86% of the examined tests) - this is comparable to similar research done on Java, but the reasons for flakiness differ. Flakiness was found to be more common in mature projects, as well as projects in the scientific/engineering domain.
2. 59% of all flakiness was caused by order dependencies, 28% by infrastructure flakiness, and 13% between networking and randomness API usage
3. Flaky tests in python have a low failure rate, resulting in a low number of reruns necessary to check if a failure was flaky (1 rerun for 95% confidence for non-order-dependent flaky tests), but a high number of reruns was necessary to check if a test in general is flaky (170 reruns for 95% confidence for non-order-dependent flaky tests)
More projects were found to be flaky in the java study in comparison to the python study since projects from the java study were specifically chosen because they contained flakiness. The rate of tests being flaky were both similar. Far more victims than brittles were found when investigating order-dependent flakiness - this could be partly due to modern test frameworks allow state setters to be declared actively, restricting possible test orders. Flaky tests are equally as prevalent in the Python ecosystem as they are in the Java ecosystem.

==reread if time==
- iv results
- note down related works?