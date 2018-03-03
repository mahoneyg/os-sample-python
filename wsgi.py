from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! - from Glenn Mahoney copy of wsgi.py"

if __name__ == "__main__":
    application.run()
