# app/main.py
from flask import redirect

from config.database import create_tables


def init_app(app):
    # Ensure database tables exist
    create_tables()

    # Define root route
    @app.route("/")
    def index():
        return "Hello world!"
