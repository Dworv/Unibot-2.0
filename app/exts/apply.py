
import time

import interactions as inter
from interactions.ext.enhanced import *
from interactions.ext.checks import check

import const
from checks import can_apply
from tools import build_response_embed

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
            if int(time.time()) - 604800 < application.date:
                await ctx.send(embeds=build_response_embed(f'You have already applied within the last week. You can apply again <t:{application.date + 604800}:R>'))
                return

        # check if url is valid

        # add to database

        # send to reviewing channel

        # confirm application
        await ctx.send(embeds=build_response_embed(
            'Application successfully submitted.', 
            url = url,
        ))


def setup(bot):
    Apply(bot)