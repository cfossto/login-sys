import sqlite3
import datetime
import time


class Database():

    def __init__(self):
        self.con = sqlite3.connect("nordaxon_db.db")
        self.cur = self.con.cursor()

    # Login section

    def user_login(self,email,password):
        if self.get_email(email):
            id = 0
            user_credentials = self.cur.execute('''SELECT id, password FROM users WHERE email = "{}"'''.format(email))
            for user in user_credentials:
                id = user[0]
                exchange_password = user[1]
                if exchange_password == password:
                    print("password checked")
                    self.update_login_info(id)
                    return True

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
            print("Didn't find email")
            return False

    
    def new_account(self,email,password, name):

        now = datetime.datetime.now()
        last_logged_in = now
        times_logged_in = 1
        try:
            self.cur.execute('''INSERT INTO users (email,name,password,user_created,last_login,login_amt) \
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


    def check_password(self,id,old_password):
        existing_password = self.cur.execute('''SELECT password FROM users WHERE id = {}'''.format(id))
        self.con.commit()
        password_from_db = ""
        for password in existing_password:
            password_from_db = password[0]
        if old_password == password_from_db:
            return True
        else:
            return False

    def update_password(self,id,new_password):
        self.cur.execute('''UPDATE users SET password="{}" WHERE id = {}'''.format(id,new_password))
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


# print(Database().check_password(5,"hello"))