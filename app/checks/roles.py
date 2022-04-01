import const
from tools import build_embed


async def can_apply(ctx):
    """
    Check if the user can apply.
    """
    if const.METADATA["role"]["member"] in ctx.author.roles:
        await ctx.send(
            embeds=build_embed(
                "To apply for Member+, you need to ask the staff so they can promote you."
            )
        )
        return False
    if const.METADATA["role"]["memberplus"] in ctx.author.roles:
        await ctx.send(
            embeds=build_embed("You have already reached the highest level of editor.")
        )
        return False
    if const.METADATA["role"]["reviewer"] in ctx.author.roles:
        await ctx.send(embeds=build_embed("Reviewers are not allowed to apply"))
        return False
    return True
