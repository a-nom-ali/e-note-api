from app import create_app, db
from app.model import User, EmojiSequence  # Import additional models as needed
from flask_migrate import Migrate

app = create_app()

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'EmojiSequence': EmojiSequence
        # Add other models here if needed
    }


if __name__ == '__main__':
    app.run(debug=True, port=8000)
