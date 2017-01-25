from flask import Flask
from routes import pages
app = Flask(__name__)
app.register_blueprint(pages.pages)


if __name__ == '__main__':
    app.run()
