"""
Problem description:
Calculate the sum of all even numbers in a list or range of numbers.

- If given a single integer, sum all even numbers from 0 up to and including that number
- If given a list, sum all even numbers in the list
- Empty lists should return 0
"""

from hashlib import sha256

# List of inputs
inputs = [
    10,  # Sum of even numbers from 0 to 10
    [1, 2, 3, 4, 5, 6],  # Sum of even numbers in the list
    [],  # Empty list
    [1, 3, 5, 7],  # List with no even numbers
    [2, 4, 6, 8],  # List with only even numbers
    100,  # Sum of even numbers from 0 to 100
    -10,  # Negative number (should handle appropriately)
]


def sum_even_numbers(x):
    """
    Calculate the sum of all even numbers.

    If x is an integer, sum all even numbers from 0 to x inclusive.
    If x is a list, sum all even numbers in the list.

    Examples:
        sum_even_numbers(10) -> 30 (0+2+4+6+8+10)
        sum_even_numbers([1,2,3,4]) -> 6 (2+4)
    """
    # Implement your solution here
    pass


def test_func(inputs):
    """
    Collects the output of your function on all provided inputs.
    Then hashes all of that and returns the first 8 characters of the hash.
    Submit this hash to see if your code is correct!
    """
    res = []
    for i in inputs:
        res.append(sum_even_numbers(i))
    res = str(res)
    return sha256(res.encode("utf-8")).hexdigest()[:8]


# Print final hash (To be submitted)
print(test_func(inputs))
