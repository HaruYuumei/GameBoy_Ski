import sqlite3

##
##  And one day...
##  ... I also hope I can come to love the "Me"...
##  ... That made you say "I love you"
##
##  - Hoshina Subaru - Kaoru Hana wa Rin to Saku
##

class DBProxy:

    def __init__(self,db_name:str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS dados (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            score INTEGER NOT NULL)''')

    def save(self,score:int):
        self.connection.execute('''INSERT INTO dados (score) VALUES (0)''', {'score': score})
        self.connection.execute("INSERT INTO dados (score) VALUES (:score)",{'score':score})
        self.connection.commit()

    def retrieve_top3(self) -> list:
        return self.connection.execute("SELECT * FROM dados ORDER BY score DESC LIMIT 3").fetchall()

    def close(self):
        return self.connection.close()