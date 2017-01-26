from flask import Blueprint, render_template, Markup
#from flask.ext.misaka import Misaka
import markdown
posts = Blueprint('posts', __name__)


@posts.route('/post/<string:filename>')
def post(filename):
    md = open('posts/{}.md'.format(filename)).read()
    content = Markup(markdown.markdown(md))
    return render_template('post.html', **locals())
