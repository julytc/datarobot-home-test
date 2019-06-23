from flask import Flask, Blueprint, request, url_for, flash, g, redirect, session, render_template
from github import Github, GithubException, UnknownObjectException
import git
from run import app, github
from repo.models import users, db
import os
bp=Blueprint('/', __name__, template_folder='templates')
@bp.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = users.query.get(session['user_id'])
@bp.after_request
def after_request(response):
    db.session.remove()
    return response
@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')
@bp.route('/login', methods=['GET', 'POST'])
def login():
    return github.authorize(scope="public_repo,read:user")
@bp.route('/logout')
def logout():
    session.pop('user_id', None)
@bp.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        flash("Authorization failed.")
        return redirect('/')
    user = users.query.filter_by(github_access_token=oauth_token).first()
    if user is None:
        user = users(oauth_token)
        db.session.add(user)
    user.github_access_token = oauth_token
    g.user = user
    github_user = github.get('/user')
    user.github_id = github_user['id']
    user.github_login = github_user['login']
    db.session.commit()
    session['user_id'] = user.id
    return redirect('/repo')
@github.access_token_getter
def token_getter(token=None):
    user = g.user
    if user is not None:
        return user.github_access_token

@bp.route('/repo')
def repo():
    user_repo_name = 'jt-datarobot-assesment'
    initial_repo_name = 'datarobot-home-test'
    token = token_getter()
    g = Github(token)
    user = g.get_user()
    try:
        user.get_repo(user_repo_name)
    except UnknownObjectException:
        user.create_repo(user_repo_name)
        os.system("rm -rf %s.git" % initial_repo_name)
        git_client = git.Git()
        git_client.clone("https://%s@github.com/julytc/%s" % (token, initial_repo_name), "--bare")
        git_repo = git.Repo('%s.git' % initial_repo_name)
        git_repo.git.push('--mirror', "https://%s@github.com/%s" % ( token , user.get_repo(user_repo_name).full_name))
        return redirect('/')
    else:
        return redirect('/')






