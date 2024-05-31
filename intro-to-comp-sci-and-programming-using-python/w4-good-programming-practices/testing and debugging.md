>[!Nice takeaway]
>Use binary search when debugging. 
>Pick halway of code and devise experiment.
>Place a print statement or breakpoint
>Compare expected vs actual
>Repeat as in binary search
## tests
### classes
#### unit
- validate a concrete piece of the program
- testing each function separately
#### regression
- add tests for bugs as you find them
- catch reintroduced errors that were previously fixed
#### integration
- testing of the overall program
### types
#### black box
- without looking at the _code_
- just having input and expected output
#### glass box
- use code directly to guide design of tests
- test cases are defined so we test each path inside the code (every if, elif, else, etc.)
## bugs 🐞
### runtime bugs
#### overt vs covert
- overt are obvious, code crashes
- covert have no obvious manifestation -> code returns a value but not a correct one
#### persistent vs intermittent

|                        |                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------- |
| overt and persistent   | easier to debug, use **defensive programming**                                                            |
| overt and intermittent | frustrating and harder to debug, have to find the conditions to be reproduced                             |
| covert                 | highly dangerous, sometimes it takes time to detect them even after code has been running for a long time |
