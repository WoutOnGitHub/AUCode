"""
Problem description:
Place the problem description here. Be very precise!
"""

from hashlib import sha256

# List of inputs
inputs = [
    # Example inputs will go here
    1,
    2,
    "test",
    [1, 2, 3],
]


def func_to_implement(x):
    """
    Implement your function here
    """
    return x


def test_func(inputs):
    """
    Collects the output of your function on all provided inputs.
    Then hashes all of that and returns the first 8 characters of the hash.
    Submit this hash to see if your code is correct!
    """
    res = []
    for i in inputs:
        res.append(func_to_implement(i))
    res = str(res)
    return sha256(res.encode("utf-8")).hexdigest()[:8]


# Print final hash (To be submitted)
print(test_func(inputs))
