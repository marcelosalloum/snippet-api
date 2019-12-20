from app import db
from app.api import bp
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
        payload['status_code'] = status_code
    response = jsonify(payload)
    response.status_code = status_code
    return response


@bp.app_errorhandler(400)
def bad_request(message):
    return error_response(400, message)


@bp.app_errorhandler(403)
def forbidden_error(error):
    return error_response(403, message='This resource can\'t be accessed by your user')


@bp.app_errorhandler(404)
def not_found_error(error):
    return error_response(404, message='This resource couldn\'t be found')


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return error_response(500, message='There was an internal error. Please contact the administrator')
