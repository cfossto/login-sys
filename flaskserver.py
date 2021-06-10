from flask import Flask,jsonify,request
from backend.db_connect import Database

app = Flask(__name__)




'''
USER ROUTES

URL-format: /user followed by method
Specific use case: /user/<int:id> followed by method (affects that specific user)

'''



@app.route("/user/<int:id>",methods=["GET"])
def get_user(id):
    db = Database()
    user = db.get_user_by_id(id)
    db.db_close()
    return jsonify(user)


@app.route("/create_user/<string:name>+<string:password>+<string:email>",methods=["POST"])
def index(name,password,email):
    db = Database()
    db.new_account(name,password,email)
    db.db_close()
    return "Created"


@app.route("/user",methods=["PUT"])
def update_user():
    return "Hello"

    

@app.route("/user/<int:id>",methods=["DELETE"])
def delete_user(id):
    db = Database()
    db.delete_user_by_id(id)
    db.db_close()
    return "Deleted user"
    



app.run(port=3000, debug=True)