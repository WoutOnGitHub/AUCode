"""
Application settings for AUCode.
"""

import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    try:
        with open(os.path.join(BASE_DIR, "secret_key.txt")) as f:
            SECRET_KEY = f.read().strip()
    except FileNotFoundError:
        # For first-time setup only, create and save a key
        if DEBUG:
            import secrets

            SECRET_KEY = secrets.token_urlsafe(32)
            with open(os.path.join(BASE_DIR, "secret_key.txt"), "w") as f:
                f.write(SECRET_KEY)
        else:
            raise Exception("SECRET_KEY not found. Set it as an environment variable.")


# Application settings
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Static and media settings
STATIC_URL = "static/"
STATIC_DIR = os.path.join(BASE_DIR, "app/static")

# Problem files location
PROBLEMS_DIR = os.path.join(BASE_DIR, "problems")

# Time zone
TIME_ZONE = "UTC"
