from datetime import datetime

from flask import render_template

from config.database import create_tables


def init_app(app):
    # Ensure database tables exist
    create_tables()

    # Register blueprints
    from app.routes.auth import auth_bp

    app.register_blueprint(auth_bp)

    # Add context processor for templates
    @app.context_processor
    def inject_now():
        return {"now": datetime.utcnow()}

    # Define root route
    @app.route("/")
    def index():
        return render_template("base.html")
