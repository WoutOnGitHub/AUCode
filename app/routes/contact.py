from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.utils.auth_helpers import get_current_username, is_authenticated

# Create a Blueprint for contact routes
contact_bp = Blueprint("contact", __name__, url_prefix="/contact")


@contact_bp.route("/", methods=["GET", "POST"])
def contact():
    """Display and handle the contact form"""
    if request.method == "POST":
        # In a real application, you would process the form submission here
        # For example, sending an email or storing the message in a database
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # Basic validation
        if not name or not email or not subject or not message:
            flash("All fields are required")
            return render_template("contact.html")

        # Here you would add code to send the email or store the message
        # For now, we'll just show a success message
        flash("Your message has been sent! We'll get back to you soon.")
        return redirect(url_for("contact.contact"))

    return render_template("contact.html")
