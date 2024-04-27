They have:
- `name`
- `parameters` (0 or more)
- `docstring` (optional)
- `body`

Example:
```python
def is_odd(number):
	"""
	Input: number, a positive integer
	Returns True if number is odd, otherwise False
	"""
	print("hi")
	return i % 2 != 0
```

```python
def {name}(0 or more parameters):
	"""
	docstring
	"""
	{body}
```

## Specifications
Achieved through the `docstring`
## Iteration vs recursion
- Recursion: program calls itself
	- Must have 1 or more base cases that are easy to solve and end the recursion
- Iteration: looping constructs
### Example with factorial
#### Recursion
```python
def factorial(n):
	"""
	n: a number greater than or equal than zero
	"""
	if n == 1 or n == 0:
		return 1
	else:
		return n*factorial(n-1)
```
#### Iteration
```python
def factorial(n):
	"""
	n: a number greater than or equal than zero
	"""
	prod = 1
	for i in range(1, n + 1):
		prod *= 1
	return prod
```