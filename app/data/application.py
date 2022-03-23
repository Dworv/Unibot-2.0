
from .editor import Editor

class Application:
    def __init__(self, data: list, editor: Editor):
        self.application_id: int = int(data[0])
        self.applicant_id: int = int(data[1])
        self.review_msg_id: int = int(data[2])
        self.status: int = int(data[3])
        self.url: str = data[4]

        self._editor = editor
    
    