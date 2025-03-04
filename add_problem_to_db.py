"""
Messy temporary file which you can use to create problems
"""

from app.models.problem import create_problem

# Add Problem 1
with open("problems/problem_001/description.md", "r") as f:
    description = f.read()

correct_hash = "f8e96cdc"  # Hash generated using the solution above
create_problem("Sum of Even Numbers", "problem_001", correct_hash)

# Add Problem 2
with open("problems/problem_002/description.md", "r") as f:
    description = f.read()

correct_hash = "5e27b49f"  # Hash generated using the solution above
create_problem("Palindrome Checker", "problem_002", correct_hash)
