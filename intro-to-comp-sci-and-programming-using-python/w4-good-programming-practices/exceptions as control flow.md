## when should I raise an exception?
when unable to produce a result **consistent** with function's specification
## assertions
- an example of [defensive programming](https://en.wikipedia.org/wiki/Defensive_programming)
- achieved through the `assert` keyword
- typically used:
	- check types
	- check that invariants on data structures are met
	- check constraints on return values
- example:
```python
def avg(grades):
	assert not len(grades) == 0, 'no grades data'
	return sum(grades)/len(grades)
```