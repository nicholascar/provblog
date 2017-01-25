from flask import Blueprint, render_template
pages = Blueprint('pages', __name__)


@pages.route('/')
def hello_world():
    return render_template('home.html')
