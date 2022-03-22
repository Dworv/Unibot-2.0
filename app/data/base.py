
import sqlite3, os

class Database:
    def __init__(self):
        self.con = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'unibot.db'))
        self.cur = self.con.cursor()

        # create tables
        self.cur.execute("CREATE TABLE IF NOT EXISTS guilds (id INTEGER PRIMARY KEY, name TEXT, prefix TEXT, enabled INTEGER)")

