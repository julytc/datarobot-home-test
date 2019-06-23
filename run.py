from flask import Flask
from flask_github import GitHub
from repo.views import *
from repo.models import db
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('instance.default')
github = GitHub(app)
if __name__ == '__main__':
    app.register_blueprint(bp)
    db.init_app(app)
    app.run(host='0.0.0.0', port=3000)

