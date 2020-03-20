import os
from flask import (Blueprint, session, redirect,
                   url_for, render_template, flash)
from six.moves.urllib.parse import urlencode
from auth0.v3.authentication import GetToken
from auth0.v3.management.users import Users as UserManagement
from flaskr.users.forms import LoginForm, RegistrationForm
from flask_login import login_user, current_user, logout_user
from flaskr.models.models import JWT, Users
from flaskr import (oauth, bcrypt, login_manager, DOMAIN,
                    CLIENT_SECRET, CLIENT_ID, SCOPE, AUDIENCE)

users = Blueprint("users", __name__)

# This will help us to extracting the access token
get_token = GetToken(DOMAIN)

# registering auth0
auth0 = oauth.register(
    'auth0',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    api_base_url=f'https://{DOMAIN}',
    access_token_url=f'https://{DOMAIN}/oauth/token',
    authorize_url=f'https://{DOMAIN}/authorize',
    client_kwargs={
        'scope': SCOPE,
    },
)


@login_manager.user_loader
def load_user(user_id):
    """
    specify the current user, so we can use it in the frontend,
     and other endpoints.
    """
    return Users.query.get(int(user_id))


@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Here we are using a login endpoint that directly connect the user
    to his auth0 account, with no need to use the login interface,
    making it easier to gain the access token, and use it freely.
    """

    # Check if there is a user logged-in already
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Loading the login form
    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        try:
            # here we use a method from the auth0.v3.authentication.GetToken
            # to gain the user's access token
            token = get_token.login(client_id=CLIENT_ID,
                                    client_secret=CLIENT_SECRET,
                                    username=email,
                                    password=password, scope=SCOPE,
                                    audience=AUDIENCE,
                                    realm='Username-Password-Authentication')

            access_token = token['access_token']

            try:
                # Here we try to add the user to the DataBase
                add_user_to_db(email=email,
                               password=password)
            except Exception as e:
                print('User Insertion Error')
                print(e)

            try:
                # Here we add the user's access token to JWT Table
                # associating it with the user id
                user_ = Users.query.filter_by(email=email).first()
                jwt = JWT(
                    access_token=access_token,
                    user_id=user_.id
                )
                jwt.insert()
            except Exception as e:
                print('JWT Insertion Error')
                print(e)

            try:
                # Here we validate the Form's data
                # to log the user in as current user.
                validate_current_user(email=form.email.data,
                                      password=form.password.data,
                                      remember=form.remember.data)
            except Exception as e:
                print('User Validation Error')
                print(e)

            return redirect(url_for('main.home'))

        except Exception as e:
            print(e)
            flash('Wrong email or password! try again.', 'danger')
    return render_template('forms/login.html', form=form, title='Login')


@users.route('/register', methods=['GET', 'POST'])
def register():
    # Check if there is a user logged-in already
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Loading the Registration form
    form = RegistrationForm()
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        try:
            # Here we try to add the user to the DataBase
            add_user_to_db(email, password)

        except Exception as e:
            print('User Insertation Error')
            print(e)

        try:
            # Here we register the new user to auth0
            # using the 'Username-Password-Authentication' connection
            # from auth0
            body = {
                'email': email,
                'password': password,
                'connection': 'Username-Password-Authentication'
            }

            register_to_auth(body)

        except Exception as e:
            print('User Registeration To Auth0 Error')
            print(e)

        return redirect(url_for('users.login'))
    return render_template('forms/register.html', title='Register', form=form)


@users.route('/logout')
def logout():
    """
    Clearing the session, Deleting the user id,
    and access token frin JWT Table, and logging the user out from auth0
    """

    # Clear session stored data
    session.clear()

    try:
        jwts = JWT.query.all()
        for jwt in jwts:
            jwt.delete()
    except Exception as e:
        print(e)

    logout_user()

    # Redirect user to logout endpoint
    params = {'returnTo': url_for('main.home', _external=True),
              'client_id': CLIENT_ID}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))


def add_user_to_db(email, password):
    registered_users = Users.query.all()
    registered_users = [u.display() for u in registered_users]
    registered_emails = [u['email'] for u in registered_users]

    # Check to see if the email is not already in the DataBase, and
    # if not adding both email and hashed password to the DataBase
    if email not in registered_emails:
        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')
        new_user = Users(
            email=email,
            password=hashed_password
        )
        new_user.insert()


def validate_current_user(email, password, remember):
    try:
        user_ = Users.query.filter_by(email=email).first()

        # Check if entered password matches user's hashed password
        if user_ and bcrypt.check_password_hash(user_.password, password):
            # Logging the user as current user
            login_user(user_, remember=remember)
    except Exception as e:
        print('Validation Error')
        print(e)


def register_to_auth(body):
    # Generate Api Management TOKEN
    api_token = os.getenv('API_TOKEN')
    # Create User management from auth0.v3.management
    userManagement = UserManagement(DOMAIN, api_token)

    # Register User to auth0, using create method
    userManagement.create(body)
