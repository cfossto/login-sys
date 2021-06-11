from flask import Flask, jsonify, request, redirect, Response,url_for
from flask_jwt import JWT, jwt_required
from flask_cors import CORS
from werkzeug.utils import redirect
from werkzeug import security
from backend.db_connect import Database



app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "veryverySecret1"


'''
Login route
'''

@app.route("/login",methods=["POST"])
def login_user():
    password = request.args.get("password")
    email = request.args.get("email")
    db = Database()
    user = db.get_user(email)
    id = user[0][0]
    name = user[0][1]
    username = user[0][2]

    user_creds = []
    user_creds.append(id)
    user_creds.append(name)
    user_creds.append(username) 

    if db.user_login_check(email,password):
        return jsonify(user_creds), 200
    else:
        return "Not logged in",404



    



'''
USER ROUTES

URL-format: /user followed by method
Specific use case: /user/<int:id> followed by method (affects that specific user)

'''


# Get specific user
@app.route("/user/<int:id>",methods=["GET"])
def get_user(id):
    db = Database()
    user = db.get_user_by_id(id)
    db.db_close()
    return jsonify(user)


# Create new user
@app.route("/create_user",methods=["POST"])
def create_user():
    name = request.args.get("name")
    password = request.args.get("password")
    email = request.args.get("email")
    db = Database()
    try:
        db.new_account(name,password,email)
        db.db_close()
        return "Created"
    except:
        return "No"


# Update user info
@app.route("/user",methods=["PUT"])
def update_user_info():
    
    id = request.args.get("id")
    name = request.args.get("name")
    email = request.args.get("email")

    db = Database()
    db.update_user_info(id,name,email)
    db.db_close()
    return "Ok"

# Update password
@app.route("/password/change",methods=["POST"])
def change_password():

    db = Database()

    id = request.args.get("id")
    old_password = request.args.get("old-password")
    new_password = request.args.get("password")
    db.update_password(id,new_password)
    db.db_close()
    return "Password changed"


# Delete user by id
@app.route("/user/<int:id>",methods=["DELETE"])
def delete_user(id):
    db = Database()
    db.delete_user_by_id(id)
    return "Deleted user"
    


# Log routes



app.run(port=3000, debug=True)