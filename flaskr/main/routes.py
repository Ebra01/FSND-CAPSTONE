from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    This is a Friendly endpoint, any user can access this endpoint
    to make it easier for users to login or register
    using the menu tab in this page.

    Check if the request header
    (Content-Type) is {application/json}.

    If Content-Type = application/json,
    we request and return data as JSON objects.

    If Content-Type != application/json,
    we use templates (HTML) to request and return data

    """

    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':

        return jsonify({
            'title': 'Home Page',
            'body': 'Home Page ;)',
            'success': True
        })
    else:

        return render_template('pages/home.html')
