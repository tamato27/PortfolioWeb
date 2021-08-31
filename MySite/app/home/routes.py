from flask import Blueprint, render_template

from flask import current_app as app

home = Blueprint('home', __name__)


@home.route('/')
def index():  # put application's code here
    return render_template('index.html')


@home.route('/skills')
def skills():
    return render_template('skills.html')
