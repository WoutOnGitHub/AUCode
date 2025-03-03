from functools import wraps

from flask import flash, redirect, session, url_for


def login_required(f):
    """
    Decorator to ensure a user is logged in before accessing a route
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to access this page")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function


def is_authenticated():
    """
    Check if the current user is authenticated
    """
    return "user_id" in session


def get_current_user_id():
    """
    Get the ID of the current user
    """
    return session.get("user_id")


def get_current_username():
    """
    Get the username of the current user
    """
    return session.get("username")
