- there is usually a trade-off between the **time** efficiency and **space** efficiency of a program
## how to evaluate efficiency of programs
- measure with a timer
	- varies between implementations
	- varies between computers
	- not predictable on small inputs
- count the operations
	- varies between computers too
	- independent from computers
	- no real definition of which operations to count
- **abstract notion of order of growth** -> this is the more appropriate
## evaluate efficiency through an abstraction notion of order of growth
- we say "order of", not exact
- we evaluate when input is very big
### types
- constant ✔✔✔
- logarithmic ✔✔
- linear ✔
- n log n ➖
- quadratic ❌
- exponential ❌❌
### big O notation
- measures the upper bound on the asymptotic growth
- constants and multiplicative factors are dropped, we focus on **dominant terms**
- for example: $n^2+2^n+2$ turns into $O(n^2)$
#### constant complexity
- $O(1)$
- very few algorithms fit this class
#### logarithmic complexity
- $O(logN)$
- examples:
	- bisection search
	- binary search of a list
#### linear complexity
- $O(n)$
- examples:
	- search a list in sequence for an element
#### polynomial/quadratic complexity
- $O(n^2)$
- most common polynomial are of this class
- **nested** loops or recursive function calls
#### exponential complexity
- $O(2^n)$
- examples:
	- towers of Hanoi
	- fib recursively