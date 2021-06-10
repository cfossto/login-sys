from flask import Flask

app = Flask(__name__)


@app.route("/",methods=["GET"])
def index():
    return "Hello"


@app.route("/auth",methods=["POST"])
def user_auth():
    pass

app.run(port=3000, debug=True)