import json

from json2html import *
from flask import Blueprint, jsonify, request

from app.openai_integration import suggest_emoji_sequence

bp = Blueprint('e-note-api', __name__)

@bp.route("/", methods=['GET'])
def hello():
    q = request.args.get('q', "Spider-saurus")
    # data = request.get_json()
    return json2html.convert(json = json.loads(suggest_emoji_sequence(q)))


@bp.route("/suggest", methods=['GET'])
def suggest():
    q = request.args.get('q', "Spider-saurus")
    # data = request.get_json()
    return suggest_emoji_sequence(q)
