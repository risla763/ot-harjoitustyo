import sqlite3

class DB:

    def __init__(self):
        self.database = sqlite3.connect("scoreboard.db")
        self.database.isolation_level = None

    def make_table(self):
        self.database.execute("""CREATE TABLE IF NOT EXISTS scoreboard (score INTEGER)""")

    #tämän metodin tekemisessä chatgpt auttoi
    def insert(self,score):
        self.database.execute("INSERT INTO scoreboard VALUES (?)", (score,))

    def fetch_from_scoreboard(self):
        result = self.database.execute("SELECT * FROM scoreboard")
        scores = result.fetchall()
        a = 0
        for tuple in scores:
            if tuple[0] > a:
                a = tuple[0]
        print(a)
        return a

        #tee testi jos ei ole highest scorea?