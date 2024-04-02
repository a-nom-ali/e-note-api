import json
import unittest
from app import create_app, db
from app.models import User, EmojiSequence, Team, Project
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_emoji_sequence_suggestion(self):
        # Example test for emoji sequence suggestion endpoint
        response = self.client.post('/suggest-emoji-sequence', data=json.dumps({'text': 'happy'}),
                                    content_type='application/json')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('emoji_sequence', data)

    # Add more tests for other endpoints


if __name__ == '__main__':
    unittest.main()
