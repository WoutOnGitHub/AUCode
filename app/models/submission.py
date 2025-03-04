from config.database import get_connection


def create_submission(user_id, problem_id, solution_hash, is_correct):
    """
    Create a new submission in the database

    Returns: The ID of the newly created submission
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO submissions (user_id, problem_id, solution_hash, is_correct) VALUES (?, ?, ?, ?)",
        (user_id, problem_id, solution_hash, is_correct),
    )

    # Get the ID of the newly inserted submission
    submission_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return submission_id


def get_submission_by_id(submission_id):
    """
    Get a submission by its ID

    Returns: Submission dict or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM submissions WHERE id = ?", (submission_id,))
    submission = cursor.fetchone()

    conn.close()

    return submission


def get_submissions_by_user(user_id):
    """
    Get all submissions by a user

    Returns: List of submission dicts
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM submissions WHERE user_id = ? ORDER BY submitted_at DESC",
        (user_id,),
    )
    submissions = cursor.fetchall()

    conn.close()

    return submissions


def get_submissions_by_problem(problem_id):
    """
    Get all submissions for a problem

    Returns: List of submission dicts
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM submissions WHERE problem_id = ? ORDER BY submitted_at DESC",
        (problem_id,),
    )
    submissions = cursor.fetchall()

    conn.close()

    return submissions


def get_user_problem_submission(user_id, problem_id):
    """
    Get a user's submission for a specific problem

    Returns: Submission dict or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM submissions WHERE user_id = ? AND problem_id = ? ORDER BY submitted_at DESC LIMIT 1",
        (user_id, problem_id),
    )
    submission = cursor.fetchone()

    conn.close()

    return submission


def get_leaderboard():
    """
    Get the leaderboard with user data and number of correct submissions

    Returns: List of dicts with user data and submission count
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT u.id, u.username, COUNT(s.id) as correct_count
        FROM users u
        JOIN submissions s ON u.id = s.user_id
        WHERE s.is_correct = 1
        GROUP BY u.id
        ORDER BY correct_count DESC
    """)

    leaderboard = cursor.fetchall()

    conn.close()

    return leaderboard
