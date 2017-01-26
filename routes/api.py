from flask import Blueprint, request, Response, render_template
from routes.functions import _get_posts
api = Blueprint('api', __name__)


@api.route('/api')
def api_home():
    posts = _get_posts()
    return render_template('api.html', **locals())


@api.route('/api/lodge-pingback')
def lodge_pingback():
    uri = request.args.get('uri')
    if uri is not None and uri != '':
        uri_txt = 'for the resource {}.'.format(uri)
    else:
        uri_txt = 'but you forgot to specify the URI you\'re pinging back for!'

    txt = '''Thanks for pinging back {} Unfortunately this site can't yet handle pingbacks. ''' \
          '''Please send Nick and email to let him know what you're doing though as he's be most interested in ''' \
          '''work derived from this site.'''.format(uri_txt)
    return Response(
        txt,
        mimetype='text/plain'
    )
