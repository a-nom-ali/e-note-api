from flask import Blueprint, jsonify, request

from app.openai_integration import suggest_emoji_sequence

bp = Blueprint('e-note-api', __name__)

@bp.route("/suggest", methods=['GET'])
def suggest():
    q = request.args.get('q', "Spider-saurus")
    # data = request.get_json()
    return suggest_emoji_sequence(open("assets/suggestion_system_prompt.txt").read(), q)
