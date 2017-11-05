#! /usr/bin/env python3

import discord, sqlite3, logging
from discord.ext.commands import Bot
import secrets

statbot = Bot(command_prefix='!')
startup_extensions = ['cogs.pubg', 'cogs.wow', 'cogs.d3', 'cogs.info', 'cogs.destiny2']

conn = sqlite3.connect('db/statbot.db')
cur = conn.cursor()
logging.basicConfig(level=logging.INFO)


@statbot.event
async def on_ready():
    print('Client logged in.')
    print(statbot.user.id)
    print('-----')
    await statbot.change_presence(game=discord.Game(name="Stats"))

    for extension in startup_extensions:
        try:
            statbot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extensions {}\n {}'.format(extension, exc))


statbot.run(secrets.BOT_TOKEN)
