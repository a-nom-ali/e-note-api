from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    return error_response(400, message)


# Example of a custom error handler for 404 not found
def not_found_error(error):
    return error_response(404, 'The requested resource was not found.')


# Example of a custom error handler for 500 internal server error
def internal_error(error):
    return error_response(500, 'An internal error occurred.')
