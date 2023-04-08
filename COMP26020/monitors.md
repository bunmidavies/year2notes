[[COMP26020]]

### ~ definition
- monitors consist of a ==lock object== and ==condition variables== - they can implement mutual exclusion using the lock, but also make threads wait for an ==external condition== to be true, which may have nothing to do with mutual exclusion
- for this reason, monitors can allow threads to have both mutual exclusion, but also cooperation

### ~ links
- [stack overflow thread on locks / monitors](https://stackoverflow.com/questions/49610644/in-java-what-is-the-difference-between-a-monitor-and-a-lock)