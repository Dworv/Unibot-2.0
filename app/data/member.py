
from .editor import Editor

class Member:
    def __init__(self, data: list, editor: Editor):
        self.user_id = int(data[0])
        self.rank = data[1]
        self.name = data[2]
        self.youtube = data[3]

        self._editor = editor
