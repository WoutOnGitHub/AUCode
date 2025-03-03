# run.py (at project root)
from app import create_app
from config.settings import DEBUG

app = create_app()

if __name__ == "__main__":
    app.run(debug=DEBUG)
