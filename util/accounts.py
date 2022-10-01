from util import dbconnection as db

class Accounts:
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password

    def login(self):
        dbConect = db.DatabaseConnect()
        query = "select * from accounts where username = %s and password = %s"
        curs = dbConect.cursor()
        curs.execute(query,[(self.user),(self.password)])
        results = curs.fetchall()
        print(results)
        dbConect.disconnect()