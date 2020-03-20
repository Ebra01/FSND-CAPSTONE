from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskr.models.models import Users


class LoginForm(FlaskForm):
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
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(RegistrationForm, self).__init__(*args, **kwargs)

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 Length(min=8), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_password(self, password):

        passw = password.data

        if not any(p.isupper() for p in passw):
            raise ValidationError('Password must have at least one uppercase.')
        if not any(p.islower() for p in passw):
            raise ValidationError('Password must have at least one lowercase.')
        if not any(p.isdigit() for p in passw):
            raise ValidationError('Password must have at least one digit.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already registered, Pleace choose another one')
