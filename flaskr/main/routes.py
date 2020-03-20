from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():

    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':

        return jsonify({
            'title': 'Home Page',
            'body': 'Home Page ;)',
            'success': True
        })
    else:

        return render_template('pages/home.html')
