
import interactions as inter
from interactions.ext.enhanced import *
from interactions.ext.checks import check

import const
from tools import build_embed

class Review(EnhancedExtension):
    ...

def setup(bot):
    Review(bot)