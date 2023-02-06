[[COMP26120]]

# Week 3 - Divide and Conquer

- Divide and conquer algorithms typically have 3 steps
	1. Divide into n subproblems
	2. Operate on each subproblem individually
	3. Combine subproblems to create final solution

### The merge sort algorithm
- The basic merge sort algorithm looks like such:
```
MergeSort(A, left, right)
{
	if (left < right)
	{
		mid = floor((left + right) / 2);
		MergeSort(A, left, mid);
		MergeSort(A, mid+1, right);
		Merge(A, left, mid, right);
	}
}
```
- The `Merge` function itself is as follows:
```
Merge(A, left, mid, right)
{
	n1 = mid - left + 1
	n2 = right - mid
	initialise arrays L[0,n1] and R[0, n2]
	for (i = 0; i < n1; i++)
	{
		L[i] = A[left + i]
	}

	for (j = 0; j < n2; j++)
	{
		R[j] = A[mid + j + 1]
	}

	i = 0
	j = 0
	for (k = left; k < right; k++)
	{
		if (L[i] <= R[j])
		{
			A[k] = L[i]
			i++;
			
		}
	}
}
```