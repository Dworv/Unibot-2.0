
import interactions as inter
from interactions.ext.enhanced import *
from interactions.ext.checks import check

import const
from tools import build_embed, build_review_modal

class Review(EnhancedExtension):
    
    @inter.extension_component('review_button')
    async def open_review_modal(self, ctx: inter.ComponentContext):
        application = self.client.database.search_applications('review_msg_id', int(ctx.message.id))

        if not application:
            await ctx.send(embeds=build_embed('That application does not seem to exist in the database.'), ephemeral=True)
            return
        application = application[0]
        if application.status != 0:
            await ctx.send(embeds=build_embed('That application has already been reviewed.'), ephemeral=True)
            return
        
        # TODO: change to bot.get when availible
        applicant = inter.Member(**await self.client._http.get_member(const.METADATA['guild'], application.applicant_id))
        
        await ctx.popup(
            modal=build_review_modal(
                application.application_id,
                applicant, 
                'Trial' if const.METADATA['role']['trial'] in applicant.roles else 'None'
            )
        )

    @extension_modal('review_modal', startswith=True)
    async def review_modal(self, ctx: inter.CommandContext):
        app_id = ctx.data.custom_id.split(':')[1]
        print(app_id)
        application = self.client.database.get_application(int(app_id))
        await ctx.send(str(application))


def setup(bot):
    Review(bot)