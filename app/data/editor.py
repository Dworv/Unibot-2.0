
class Editor:
    def __init__(self, con, cur):
        self.con = con
        self.cur = cur
    
    def create_application(self, applicant_id, review_msg_id, status, url):
        res = self.cur.execute(
            'INSERT INTO applications (applicant_id, review_msg_id, status, url) VALUES (?, ?, ?, ?) RETURNING *',
            (applicant_id, review_msg_id, status, url)
        )
        data = next(res)
        self.con.commit()
        return data
    
    def create_member(self, user_id, rank, name, youtube):
        res = self.cur.execute(
            'INSERT INTO members (user_id, rank, name, youtube) VALUES (?, ?, ?, ?) RETURNING *',
            (user_id, rank, name, youtube)
        )
        data = next(res)
        self.con.commit()
        return data