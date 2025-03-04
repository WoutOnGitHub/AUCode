"""
Database configuration for AUCode.
"""

# Database configuration - SQLite by default
DATABASE = {
    "engine": "sqlite3",
    "name": "aucode.db",
    "user": "",
    "password": "",
    "host": "",
    "port": "",
}


def get_connection():
    """Get a database connection"""
    if DATABASE["engine"] == "sqlite3":
        import sqlite3

        conn = sqlite3.connect(DATABASE["name"])
        conn.row_factory = sqlite3.Row
        return conn
    else:
        raise ValueError(f"Unsupported database engine: {DATABASE['engine']}")


def create_tables():
    """Create database tables if they don't exist"""
    conn = get_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create problems table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        problem_folder TEXT NOT NULL,
        correct_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create submissions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        problem_id INTEGER NOT NULL,
        solution_hash TEXT NOT NULL,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_correct BOOLEAN NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (problem_id) REFERENCES problems (id)
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
