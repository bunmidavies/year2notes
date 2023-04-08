[[COMP26020]]

### ~ definition
- a data race is ==undeterministic behaviour/output== due to the failure to control [[concurrency]]
- since the output is undeterministic, data races can be hard to detect / reproduce, since the output could have relied on some specific timing or ordering of concurrent operations
- thus, to avoid data races, proper concurrency management techniques are required