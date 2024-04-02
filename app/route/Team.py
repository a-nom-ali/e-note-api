from flask import jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.model import User, Team
from app import db
from app.route import bp


@bp.route("/")
def hello_world():
    return "Hello, World!"


@bp.route('/add_user', methods=['POST'])
def add_user():
    # Get data from request
    user_data = request.get_json()

    new_user = User(
        username=user_data['username'],
        email=user_data['email'],
        # Here you should add password hashing
        password_hash=user_data['password']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


@bp.route('/register', methods=['POST'])
def register():
    # Get data from the request
    data = request.get_json()

    # Check if the user already exists
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'message': 'Email already exists.'}), 409

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=hashed_password
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201


@bp.route('/login', methods=['POST'])
def login():
    # Get data from the request
    auth_data = request.get_json()

    # Validate credentials
    user = User.query.filter_by(email=auth_data['email']).first()
    if user and check_password_hash(user.password_hash, auth_data['password']):
        # Generate the JWT token
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    return jsonify({'message': f'Welcome {user.username}!'}), 200


@bp.route('/teams', methods=['POST'])
@jwt_required()
def create_team():
    data = request.get_json()
    new_team = Team(name=data['name'], description=data['description'])
    db.session.add(new_team)
    db.session.commit()
    return jsonify(
        {'message': 'New team created', 'team': {'name': new_team.name, 'description': new_team.description}}), 201


@bp.route('/teams/<int:team_id>', methods=['GET'])
@jwt_required()
def get_team(team_id):
    team = Team.query.get_or_404(team_id)
    return jsonify({'name': team.name, 'description': team.description}), 200


@bp.route('/teams/<int:team_id>', methods=['PUT'])
@jwt_required()
def update_team(team_id):
    team = Team.query.get_or_404(team_id)
    data = request.get_json()
    team.name = data['name']
    team.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Team updated', 'team': {'name': team.name, 'description': team.description}}), 200


@bp.route('/teams/<int:team_id>', methods=['DELETE'])
@jwt_required()
def delete_team(team_id):
    team = Team.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team deleted'}), 200


