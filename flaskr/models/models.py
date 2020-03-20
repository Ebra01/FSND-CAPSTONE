import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

database_path = os.environ.get('DATABASE_URL')


def setup_db(app, db_path=database_path):
    """
    Setting up Database
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('CAPSTONE_SECRET')
    db.app = app
    db.init_app(app)
    db.create_all()


class Actors(db.Model):
    """
    Actors Table, including insert, update,
     and delete functions to make CRUD process easier
    """
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def display(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Movies(db.Model):
    """
    Movies Table, including insert, update,
    and delete functions to make CRUD process easier
    """
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    availability = db.Column(db.DateTime)

    def __init__(self, title, release_data, availability):
        self.title = title
        self.release_date = release_data
        self.availability = availability

    def __repr__(self):
        return f"Title: {self.title}, Release Date: {self.release_date}," \
               f" Availability: {self.availability}"

    def display(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'availability': self.availability
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class JWT(db.Model):
    """
    JWT Table, including insert,and delete
    functions to make CRUD process easier.

    This Table stores user's access token and id
    to make it easier to access endpoints in the frontend,
     both access token and id get deleted after logging out
    """
    __tablename__ = 'jwt'
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id

    def display(self):
        return {
            'access_token': self.access_token,
            'user_id': self.user_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Users(db.Model, UserMixin):
    """
    Actors Table, including insert, update,
    and delete functions to make CRUD process easier.

    This Table stores both the email and the hashed password of a user
    once they register, or log in with their auth0 account
    for the first time, this table make it easier to identify
    which access token belongs to whom
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def display(self):
        return {
            'id': self.id,
            'email': self.email
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
