# Flask Coding Challenge Website (MVP)

This is a Minimum Viable Product (MVP) for a web application that hosts coding challenges, built using Flask and Python.

Users can register, view programming problems, download starter files, solve the problems locally, and submit a unique code generated from their solution's test results to earn points.

## Key Features

- User registration and login.
- Viewing available coding problems.
- Downloading Python starter files for each problem.
- Unique client-side solution verification mechanism.

## Solution Verification Mechanism

To avoid the security risks and resource load of running user-submitted code on the server, this application uses a client-side verification approach:

1.  The user downloads a Python file containing the problem description, a function stub to implement, and a series of test cases.
2.  The user implements their solution within the provided function stub.
3.  Running the downloaded Python file executes the user's solution against all the test cases.
4.  The results (e.g., True/False for each test case, or specific outputs) are concatenated into a single string.
5.  This string is hashed using SHA256.
6.  The script prints the first 8 characters of the resulting hexadecimal SHA256 hash.
7.  The user submits these 8 characters back to the website.
8.  The website compares the submitted hash prefix against the expected prefix for a correct solution to award points.

## Setup and Run Locally

Follow these steps to set up and run the application on your local machine (commands are for linux/mac):

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/WoutOnGitHub/AUCode.git
    cd AUCode
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    # On Windows use `env\Scripts\activate`
    # On Linux/macOS use:
    . ./env/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database with sample problems:**

    ```bash
    # This script adds the initial problems to the database
    python add_problem_to_db.py
    ```

5.  **Run the Flask application:**

    ```bash
    python run.py
    ```

6.  **Access the website:**
    Open your web browser and navigate to `http://127.0.0.1:5000` (or the address provided by Flask). You can now register an account and start solving the two test problems available.

## Technologies Used

- Python
- Flask
- SQLite (default database)
- HTML/CSS (basic frontend)
