# Import necessary modules
import discord
from discord.ext import commands
import logging
from googletrans import Translator


# configure the logging module
# code taken from the discord.py logging page
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class MyClient(discord.Client):
    # Executes once at the start of the bot's runtime when bot is ready
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # Executes whenever a message is sent
    async def on_message(self, message): 
        if message.author == bot.user:
            return

        await self.deez_nuts_check(message)
        await self.translate_message(message)
            
    # Deez Nuts checker
    # Finishes the deez nuts joke based on the message sent
    async def deez_nuts_check(self, message):
        for substring in deez_nuts_dict:
            if substring in message.content.lower().strip():
                await message.reply(f'> *{substring}*\n{deez_nuts_dict[substring]}', mention_author=False)

    # English Translator
    # Automatically translates non-english messages to English
    # TODO resolve 2000 char limit problem (possibly use embeds)
    async def translate_message(self, message):
        detectedLang = translator.detect(message.content)
        if detectedLang.lang != "en" and detectedLang.confidence > 0.2:
            translated = translator.translate(message.content, "en")
            await message.reply(f'> *{message.content}*\n`{translated.src} to {translated.dest}: confidence: {detectedLang.confidence}`\n{translated.text}', mention_author=False)

    # TODO commands for translate and help and an admin kill


# Commands




# Read file to get the bot token
# format is {token: <token here>} on the first line of the file
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


# Initialize the Translator object
translator = Translator()


# Run the discord client
bot = MyClient()
bot.run(TOKEN)
