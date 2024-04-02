from flask import Blueprint, jsonify, request

bp = Blueprint('e-note-api', __name__)

@bp.route("/")
def hello_world():
    return "Hello, World!"
