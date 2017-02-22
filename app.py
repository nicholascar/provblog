from flask import Flask
from routes import pages, posts, api
from flask_mobility import Mobility

app = Flask(__name__)
app.register_blueprint(pages.pages)
app.register_blueprint(posts.posts)
app.register_blueprint(api.api)
Mobility(app)

if __name__ == '__main__':
    app.run(port=5001)
