from flask_marshmallow import Marshmallow
from marshmallow import fields
from app.model import User, EmojiSequence, Team, Project

ma = Marshmallow()


# Schema for User model
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # Optional: deserialize to model instances
        include_fk = True  # Optional: include foreign keys

    # Custom fields can be added here if needed


# Schema for EmojiSequence model
class EmojiSequenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmojiSequence
        load_instance = True


# Schema for Team model
class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        load_instance = True

    # If you want to show users in the team
    users = fields.Nested(UserSchema, many=True, exclude=('teams',))


# Schema for Project model
class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        load_instance = True

    # If you want to show teams in the project
    teams = fields.Nested(TeamSchema, many=True, exclude=('projects',))


# Initialize the Marshmallow object
def init_app(app):
    ma.init_app(app)
