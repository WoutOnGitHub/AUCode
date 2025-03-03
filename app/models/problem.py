from config.database import get_connection


def create_problem(title, description, file_path):
    """
    Create a new problem in the database

    Returns: The ID of the newly created problem
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO problems (title, description, file_path) VALUES (?, ?, ?)",
        (title, description, file_path),
    )

    # Get the ID of the newly inserted problem
    problem_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return problem_id


def get_problem_by_id(problem_id):
    """
    Get a problem by its ID

    Returns: problem dict or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems WHERE id = ?", (problem_id,))
    problem = cursor.fetchone()

    conn.close()

    return problem


def get_all_problems():
    """
    Get all problems

    Returns: List of problem dicts
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems ORDER BY created_at DESC")
    problems = cursor.fetchall()

    conn.close()

    return problems


def delete_problem(problem_id):
    """
    Delete a problem

    Returns: True if successful, False otherwise
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM problems WHERE id = ?", (problem_id,))

    success = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return success
