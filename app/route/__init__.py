import json
from json import JSONDecodeError

from json2html import *
from flask import Blueprint, jsonify, request

from app.openai_integration import suggest_emoji_sequence, fix_json

bp = Blueprint('e-note-api', __name__)

@bp.route("/", methods=['GET'])
def hello():
    print("hello")
    q = request.args.get('q', "Spider-saurus")
    # data = request.get_json()
    try:
        result = json.loads(suggest_emoji_sequence(q))
        print("html")
        return json2html.convert(
            json = result,
            table_attributes='border="1" width="100%"'
        )
    except JSONDecodeError as e:
        print("attempt to fix json")
        result = fix_json(result)
        return json2html.convert(
            json = result,
            table_attributes='border="1" width="100%"'
        )



@bp.route("/suggest", methods=['GET'])
def suggest():
    q = request.args.get('q', "Spider-saurus")
    # data = request.get_json()
    return suggest_emoji_sequence(q)
