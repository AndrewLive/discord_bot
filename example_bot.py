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

        ## print('Message from {0.author}: {0.content}'.format(message))
        ## await message.channel.send('Message from {0.author}: {0.content}'.format(message))
        await self.deez_nuts_check(message)

    async def deez_nuts_check(self, message):
        for substring in deez_nuts_dict:
            if substring in message.content.lower().strip():
                await message.reply(f'> *{substring}*\n{deez_nuts_dict[substring]}', mention_author=False)


client = MyClient()

# Read file to get the bot token
# format is token: <token here> on the first line of the file
config_file = open("discord_bot\example_bot.config", "r")

TOKEN = config_file.readline().split()[1]
print(TOKEN)

config_file.close()


# Read deez_nutz file to get dictionary of deez nutz replies
deez_nuts_file = open("discord_bot\deez_nuts.txt", "r")

deez_nuts_dict = {}
for i in deez_nuts_file.readlines():
    i = i.strip().split(": ")
    deez_nuts_dict[i[0]] = i[1]

deez_nuts_file.close()


# Run the discord client
client.run(TOKEN)