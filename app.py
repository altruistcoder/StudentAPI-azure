from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to student records API!" + "created by Rishabh Aggarwal"


if __name__ == "__main__":
    app.run(port=8000, use_reloader=True, debug=True)
