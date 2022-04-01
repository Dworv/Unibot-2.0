
from datetime import datetime, timedelta
from time import mktime

import interactions as inter
from interactions.ext.enhanced import *

from tools import build_embed

class Mod(EnhancedExtension):

    @inter.extension_command()
    async def mute(
        self, 
        ctx: inter.CommandContext, 
        target: EnhancedOption(inter.User, "The user to mute"), 
        length: EnhancedOption(
            str,
            'The amount of time to mute them for', 
            choices=[
                inter.Choice(name='60 Seconds', value='60'),
                inter.Choice(name='5 Minutes', value='300'),
                inter.Choice(name='30 Minutes', value='1800'),
                inter.Choice(name='2 Hours', value='7200'),
                inter.Choice(name='6 Hours', value='21600'),
                inter.Choice(name='24 Hours', value='86400'),
                inter.Choice(name='3 Days', value='259200'),
                inter.Choice(name='7 Days', value='604800'),
                inter.Choice(name='3 Weeks', value='1814400')
            ]
        ),
        reason: EnhancedOption(str, 'The reason you are muting them (optional)') = 'Not provided'
    ):  
        """The command to mute a user"""
        #TODO: MAKE WORK LMAO
        muted_until = datetime.now() + timedelta(seconds=int(length))
        await target.modify(ctx.guild_id, communication_disabled_until=muted_until.isoformat())
        await ctx.send(embeds=build_embed(f"{target.mention} has been muted until <t:{int(mktime(muted_until.timetuple()))}:F>"))


def setup(bot):
    Mod(bot)