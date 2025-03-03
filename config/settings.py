"""
Application settings for AUCode.
"""

import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
DEBUG = True

# Application settings
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Static and media settings
STATIC_URL = "static/"
STATIC_DIR = os.path.join(BASE_DIR, "app/static")

# Challenge files location
CHALLENGES_DIR = os.path.join(BASE_DIR, "challenges")

# Time zone
TIME_ZONE = "UTC"
