from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.utils.auth_helpers import get_current_user_id, login_required

# Create a Blueprint for profile routes
profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


@profile_bp.route("/")
def profile():
    user_id = get_current_user_id()
    if user_id:
        return render_template("profile.html")
    else:
        return redirect(url_for("index"))
