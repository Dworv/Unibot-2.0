
import interactions as inter
from interactions.ext import enhanced

import const

class Info(enhanced.EnhancedExtension):
    """An extension dedicated to /info."""

    @inter.extension_command()
    async def info(self, ctx: inter.CommandContext):
        """Get information about UniBot 2.0"""

        embed = inter.Embed(
            title="UniBot 2.0",
            description="UniBot is a discord bot written in python using the `interactions.py` library.",
            color=const.METADATA['color'],
            fields=[
                inter.EmbedField(
                    name='Development Start',
                    value='<t:1646890200:f>',
                    inline=True
                ),
                inter.EmbedField(
                    name='Version',
                    value=const.VERSION,
                    inline=True
                ),
                inter.EmbedField(
                    name='Authors',
                    value='\n'.join(const.AUTHORS),
                    inline=True
                ),
                inter.EmbedField(
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