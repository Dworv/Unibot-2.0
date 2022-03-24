
from time import time

import interactions as inter
from interactions.ext.enhanced import *
from interactions.ext.checks import check
import validators.url

import const
from checks import can_apply
from tools import build_embed

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
        
        # check if allowed to apply
        applications = self.client.database.search_applications('applicant_id', int(ctx.author.id))
        for application in applications:
            if int(time()) - 604800 < application.date:
                await ctx.send(embeds=build_embed(f'You have already applied within the last week. You can apply again <t:{application.date + 604800}:R>'))
                return

        # check if url is valid
        if not validators.url.url(url):
            await ctx.send(embeds=build_embed('The url you used appeaars to be invalid. Please use a valid url.'))
            return

        # send to reviewing channel
        reviewing_msg = await ctx.send(build)

        # add to database

        # confirm application
        await ctx.send(embeds=build_embed(
            'Application successfully submitted.', 
            URL = url,
        ))


def setup(bot):
    Apply(bot)