from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


# Function to hash a password
def hash_password(password):
    return generate_password_hash(password)


# Function to check a hashed password
def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)


# Function to generate JWT tokens
def create_tokens(identity):
    access_token = create_access_token(identity=identity, fresh=True, expires_delta=timedelta(minutes=15))
    refresh_token = create_refresh_token(identity=identity, expires_delta=timedelta(days=30))
    return access_token, refresh_token


# Function to validate an input for certain criteria
def is_valid_input(input_data):
    # Implementation depends on what you're validating
    pass


# You can also include decorators for routes that need specific types of validation or authentication
def admin_required(fn):
    # Custom decorator to ensure user is an admin
    pass

# Any other general utility functions that don't fit into other modules can go here
