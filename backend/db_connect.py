import sqlite3
import datetime
import time
from werkzeug.security import safe_str_cmp
from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet


class Database():

    def __init__(self):
        self.con = sqlite3.connect("login-app.db")
        self.cur = self.con.cursor()

    # Login section

    def user_login_check(self,email,password):
        try:
            result = self.cur.execute('''SELECT * FROM clear_text_users WHERE email = "{}"'''.format(email))
            user_credentials = []
            for user in result:
                user_credentials.append(user)
            print(user_credentials)
            db_password = user_credentials[0][3]
            if password == db_password:
                print("Success")
                return True
        except:
            print("cant find user")

    
    def get_user(self,email):
        try:
            result = self.cur.execute('''SELECT * FROM clear_text_users WHERE email = "{}"'''.format(email))
            user_credentials = []
            for user in result:
                user_credentials.append(user)

            return user_credentials
        except:
            return False
            


    # User-section

    def get_all_users(self):
        ''' Only for testing purposes..'''
        try:
            user_list = []
            users = self.cur.execute('''SELECT * FROM users''')
            for user in users:
                user_list.append(user)
            return user_list
        except:
            return False


    def get_user_by_id(self,id):
        try:
           self.cur.execute('''SELECT * FROM users WHERE id = {}'''.format(int(id)))
           user = self.cur.fetchall()
           print(user[0])
           return user[0]
        except:
            print("Can't find user")
            return False
            

    def get_email(self,email):
        try:
        
            self.cur.execute('''SELECT * FROM users WHERE email = "{}"'''.format(email))
            self.cur.fetchall()
            print("Found email")
            return True
        except:
            print("Get email is down")
            return False 
    
    def new_account(self,email,password, name):

        now = datetime.datetime.now()
        last_logged_in = now
        times_logged_in = 1
        try:
            self.cur.execute('''INSERT INTO clear_text_users (email,name,password,user_created,last_login,login_amt) \
                VALUES("{}","{}","{}","{}","{}",{})'''.format(name,email,password,now,last_logged_in,int(times_logged_in)))
            self.con.commit()
            print("yes")
            return True
            
        except:
            print("no")
            return False

    
    def update_user_info(self,id,name,email):
        
        self.cur.execute('''UPDATE users SET name="{}",email="{}" WHERE id = {}'''.format(name,email,id))
        self.con.commit()
        print("Changed some stuff")
        return True



    def update_password(self,id,changed_password):
        self.cur.execute('''UPDATE users SET password="{}" WHERE id = {}'''.format(password,id))
        self.con.commit()
        return True


    def delete_user_by_id(self,id):
            if self.get_user_by_id(id):
                self.cur.execute('''DELETE FROM users WHERE id = {}'''.format(id))
                self.con.commit()


    def update_login_info(self,id):
        self.id = id
        # print(self.id)
        login_amount = self.cur.execute('''SELECT login_amt FROM users WHERE id = {}'''.format(self.id))
        self.con.commit()
        for amount in login_amount:
            new_login_amount = amount[0]+1
            now = datetime.datetime.now()
            self.cur.execute('''UPDATE users SET last_login = "{}",login_amt = {} WHERE id = {}'''.format(now,new_login_amount, self.id))
            self.con.commit()
            break

    def db_close(self):
        self.cur.close()
        self.con.close()


Database().user_login_check("hejsan","test")