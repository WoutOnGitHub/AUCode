import os

from config.settings import PROBLEMS_DIR


def get_problem_description(problem_folder):
    """Read the problem description markdown file"""
    desc_path = os.path.join(PROBLEMS_DIR, problem_folder, "description.md")
    try:
        with open(desc_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Problem description not found."


def get_problem_file_path(problem_folder):
    """Get the path to the problem Python file"""
    return os.path.join(problem_folder, "problem.py")


def get_problem_absolute_file_path(problem_folder):
    """Get the absolute path to the problem Python file"""
    return os.path.join(PROBLEMS_DIR, problem_folder, "problem.py")
