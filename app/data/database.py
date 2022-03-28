
import sqlite3, os, time
from .tables import members_create, applications_create
from .application import Application
from .member import Member
from .editor import Editor

class Database:
    def __init__(self):
        self.con = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'unibot.db'))
        self.cur = self.con.cursor()
        self.editor = Editor(self.con, self.cur)

        # create tables
        self.cur.execute(members_create)
        self.cur.execute(applications_create)

    # member methods
    def new_member(self, user_id: int, rank: str, name: str, youtube: str) -> Member:
        data = self.editor.create_member(user_id, rank, name, youtube)
        return Member(data, self.editor)

    def get_member(self, user_id: int) -> Member:
        self.cur.execute('SELECT * FROM members WHERE user_id = ?', (user_id,))
        res = self.cur.fetchone()
        if not res:
            return None
        return Member(res, self.editor)
    
    def search_members(self, field, value):
        self.cur.execute(f'SELECT * FROM members WHERE {field} = ?', (value,))
        return [Member(data, self.editor) for data in self.cur.fetchall()]
    
    class member_fields:
        rank = 'rank'

    # application methods
    def new_application(self, applicant_id: int, review_msg_id: int, status: str, url: str) -> Application:
        data = self.editor.create_application(applicant_id, review_msg_id, status, url, int(time.time()))
        return Application(data, self.editor)
    
    def get_application(self, application_id: int) -> Application:
        self.cur.execute('SELECT * FROM applications WHERE application_id = ?', (application_id,))
        res = self.cur.fetchone()
        if not res:
            return None
        return Application(res, self.editor)
    
    def search_applications(self, field, value):
        self.cur.execute(f'SELECT * FROM applications WHERE {field} = ?', (value,))
        return [Application(data, self.editor) for data in self.cur.fetchall()]

    class application_fields:
        applicant_id = 'applicant_id'
        review_msg_id = 'review_msg_id'
        status = 'status'
