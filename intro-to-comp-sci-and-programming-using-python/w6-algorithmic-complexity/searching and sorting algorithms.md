## linear search
- list doesn't have to be sorted
- brute force search
## bisection search
- list must be sorted

>[!when is it worth it to sort and then use bisection search?]
>If you are only going to search once never. Because no sort algorithm is less than $O(n) - O(log n)$
>But if we are going to search many times after sorting then it is worth it to sort the list first.
## bubble sort
### complexity
- $O(n^2)$ where $n$ is $len(list) - 1$
## selection sort
### complexity
- $O(n^2)$ where $n$ is $len(list) - 1$

- extract minimum element, then swap with index 0
	- then in remaining sublist without index 0, do the same repeatedly
- the while loop keeps track of what point of the list we currently are with a pointer ("suffixSt" in the example)
```python
def selection_sort(L):
	suffixSt = 0
	while suffixSt != len(L):
		for i in range(suffixSt, len(L))_
			if L[i] < L[suffixSt]:
				# SWAP
				L[suffixSt], L[i] = L[i], L[suffixSt]
		suffixSt += 1
```
## merge sort
- uses **divide & conquer** approach
- repeatedly split list until we have only one number on each list
- **merge** each list putting lower value first
### complexity
- $O(nlog (n))$ 🎉

```python
def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right): # until one of the list is exhausted
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	# copy remaining sublist
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1

	return result
```

```python
def merge_sorty(L):
	if len(L) < 2: # base case
		return L[:]
	else:
		middle = len(L)//2
		left = merge_sort(L[:middle])
		right = merge_sort(L[middle:])
		return merge(left, right)
```
