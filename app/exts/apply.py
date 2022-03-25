
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
                await ctx.send(embeds=build_embed(
                    f'You have already applied within the last week. You can apply again <t:{application.date + 604800}:R>',
                    infos = {
                        'Last Date': f'<f:{application.date}:F',
                        'Last App': application.url
                    }
                ))
                return

        # check if url is valid
        if not validators.url.url(url):
            await ctx.send(embeds=build_embed('The url you used appeaars to be invalid. Please use a valid url.'))
            return

        # send to reviewing channel
        # TODO: change to bot.get
        reviewing_channel = inter.Channel(**self.client._http.get_channel(const.METADATA['channel']['reviewing']))
        reviewing_channel._client = self.client._http

        has_trail = const.METADATA['role']['trial'] in ctx.author.roles

        reviewing_msg = await reviewing_channel.send(
            url, 
            embeds=build_embed(
                'New Application!',
                infos = {
                    'Rank:': 'Trial' if has_trail else 'None',
                    'URL': url,
                    'User': ctx.author.mention
                }
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