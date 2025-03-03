from config.database import get_connection


def create_user(username, email, password_hash):
    """
    Create a new user in the database

    Returns: The ID of the newly created user
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (username, email, password_hash),
    )

    # Get the ID of the newly inserted user
    # Should change this later
    user_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return user_id


def get_user_by_id(user_id):
    """
    Get a user by their ID

    Returns: User dict or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()

    return user


def get_user_by_username(username):
    """
    Get a user by their username

    Returns: User dict or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()

    return user


def get_user_by_email(email):
    """
    Get a user by their email

    Returns: User dict or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    conn.close()

    return user
