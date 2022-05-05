# Import necessary modules
import discord
from discord.ext import commands
import logging
from googletrans import Translator
from googletrans import LANGUAGES


# configure the logging module
# code taken from the discord.py logging page
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!')

## BOT FUNCTIONS ##

## Passives

# Executes once at the start of the bot's runtime when bot is ready
@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    return

# Executes whenever a message is sent
@bot.event
async def on_message(message): 
    if message.author == bot.user:
        return

    await deez_nuts_check(message)
    # await translate_message(message)

    await bot.process_commands(message)

    return


# Commands
# TODO: add translate and help commands

# Translate Command
# User replies to a message to be translated with the command
@bot.command()
async def translate(ctx, dest='en'):
    if dest not in LANGUAGES:
        await ctx.reply('Invalid language code', mention_author=True)
        return

    if ctx.message.reference == None:
        await ctx.reply('No message to translate', mention_author=True)
        return

    # print(dest)
    original_message = await ctx.fetch_message(ctx.message.reference.message_id)
    await translate_message(original_message, dest)
    return
        


## FUNCTION IMPLEMENTATIONS ##

# Deez Nuts checker
# Finishes the deez nuts joke based on the message sent
async def deez_nuts_check(message):
    for substring in deez_nuts_dict:
        if substring in message.content.lower().strip():
            await message.reply(f'> *{substring}*\n{deez_nuts_dict[substring]}', mention_author=False)

# English Translator
# Automatically translates non-english messages to English
# TODO resolve 2000 char limit problem (possibly use embeds)
async def translate_message(message, dest='en'):
    detectedLang = translator.detect(message.content)
    if detectedLang.lang != dest and detectedLang.confidence > 0.2:
        translated = translator.translate(message.content, dest)
        await message.reply(f'> *{message.content}*\n`{translated.src} to {translated.dest}: confidence: {detectedLang.confidence}`\n{translated.text}', mention_author=False)




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


# Run the discord bot
bot.run(TOKEN)
