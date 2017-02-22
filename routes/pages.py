from flask import Blueprint, render_template, Markup
from flask_mobility.decorators import mobile_template
from routes.functions import _get_posts
import markdown
pages = Blueprint('pages', __name__)


@pages.route('/')
@mobile_template('{mobile/}page.html')
def home(template):
    posts = _get_posts()
    md = open('pages/home.md').read()
    content = Markup(markdown.markdown(md))
    return render_template(template, **locals())

