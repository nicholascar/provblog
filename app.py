from flask import Flask
from routes import pages, posts, api
app = Flask(__name__)
app.register_blueprint(pages.pages)
app.register_blueprint(posts.posts)
app.register_blueprint(api.api)


if __name__ == '__main__':
    app.run()
