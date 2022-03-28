
import datetime

from typing_extensions import Annotated
import interactions as inter
from interactions.ext.enhanced import *

class Mod(EnhancedExtension):

    @inter.extension_command()
    async def mute(
        self, 
        ctx: inter.CommandContext, 
        target: Annotated[inter.Member, EnhancedOption(description='The user to mute')], 
        length: Annotated[
            str, 
            EnhancedOption(
                description='The amount of time to mute them for', 
                choices=[]
            )
        ],
        reason: str = 'Not provided'
    ):...
        # await target.modify(ctx.guild_id, communication_disabled_until=datetime.)


def setup(client):
    Mod(client)