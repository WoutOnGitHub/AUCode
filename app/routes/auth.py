from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.user import create_user, get_user_by_username
from app.utils.auth_helpers import login_required

# Create a Blueprint for authentication routes
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        # Check which form was submitted
        if "register" in request.form:
            # Handle registration
            username = request.form.get("reg_username")
            email = request.form.get("reg_email")
            password = request.form.get("reg_password")

            # Basic validation
            if not username or not email or not password:
                flash("All registration fields are required")
                return render_template("auth.html")

            # Check if user already exists
            existing_user = get_user_by_username(username)
            if existing_user:
                flash("Username already exists")
                return render_template("auth.html")

            # Create new user
            password_hash = generate_password_hash(password)
            user_id = create_user(username, email, password_hash)

            flash("Registration successful! You can now log in.")
            return redirect(url_for("auth.auth"))

        elif "login" in request.form:
            # Handle login
            username = request.form.get("login_username")
            password = request.form.get("login_password")

            # Validate input
            if not username or not password:
                flash("Both username and password are required")
                return render_template("auth.html")

            # Check if user exists
            user = get_user_by_username(username)
            if not user or not check_password_hash(user["password_hash"], password):
                flash("Invalid username or password")
                return render_template("auth.html")

            # Set user session
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            flash(f"Welcome back, {username}!")
            return redirect(url_for("index"))

    return render_template("auth.html")


@auth_bp.route("/logout")
def logout():
    # Clear the session
    session.clear()
    flash("You have been logged out")
    return redirect(url_for("index"))
