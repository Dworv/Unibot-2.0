
import interactions as inter
from interactions.ext import enhanced

import logging, os
from const import *

# logging.basicConfig(level=logging.DEBUG)

bot = inter.Client(
    TOKEN,
    presence=inter.ClientPresence(
        activities=[
            inter.PresenceActivity(
                name="International Editing",
                url='https://www.youtube.com/c/universeediting',
                type=inter.PresenceActivityType.STREAMING
            ),
        ],
        status=inter.StatusType.IDLE,
    ),
)

# load global exts
bot.load('interactions.ext.enhanced', debug_scope=DATA['guild'])

# load local exts
[
    bot.load(
    f"exts.{file.removesuffix('.py')}"
    )

    for file 
    in os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "exts")) 
    if not file.startswith("_")
]

# on ready
@bot.event
async def on_ready():
    print(f"Bot is ready (logged in as {bot.me.name})")

bot.start()