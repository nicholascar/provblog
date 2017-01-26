from flask import Blueprint, render_template, Markup
from routes.functions import _get_posts
import markdown
pages = Blueprint('pages', __name__)


@pages.route('/')
def home():
    posts = _get_posts()
    md = open('pages/home.md').read()
    content = Markup(markdown.markdown(md))
    return render_template('page.html', **locals())
