
import os
DEBUG = True
SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']

