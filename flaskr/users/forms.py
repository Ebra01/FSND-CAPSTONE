from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (DataRequired, Length, Email,
                                EqualTo, ValidationError)
from flaskr.models.models import Users


class LoginForm(FlaskForm):
    """
    LoginForm designed to log-in a user directly to auth0
    with no need for auth0 login interface
    """
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LoginForm, self).__init__(*args, **kwargs)

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    """
    RegistrationForm designed to register a user directly to auth0
    with no need for auth0 register interface
    """
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(RegistrationForm, self).__init__(*args, **kwargs)

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 Length(min=8),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_password(self, password):
        """
        Validate if password contains at least one uppercase,
        one lowercase, and one digit.
        """
        passw = password.data

        if not any(p.isupper() for p in passw):
            raise ValidationError(
                'Password must have at least one uppercase.')
        if not any(p.islower() for p in passw):
            raise ValidationError(
                'Password must have at least one lowercase.')
        if not any(p.isdigit() for p in passw):
            raise ValidationError(
                'Password must have at least one digit.')

    def validate_email(self, email):
        """
        Check if the email is already registered in the DB.
        """
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError(
                'Email already registered, Pleace choose another one')
