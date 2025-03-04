# Palindrome Checker

## Problem Description

A palindrome is a sequence that reads the same forward and backward. Your task is to implement a function that checks if a given input is a palindrome, with the following rules:

- For strings: Ignore case, spaces, and punctuation when checking
- For numbers: Check if the digits read the same forward and backward
- For lists: Check if the list elements are the same when read forward and backward

## Examples

```python
is_palindrome("racecar") -> True
is_palindrome("A man, a plan, a canal: Panama") -> True
is_palindrome("hello") -> False
is_palindrome(12321) -> True
is_palindrome([1, 2, 3, 2, 1]) -> True
is_palindrome([1, 2, 3, 4, 5]) -> False
```

## Constraints

- Input can be a string, integer, or list
- Strings will have a maximum length of 1,000 characters
- Integers will be within the range of -10^9 to 10^9
- Lists will have a maximum of 1,000 elements

## Tips

- For strings, you'll need to remove spaces and punctuation, and convert to a consistent case before checking
- An empty string is considered a palindrome
- Remember that for negative numbers, the negative sign makes the number not a palindrome (e.g., -121 is not a palindrome)
