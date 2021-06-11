import sqlite3
import datetime
import time
from werkzeug.security import safe_str_cmp
from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet
from security import encrypt_mail, decrypt_mail


class Database():

    def __init__(self):
        self.con = sqlite3.connect("nordaxon_db.db")
        self.cur = self.con.cursor()

    # Login section

    def user_login_check(self,email,password):
        try:
            e_email = encrypt_mail(email)
            result = self.cur.execute('''SELECT * FROM users''')
            user = []
            for users in result:
                user.append(users)
            id = user[0][0]
            db_password = user[0][3]
            print(db_password)
            print(password)
            if not pbkdf2_sha256.verify(password,):
                print("yep")
        except:
            print("cannot find user")



    # User-section

    def get_all_users(self):
        ''' Only for testing purposes..'''
        try:
            user_list = []
            users = self.cur.execute('''SELECT * FROM users''')
            for user in users:
                user_name = decrypt_user_details(encrypted_username=user)
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
            encrypted_email = encrypt_mail(email)
            print(encrypted_email)
            self.cur.execute('''SELECT * FROM users WHERE email = "{}"'''.format(encrypted_email))
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
        hashed_password = pbkdf2_sha256.hash(password)
        encrypted_username, encrypted_name = encrypt_user_details(email,name)
        try:
            self.cur.execute('''INSERT INTO users (email,name,password,user_created,last_login,login_amt) \
                VALUES("{}","{}","{}","{}","{}",{})'''.format(encrypted_name,encrypted_username,hashed_password,now,last_logged_in,int(times_logged_in)))
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
        new_password = pbkdf2_sha256.hash(changed_password)
        print(new_password)
        self.cur.execute('''UPDATE users SET password="{}" WHERE id = {}'''.format(new_password,id))
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


Database().user_login_check("test","test")