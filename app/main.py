from datetime import datetime

import markdown
from flask import render_template
from markupsafe import Markup

from config.database import create_tables


def init_app(app):
    # Ensure database tables exist
    create_tables()

    # Custom implementation of markdown filter
    @app.template_filter("markdown")
    def render_markdown(text):
        return Markup(markdown.markdown(text, extensions=["fenced_code"]))

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.problems import problems_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(problems_bp)

    # Add context processor for templates
    @app.context_processor
    def inject_now():
        return {"now": datetime.utcnow()}

    # Define root route
    @app.route("/")
    def index():
        return render_template("base.html")
