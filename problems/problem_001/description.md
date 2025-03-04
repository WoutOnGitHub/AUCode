# Sum of Even Numbers

## Problem Description

Write a function that calculates the sum of all even numbers according to the following rules:

- If given a single integer `n`, sum all even numbers from 0 up to and including `n`
- If given a list, sum all even numbers in the list
- Empty lists should return 0
- Negative numbers should be handled appropriately (i.e., for negative integers, there are no even numbers to sum)

## Examples

```python
sum_even_numbers(10) -> 30  # Sum of 0+2+4+6+8+10
sum_even_numbers([1,2,3,4,5,6]) -> 12  # Sum of 2+4+6
sum_even_numbers([]) -> 0  # Empty list returns 0
sum_even_numbers([1,3,5,7]) -> 0  # No even numbers in the list
```

## Constraints

- You can assume that all inputs will be either integers or lists of integers
- List inputs will not contain more than 1,000 elements
- Integer inputs will be between -10^6 and 10^6

## Tips

- Remember that 0 is considered an even number
- For negative integers, you should sum all even numbers from 0 down to that number
