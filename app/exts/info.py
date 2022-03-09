
import interactions as i
from interactions.ext import better_interactions as b

import const

class Info(i.Extension):
    """An extension dedicated to /info."""

    def __init__(self, client: i.Client):
        client.load('interaction.ext.bett')

    @i.extension_command(
        name="info",
        description="Get information about the bot.",
        scope=const.DATA["guild"]
    )
    async def info(self, ctx: i.CommandContext):
        embed = i.Embed(
            title="Info"
        )
        await ctx.send(embeds=embed)
    
def setup(bot):
    Info(bot)