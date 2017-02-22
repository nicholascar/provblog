from flask import Blueprint, render_template, Markup
#from flask.ext.misaka import Misaka
import markdown
import markdown2
from routes.functions import _get_posts
posts = Blueprint('posts', __name__)


@posts.route('/post/<string:filename>')
def post(filename):
    posts = _get_posts()
    md = open('posts/{}.md'.format(filename)).read()
    content = Markup(markdown.markdown(md, extensions=['codehilite', 'fenced_code']))
    post_title = filename[10:].replace('-', ' ')
    return render_template('post.html', **locals())
