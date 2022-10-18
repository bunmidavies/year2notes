# Algorithmic Complexity
***
### Video 1 - Introducing Complexity Analysis (revision)

- Motivating example = bubble sort
- Time complexity of bubble sort = $O(n^2)$
- Time complexity involves performing worst cases analysis and ignoring constants
- Goes through different algorithms and their runtimes, demonstrates merge sort having logarithmic time complexity
***
### Video 2 - Asymptotic Performance

- In this course **we care the most about asymptotic performance**
- We focus on the **infinite set of large n**, ignoring very small values of n
- We want to know how algorithms behave as the problem size scales, behaviour includes factors like
	- Running time
	- Memory usage
	- Bandwidth/power usage
- Example: Linear Search:
	- Worst case = $f(n) = n$
	- Average case = $n/2$
- Example: Binary Search
	- Worst case = $f(n) = log(n)$

- Analysis is performed with a computational model in mind - a generic uniprocessor where **all memory is equally as expensive to access**, there is **no concurrency**, all builtin instructions take **unit time**, and there is a **constant word space**

- **Worst Case vs Average Case**
	- Worst case provides an upper bound on running time, i.e. an **absolute guarantee** of what the running time could scale to
	- Average case provides expected running time, which is arguably more useful, but how do we know what is 'average' for all algorithms?
***
### Video 3 - Analysing Insertion Sort

Insertion sort code:
```
InsertionSort(A, n)
{
	for (int i = 1; i <= n)
	{
		int key = A[i];
		int j = i - 1;
		while (j > 0) and (A[j] > key)
		{
			A[j+1] = A[j]
			j--;
		}
		A[j+1] = key
	}
}
```

- While analysing complexity we need a precondition and a postcondition
- As well as this we need an invariant, i.e. some kind of property that is going to hold through the iterations

- **In COMP26120 we're not focusing on average case scenarios - we're only really focusing on worst / best case scenarios, and producing time complexities for these**

***
### Video 4 - Upper / Lower Bounds

- **Big O defines the UPPER BOUND of a function**
	- $f(n)$ is $O(g(n))$ if there exists positive constants $c$ and $n_0$ such that $f(n) \leq c \cdot g(n)$ for all $n \geq n_0$
- $\Omega$ **defines the LOWER BOUND of a function**
- $\Theta$ **defines the AVERAGE CASE of a function** (i.e. time lies within two bounds)