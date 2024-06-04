any procedure or method with `yield` statement is called a **generator**
```python
def genTest():
	yield 1
	yield 2
```
they also have a `next()` method which starts or resumes the execution of the procedure
in the previous case if I do
```python
foo.__next__()
>1
```
and if I call it again
```python
foo.__next__()
>2
```
calling a generator after all yields have been called lead to a StopIteration exception
## why use them?
- they separate computing a very long sequence of objects from the process of computing them explicitly
- similar idea to `range`
- instead of having *all* fibonacci numbers, we use a generator and then ask for the 13th if we wanted that
- https://stackoverflow.com/questions/102535/what-can-you-use-generator-functions-for