import sqlite3
import datetime
import time


class Database():

    db_path = "nordaxon_db.db"

    def __init__(self):
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()


    def get_allusers(self):
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
            return True
        except:
            return False

    
    def new_account(self,email,password, name):

        now = datetime.datetime.now()
        last_logged_in = now
        times_logged_in = 1
        try:
            self.cur.execute('''INSERT INTO users (name,email,password,user_created,last_login,login_amt) \
                VALUES("{}","{}","{}","{}","{}",{})'''.format(name,email,password,now,last_logged_in,int(times_logged_in)))
            self.con.commit()
            print("yes")
            return True
            
        except:
            print("no")
            return False

    
    def update_user_info(self,id,name,email):
        pass

    def update_password(self,id,new_password):
        pass


    def delete_user_by_id(self,id):
        try:
            if self.get_user_by_id(id):
                self.cur.execute('''DELETE FROM users WHERE id = {}'''.format(id))
                self.con.commit()
        except:
            return False



    def db_close(self):
        self.cur.close()
        self.con.close()