import unittest
from app import create_app, db
from app.models import User, EmojiSequence, Team, Project
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI
