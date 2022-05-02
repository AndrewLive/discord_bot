import discord
import logging

# configure the logging module
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message): 
        if message.author == client.user:
            return

        print('Message from {0.author}: {0.content}'.format(message))
        await message.channel.send('Message from {0.author}: {0.content}'.format(message))


client = MyClient()

# Read file to get the bot token
# format is token: <token here> on the first line of the file
config_file = open("discord_bot\example_bot.config", "r")

TOKEN = config_file.readline().split()[1]
print(TOKEN)

config_file.close()

client.run(TOKEN)