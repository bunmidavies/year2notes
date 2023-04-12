[[COMP23311]] `week 3`

In code, there are two main types of errors:
- ==synatactical errors== - easy to deal with most of the time; missing brackets, missing semicolons, forgeting an import etc. IDEs will throw these up
- ==semantic/conceptual errors== - the language used is correct, but the code does not work ==as intended==. This is buggy behaviour, but the IDE will not complain 

Software bugs refer to ==any flaw in a codebase== - *the term originates from a live bug being found inside a calculator being developed in the 1940s, causing the device to behave strange*

==Debugging== is the process of discovering, locating and fixing bugs - there exists a systematic approach for it:
1. ==Start with a problem== - confirm the reported problem by ==replicating it==. You should try to recreate the same conditions under which the bug occured, make sure you understand the expected behaviour and observe the actual behaviour

2. ==Stabilise the problem== - narrow down the problem to as ==precise== of a statement as possible (use what has been observed in the previous step)

3. ==Isolate the source of the problem== - typically the most important step, as you will be identifying ==where the bug occurs in the code==
   There are a number of different strategies which exist - e.g. brute force, back tracking, binary search, cause elimination. Brute force is the longest method, which involves just going line by line in the code
   There are also tactics e.g. print statements, break points, test cases, rubber ducking (explaining exactly what the code is doing)
   It is normal to usually combine a strategy and tactic e.g. cause elimination + print statements

4. ==Fix the problem== - once the bug has been identified in code this part is usually straightforward

5. ==Test the fix== - run the tests which you already have to ensure other functionality has not been affected

6. ==Look for similar errors== - try to find another occurence of the method which has been modified. This code should behave as intended

[the 11 truths of debugging (on page 2) - Nick Parlante](https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1184//handouts/9%20-%20Debugging.pdf)