[[COMP25212]]

- there are 3 main types of data dependencies, which can typically occur due to out of order execution within [[out of order processors]]
- the names are pretty self explanatory

### true dependencies
- these are known as ==read-after-writes== (RAW)
```Pug
r1 = r2 op r3
r4 = r1 op r5
```

### anti-dependencies
- these are known as ==write-after-reads== (WAR)
```Pug
r1 = r2 op r3
r2 = r4 op r5
```

### output dependencies
- these are known as ==write-after-writes== (WAW)
```Pug
r1 = r2 op r3
r1 = r4 op r5
```