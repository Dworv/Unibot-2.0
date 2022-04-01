
from time import time

import interactions as inter
from interactions.ext.enhanced import *
from interactions.ext.checks import check
import validators.url

import const
from checks import can_apply
from tools import build_embed
from data import Application

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
        applications: Application = self.client.database.search_applications('applicant_id', int(ctx.author.id))
        for application in applications:
            if int(time()) - 604800 < application.date:
                await ctx.send(embeds=build_embed(
                    f'Only one app per week. You can apply again <t:{application.date + 604800}:R>',
                    Last_Application_Data=f'<t:{application.date}:F>',
                    Previous_Application=application.url
                ))
                return

        # check if url is valid
        if not validators.url(url):
            await ctx.send(embeds=build_embed('The link you used appeaars to be invalid. Please use a valid url.'))
            return

        # send to reviewing channel
        reviewing_channel = self.client.get(
            inter.Channel, 
            channel_id=const.METADATA['channel']['reviewing']
        )

        has_trail = const.METADATA['role']['trial'] in ctx.author.roles

        reviewing_msg = await reviewing_channel.send(
            url, 
            embeds=build_embed(
                'New Application!',
                Rank='Trial' if has_trail else 'None',
                URL=url,
                User=ctx.author.mention
            ),
            components=[# TODO: MAKE REVIEW SELECT MENU BY PUTTING NEW RANK IN CUSTOM_ID
                inter.Button(
                    custom_id='review_button',
                    style=inter.ButtonStyle.SUCCESS,
                    label='Review',
                )
            ]
        )

        # add to database
        self.client.database.new_application(
            int(ctx.author.id), 
            int(reviewing_msg.id), 
            0, 
            url
        )

        # confirm application
        await ctx.send(embeds=build_embed(
            'Application successfully submitted.', 
            URL=url,
        ))
        

def setup(bot):
    Apply(bot)