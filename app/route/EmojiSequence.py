from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.model import EmojiSequence
from app import db
from app.route import bp


@bp.route('/emoji-sequences', methods=['POST'])
@jwt_required()
def create_emoji_sequence():
    data = request.get_json()
    new_sequence = EmojiSequence(keyword=data['keyword'], sequence=data['sequence'])
    db.session.add(new_sequence)
    db.session.commit()
    return jsonify({'message': 'Emoji sequence created',
                    'emoji_sequence': {'keyword': new_sequence.keyword, 'sequence': new_sequence.sequence}}), 201


@bp.route('/emoji-sequences/<int:sequence_id>', methods=['GET'])
@jwt_required()
def get_emoji_sequence(sequence_id):
    sequence = EmojiSequence.query.get_or_404(sequence_id)
    return jsonify({'keyword': sequence.keyword, 'sequence': sequence.sequence}), 200


@bp.route('/emoji-sequences/<int:sequence_id>', methods=['PUT'])
@jwt_required()
def update_emoji_sequence(sequence_id):
    sequence = EmojiSequence.query.get_or_404(sequence_id)
    data = request.get_json()
    sequence.keyword = data['keyword']
    sequence.sequence = data['sequence']
    db.session.commit()
    return jsonify({'message': 'Emoji sequence updated',
                    'emoji_sequence': {'keyword': sequence.keyword, 'sequence': sequence.sequence}}), 200


@bp.route('/emoji-sequences/<int:sequence_id>', methods=['DELETE'])
@jwt_required()
def delete_emoji_sequence(sequence_id):
    sequence = EmojiSequence.query.get_or_404(sequence_id)
    db.session.delete(sequence)
    db.session.commit()
    return jsonify({'message': 'Emoji sequence deleted'}), 200


@bp.route('/emoji-sequences/search', methods=['GET'])
@jwt_required()
def search_emoji_sequences():
    query = request.args.get('q')
    if not query:
        return jsonify({'message': 'No search query provided'}), 400

    # This is a simple search that looks for sequences containing the query.
    # It might need to be optimized for performance depending on the dataset size
    sequences = EmojiSequence.query.filter(EmojiSequence.keyword.like(f'%{query}%')).all()
    serialized_sequences = [{'keyword': s.keyword, 'sequence': s.sequence} for s in sequences]
    return jsonify(serialized_sequences), 200
