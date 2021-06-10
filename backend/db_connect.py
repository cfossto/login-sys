import sqlite3


class Database():

    db_path = "nordaxon_db.db"

    def __init__(self):
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()


    def get_allusers(self):
        try:
            users = self.cur.execute('''SELECT * FROM users''')
            for user in users:
                print(user)
        except:
            return False


    def get_user_by_id(self,id):
        try:
           self.cur.execute('''SELECT * FROM users WHERE id = {}'''.format(int(id)))
           user = self.cur.fetchall()
           print(user[0])
        except:
            print("Can't find user")



Database().get_allusers()
Database().get_user_by_id(1)