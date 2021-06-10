from flask import Flask,jsonify
from backend.db_connect import Database

app = Flask(__name__)


@app.route("/create_user",methods=["POST"])
def index():
    db = Database()
    db.new_account("chris@fossto.com","1234","Isak")
    db.db_close()
    return "Created"


@app.route("/update_user",methods=["POST"])
def update_user():
    db = Database()
    
    

@app.route("/user/<int:id>",methods=["GET"])
def get_user(id):
    db = Database()
    user = db.get_user_by_id(id)
    db.db_close()
    return jsonify(user)
    

app.run(port=3000, debug=True)