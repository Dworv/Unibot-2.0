
import interactions as i
from interactions.ext import better_interactions as b

import logging, os
from const import *

# logging.basicConfig(level=logging.DEBUG)

bot = i.Client(
    TOKEN,
    presence=i.ClientPresence(
        activities=[
            i.PresenceActivity(
                name="International Editing",
                url='https://www.youtube.com/c/universeediting',
                type=i.PresenceActivityType.STREAMING
            ),
        ],
        status=i.StatusType.IDLE,
    ),
)

# load global exts
bot.load('interactions.ext.better_interactions')

# load local exts
[
    bot.load(
    f"exts.{file.removesuffix('.py')}"
    )

    for file 
    in os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "exts")) 
    if not file.startswith("_")
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.me.name}.")

bot.start()