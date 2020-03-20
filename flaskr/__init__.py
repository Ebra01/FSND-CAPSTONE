import os
from pathlib import Path
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flaskr.models.models import setup_db, db
from flaskr.users.forms import LoginForm
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth
from flask_bcrypt import Bcrypt

# Here we specify the environment folder for important values
parent_folder = Path(Path(__file__).parent).parent
env_file = os.path.join(parent_folder, '.env')

load_dotenv(dotenv_path=env_file)

# Calling important modules
oauth = OAuth()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt()

# Here we use values from .env file
JWT_ALGORITHM = ['RS256']
DOMAIN = os.getenv('DOMAIN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
AUDIENCE = os.getenv('AUDIENCE')
SCOPE = os.getenv('SCOPE')


def create_app():
    # Create the app
    app = Flask(__name__, template_folder='templates')

    # Setting up DB, and initialize app in oauth, login_manager, and bcrypt
    setup_db(app)
    oauth.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Setting up CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS,PATCH')

        return response

    # Calling blueprints
    from flaskr.actors.routes import actor
    from flaskr.movies.routes import movie
    from flaskr.main.routes import main
    from flaskr.errors.handlers import errors
    from flaskr.users.routes import users

    # Register blueprints in the application
    app.register_blueprint(actor)
    app.register_blueprint(movie)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(users)

    return app
