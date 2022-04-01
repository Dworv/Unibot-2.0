import interactions as inter
from interactions.ext import enhanced

import const


class Gadgets(enhanced.EnhancedExtension):
    """An extension for basic tools."""

    @inter.extension_command()
    async def ping(self, ctx: inter.CommandContext):
        """Returns a "Pong!" if the bot is working correctly."""

        await ctx.send("Pong!")


def setup(bot):
    Gadgets(bot)
