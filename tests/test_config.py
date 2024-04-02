# test_config.py

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory SQLite database for tests.
    SECRET_KEY = 'test_secret_key'
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in the forms for tests.
    JWT_SECRET_KEY = 'test_jwt_secret_key'  # JWT secret key for testing.

    # Any other configuration variables that need to be overridden for testing purposes.
