[[COMP26120]]

- a binary heap is a special type of [[binary heap]]
- a min / max heap have different invariants:
	- min heap: each node value is greater than that of its parent
	- max heap: each node value is less than that of its parent

## max heapify algorithm
```python
# heap is being represented using an array
maxHeapify(H, i):
	largest = i #index of the largest element 
	l = H.left(i)
	r = H.right(i)

	if r < H.heapSize and H[l] > H[largest]:
		largest = l
	if r < H.heapSize and H[r] > H[largest]:
		largest = r
	if largest != i:
		swap H[i] and H[largest]
		maxHeapify(H, largest) # recursive call
```

- max heapify can be used to build any array / binary tree into a max heap

## complexities
[[binary heap complexities]]