# Generator of math problems.

### The main function is problem_gen.
```python
problem_gen(level, diff=False, mult=False, div=False)
```
### Returns random math problem.

| **Parameters**           | description                                                                                                 |
| :----------------------- | :---------------------------------------------------------------------------------------------------------- |
| level : int              | Problem difficulty level. <br />The larger the number, the longer the problem and the larger numbers in it. |
| diff : bool, optional    | If provided True, difference will be in the problem. <br />See above for behavior if `diff=False`.          |
| mult : False, optional   | If provided True, multiplication will be in the problem. <br />See above for behavior if `mult=False`.      |
| div : False, optional    | If provided True, divdivision will be in the problem. <br />See above for behavior if `div=False`.          |
