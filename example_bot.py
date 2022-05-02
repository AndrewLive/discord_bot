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

        print(message.content)
        await message.channel.send('Message from {0.author}: {0.content}'.format(message))


client = MyClient()

TOKEN = 'OTcwNTEzODY5MDUzMjUxNjE2.Ym9DeQ.zMMdSZ9m6b2-U9H2Vcx20VyXEw0'
client.run(TOKEN)