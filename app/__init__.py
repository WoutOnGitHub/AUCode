from flask import Flask


# To avoid circular imports, make sure only run.py imports this
def create_app():
    """Application factory function"""
    app = Flask(__name__)

    # Import configuration
    from config.settings import SECRET_KEY, STATIC_DIR

    # Configure app
    app.static_folder = STATIC_DIR
    app.secret_key = SECRET_KEY

    # Register routes and initialize app components
    from app.main import init_app

    init_app(app)

    return app
