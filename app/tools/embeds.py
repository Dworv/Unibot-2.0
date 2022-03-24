
import interactions as inter
import const

def build_embed(message, **infos):
    if infos:
        return inter.Embed(
            title=message,
            color=const.METADATA['color'],
            fields = [
                inter.EmbedField(name=info[0], value=info[1], inline=True)
                for info in list(infos.items())
            ]
        )
    else:
        return inter.Embed(
            description=message,
            color=const.METADATA['color']
        )

