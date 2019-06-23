from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    github_access_token = db.Column(String(255))
    github_id = db.Column(Integer)
    github_login = db.Column(String(255))

    def __init__(self, github_access_token):
        self.github_access_token = github_access_token

