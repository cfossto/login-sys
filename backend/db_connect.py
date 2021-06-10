import sqlite3
import datetime
import time


class Database():


    db_path = "nordaxon_db.db"

    def __init__(self):
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()


    # Login section

    def user_login(self,email,password):
        try:
            if self.get_email(email):
                user_credentials = self.cur.execute('''SELECT * FROM users WHERE email = "{}"'''.format(email))
                self.con.commit()
                print(user_credentials)
                self.db_close()
                #for user in user_credentials:
                #    if user[3] == password:
                #        print("Password is correct")
                #        #self.update_login_info(user[0])
                #        return True
                    #else:
                    #    print("Something is very wrong")
                    #    return False
            return True
        except:
            print("Nope")
            return False

        self.db_close()


    # User-section

    def get_allusers(self):
        ''' Only for testing purposes..'''
        try:
            user_list = []
            users = self.cur.execute('''SELECT * FROM users''')
            for user in users:
                user_list.append(user)
            self.db_close()
            return user_list
        except:
            return False


    def get_user_by_id(self,id):
        try:
           self.cur.execute('''SELECT * FROM users WHERE id = {}'''.format(int(id)))
           user = self.cur.fetchall()
           print(user[0])
           self.db_close()
           return user[0]
        except:
            print("Can't find user")
            self.db_close()
            return False
            

    def get_email(self,email):
        try:
            self.cur.execute('''SELECT * FROM users WHERE email = "{}"'''.format(email))
            self.cur.fetchall()
            self.db_close()
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
            self.cur.execute('''INSERT INTO users (name,email,password,user_created,last_login,login_amt) \
                VALUES("{}","{}","{}","{}","{}",{})'''.format(name,email,password,now,last_logged_in,int(times_logged_in)))
            self.con.commit()
            print("yes")
            self.db_close()
            return True
            
        except:
            print("no")
            self.db_close()
            return False

    
    def update_user_info(self,id,name,email):
        
        self.cur.execute('''UPDATE users SET name="{}",email="{}" WHERE id = {}'''.format(name,email,id))
        self.con.commit()
        print("Changed some stuff")
        self.db_close()
        return True


    def check_password(self,id,old_password):
        existing_password = self.cur.execute('''SELECT password FROM users WHERE id = {}'''.format(id))
        self.con.commit()
        if old_password == existing_password:
            return True
        else:
            return False

    def update_password(self,id,new_password):
        self.cur.execute('''UPDATE users SET password="{}" WHERE id = {}'''.format(id,new_password))
        self.con.commit()
        self.db_close()
        return True


    def delete_user_by_id(self,id):
        try:
            if self.get_user_by_id(id):
                self.cur.execute('''DELETE FROM users WHERE id = {}'''.format(id))
                self.con.commit()
                self.db_close()
        except:
            return False


    def update_login_info(self,id):
        login_amount = self.cur.execute('''SELECT login_am FROM users''')
        now = datetime.datetime.now()
        self.cur.execute('''UPDATE users SET last_login = "{}", login_am = {}'''.format(now, login_amount+1))
        self.con.commit()
        self.db_close()

    def db_close(self):
        self.cur.close()
        self.con.close()



Database().get_email("adfa")