
import interactions as i
from interactions.ext import better_interactions as b

import const

class Info(i.Extension):
    """An extension dedicated to /info."""

    @i.extension_command(scope=const.DATA["guild"])
    async def info(self, ctx: i.CommandContext):
        """Get information about UniBot 2.0"""

        embed = i.Embed(
            title="UniBot 2.0",
            description="UniBot is a discord bot written in python using the `interactions.py` library.",
            color=const.DATA['color'],
            fields=[
                i.EmbedField(
                    name='Development Start',
                    value='<t:1646890200:f>',
                    inline=True
                ),
                i.EmbedField(
                    name='Version',
                    value=const.VERSION,
                    inline=True
                ),
                i.EmbedField(
                    name='Authors',
                    value='\n'.join(const.AUTHORS),
                    inline=True
                ),
                i.EmbedField(
                    name='What is this for',
                    value="""
UniBot 2.0, a bot written to replace the original UniBot written by G_bby, was built due to the Discord API v6 going EOL in April, 2022.
Using the new slash commands, buttons and modals, UniBot 2.0 aims to automate the applying and reviewing process that was already made simple with the previous bot.
We, the developing team, hope you enjoy using the bot. You can contact us in GitHub at https://github.com/Dworv/UniBot-2.0
"""
                )
            ]
        )
        await ctx.send(embeds=embed)
    
def setup(bot):
    Info(bot)