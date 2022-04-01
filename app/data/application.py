from .editor import Editor


class Application:
    def __init__(self, data: list, editor: Editor):
        self.application_id: int = int(data[0])
        self.applicant_id: int = int(data[1])
        self.review_msg_id: int = int(data[2])
        self.status: str = int(data[3])
        self.url: str = data[4]
        self.date: int = int(data[5])
        self.reviewer_id = int(data[6])

        self._editor = editor

    def update_status(self, status: str):
        self._editor.edit_application(self.application_id, "status", status)
        self.status = status

    def update_reviewer(self, reviewer_id: int):
        self._editor.edit_reviewer(self.application_id, "reviewer_id", reviewer_id)
