class Editor:
    def __init__(self, con, cur):
        self.con = con
        self.cur = cur

    def create_application(self, applicant_id, review_msg_id, status, url, date):
        res = self.cur.execute(
            "INSERT INTO applications (applicant_id, review_msg_id, status, url, date, reviewer_id) VALUES (?, ?, ?, ?, ?, ?) RETURNING *",
            (applicant_id, review_msg_id, status, url, date),
        )
        data = next(res)
        self.con.commit()
        return data

    def create_member(self, user_id, rank, name, youtube):
        res = self.cur.execute(
            "INSERT INTO members (user_id, rank, name, youtube) VALUES (?, ?, ?, ?) RETURNING *",
            (user_id, rank, name, youtube),
        )
        data = next(res)
        self.con.commit()
        return data

    def edit_application(self, application_id, field, value):
        self.cur.execute(
            f"UPDATE applications SET {field} = ? WHERE application_id = ?",
            (value, application_id),
        )
        self.con.commit()

    def edit_member(self, user_id, field, value):
        self.cur.execute(
            f"UPDATE members SET {field} = ? WHERE user_id = ?", (value, user_id)
        )
        self.con.commit()
