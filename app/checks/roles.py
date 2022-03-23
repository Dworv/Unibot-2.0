
import const

def can_apply(ctx):
    """
    Check if the user can apply.
    """
    return const.METADATA['role']['member'] not in ctx.author.roles and const.METADATA['role']['memberples'] not in ctx.author.roles