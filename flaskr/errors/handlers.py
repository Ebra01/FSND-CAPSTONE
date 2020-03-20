from flask import Blueprint, jsonify, render_template, request
from werkzeug.exceptions import NotFound
from flaskr.auth.auth import AuthError, autherrorhandler

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':

        return jsonify({
            'error': 404,
            'message': 'Not Found',
            'success': False
        }), 404
    else:
        return render_template('errors/404.html')


@errors.app_errorhandler(400)
def error_400(error):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':

        return jsonify({
            'error': 400,
            'message': 'Bad Request',
            'success': False
        }), 400
    else:
        return render_template('errors/400.html')


@errors.app_errorhandler(405)
def error_405(error):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':

        return jsonify({
            'error': 405,
            'message': 'Method Not Allowed',
            'success': False
        }), 405
    else:
        return render_template('errors/405.html')


@errors.app_errorhandler(422)
def error_422(error):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':

        return jsonify({
            'error': 422,
            'message': 'Unprocessable',
            'success': False
        }), 422
    else:
        return render_template('errors/422.html')


@errors.app_errorhandler(AuthError)
def authentification_failed(autherror):
    error = autherrorhandler(autherror.error, 'authorization error')
    status_code = autherror.status_code

    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':

        return jsonify({
            'error': status_code,
            'message': error[0],
            'success': False
        }), status_code

    else:
        return render_template('errors/authError.html',
                               error=error, status_code=status_code)
