
from .editor import Editor

class Member:
    def __init__(self, data: list, editor: Editor):
        self.user_id = int(data[0])
        self.rank = data[1]
        self.name = data[2]
        self.youtube = data[3]

        self._editor = editor

    def update_rank(self, rank: str):
        self._editor.edit_member(self.user_id, 'rank', rank)
        self.rank = rank
    
    def update_name(self, name: str):
        self._editor.edit_member(self.user_id, 'name', name)
        self.name = name
    
    def update_youtube(self, youtube: str):
        self._editor.edit_member(self.user_id, 'youtube', youtube)
        self.youtube = youtube