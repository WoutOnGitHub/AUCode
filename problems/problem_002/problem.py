"""
Problem description:
Check if a given input is a palindrome.

A palindrome is a string that reads the same forward and backward, ignoring case, spaces, and punctuation.
For example, "A man, a plan, a canal: Panama" is a palindrome because when you strip away spaces,
punctuation, and ignore letter case, it reads the same in both directions.

- If input is a string, check if it's a palindrome after removing spaces, punctuation, and ignoring case
- If input is a number, check if its string representation is a palindrome
- If input is a list, check if the list reads the same forward and backward
"""

from hashlib import sha256

# List of inputs
inputs = [
    "racecar",  # Simple palindrome
    "A man, a plan, a canal: Panama",  # Palindrome with spaces and punctuation
    "hello",  # Not a palindrome
    12321,  # Numeric palindrome
    [1, 2, 3, 2, 1],  # List palindrome
    [1, 2, 3, 4, 5],  # Not a palindrome
    "",  # Empty string (is a palindrome)
    "Madam, I'm Adam.",  # Another punctuated palindrome
    "Was it a car or a cat I saw?",  # Complex palindrome
]


def is_palindrome(x):
    """
    Check if the input is a palindrome.

    For strings: Ignore case, spaces, and punctuation.
    For numbers: Check if the number reads the same forward and backward.
    For lists: Check if the list is the same forward and backward.

    Examples:
        is_palindrome("racecar") -> True
        is_palindrome("hello") -> False
        is_palindrome(12321) -> True
        is_palindrome([1,2,3,2,1]) -> True
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
        res.append(is_palindrome(i))
    res = str(res)
    return sha256(res.encode("utf-8")).hexdigest()[:8]


# Print final hash (To be submitted)
print(test_func(inputs))
