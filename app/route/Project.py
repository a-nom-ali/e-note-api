from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.model import Team, Project
from app import db
from app.route import bp


@bp.route('/teams/<int:team_id>/projects', methods=['POST'])
@jwt_required()
def create_project(team_id):
    team = Team.query.get_or_404(team_id)
    data = request.get_json()
    new_project = Project(name=data['name'], description=data['description'], team=team)
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'New project created',
                    'project': {'name': new_project.name, 'description': new_project.description}}), 201


@bp.route('/projects/<int:project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({'name': project.name, 'description': project.description, 'team_id': project.team_id}), 200


@bp.route('/projects/<int:project_id>', methods=['PUT'])
@jwt_required()
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    project.name = data['name']
    project.description = data['description']
    db.session.commit()
    return jsonify(
        {'message': 'Project updated', 'project': {'name': project.name, 'description': project.description}}), 200


@bp.route('/projects/<int:project_id>', methods=['DELETE'])
@jwt_required()
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted'}), 200


