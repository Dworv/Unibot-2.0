
import interactions as inter
from interactions.ext.enhanced import *
from interactions.ext.checks import check

import const
from checks import can_apply

class Apply(EnhancedExtension):
    """An extension dedicated to /apply."""

    @inter.extension_command()
    @check(can_apply)
    async def apply(
        self, 
        ctx: inter.CommandContext,
        url: EnhancedOption(str, 'The url to your application'),
    ):
        """Apply to become a member of the Universe Editing Team"""
        await ctx.send('it worked')

        

def setup(bot):
    Apply(bot)