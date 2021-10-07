#----Imports needed for the bot----#
from discord.ext import commands
import json

#----get the bot config from config.json----#
with open("config.json", "r")as r:
    read = json.load(r)
    
#----Main Bot code starts----#
bot = commands.Bot(command_prefix = read["prefix"])

#----An event that happen when the bot is online----#
@bot.event
async def on_ready():
    print("Logged in as ", bot.user.name)
    
#----A simple command to use in you're bot
@bot.command()
async def hello(ctx):
    await ctx.send("Hello ", ctx.author.mention, "!")
    
#----Used to run this bot----#
bot.run(read["token"])
