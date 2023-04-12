[[COMP23311]] `week 2`

**Note that in JUnit, when comparing values, the order is always `expected` followed by `actual` - this means the value you're expecting to see should be the first argument, while the value you recorded is the second argument**

### Annotations

Identify a method as a test

```Java
@Test
```

Fail if the method does not throw the named exception

```Java
@Test(expected = Exception.class)
```

Fail if the test takes longer than 100ms

```Java
@Test(timeout=100)
```

Identify the method to be executed ==before== or ==after== each test, respectively

```Java
@Before
@After
```

Identify the method to be executed before and after ==all tests==, respectively
```Java
@BeforeClass
@AfterClass
```

### Statements

Fail the test
```Java
fail("message")
```

check that a condition is ==true== or ==false==, respectively
```Java
assertTrue("message",condition)
assertFalse("message",condition)
```

check that two values are the same, or with some tolerance for ==doubles==, respectively
```Java
assertEquals("message",value1,value2)
assertEquals("message",double1,double2,tolerance)
```

check that an object is ==null== or ==not null==, respectively
```Java
assertNull("message",object)
assertNotNull("message",object)
```

check that two variables ==refer to the same object== or not, respectively
```Java
assertSame("message",var1,var2)
assertNotSame("message",expected,actual)
```