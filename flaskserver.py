from flask import Flask,jsonify,request,session, redirect
from werkzeug.utils import redirect
from backend.db_connect import Database

app = Flask(__name__)




'''
Login route
'''

@app.route("/login",methods=["POST"])
def login_user():

    password = request.args.get("password")
    email = request.args.get("email")
    db = Database()
    if db.user_login(email,password) == True:
        print("All the way")
    else:
        print("Failed as expected")
    return "Ok"

    



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


@app.route("/create_user",methods=["POST"])
def index():
    name = request.args.get("name")
    password = request.args.get("password")
    email = request.args.get("email")
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