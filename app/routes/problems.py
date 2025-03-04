import os

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)

from app.models.problem import get_all_problems, get_problem_by_id
from app.models.submission import create_submission, get_user_problem_submission
from app.utils.auth_helpers import get_current_user_id, login_required
from app.utils.problem_helpers import (
    get_problem_absolute_file_path,
    get_problem_description,
)

# Create a Blueprint for problem routes
problems_bp = Blueprint("problems", __name__, url_prefix="/problems")


@problems_bp.route("/")
def list_problems():
    """Display list of all problems"""
    problems = get_all_problems()

    # For each problem, check if the current user has solved it
    user_id = get_current_user_id()
    for problem in problems:
        description = get_problem_description(problem["problem_folder"])
        problem["description"] = description
        if user_id:
            submission = get_user_problem_submission(user_id, problem["id"])
            problem["solved"] = submission and submission["is_correct"]
        else:
            problem["solved"] = False
        pass

    return render_template("problems/list.html", problems=problems)


@problems_bp.route("/<int:problem_id>")
def view_problem(problem_id):
    """Display a specific problem"""
    problem = get_problem_by_id(problem_id)
    if not problem:
        flash("Problem not found")
        return redirect(url_for("problems.list_problems"))

    # Fetch the description
    description = get_problem_description(problem["problem_folder"])
    problem["description"] = description

    # Check if the current user has solved this problem
    user_id = get_current_user_id()
    submission = None
    if user_id:
        submission = get_user_problem_submission(user_id, problem_id)

    return render_template(
        "problems/detail.html", problem=problem, submission=submission
    )


@problems_bp.route("/<int:problem_id>/download")
def download_problem(problem_id):
    """Download the problem file"""
    problem = get_problem_by_id(problem_id)
    if not problem:
        flash("Problem not found")
        return redirect(url_for("problems.list_problems"))

    full_path = get_problem_absolute_file_path(problem["problem_folder"])

    if not os.path.exists(full_path):
        flash("Problem file not found")
        return redirect(url_for("problems.view_problem", problem_id=problem_id))

    return send_file(full_path, as_attachment=True)


@problems_bp.route("/<int:problem_id>/submit", methods=["POST"])
@login_required
def submit_solution(problem_id):
    """Submit a solution for a problem"""
    problem = get_problem_by_id(problem_id)
    if not problem:
        flash("Problem not found")
        return redirect(url_for("problems.list_problems"))

    solution_hash = request.form.get("solution").strip()
    if not solution_hash:
        flash("Solution is required")
        return redirect(url_for("problems.view_problem", problem_id=problem_id))

    # Check if the solution is correct
    is_correct = solution_hash == problem["correct_hash"]

    # Create a submission record
    user_id = get_current_user_id()
    create_submission(user_id, problem_id, solution_hash, is_correct)

    if is_correct:
        flash("Congratulations! Your solution is correct.")
    else:
        flash("Your solution is incorrect. Please try again.")

    return redirect(url_for("problems.view_problem", problem_id=problem_id))
