#MIT License

#Copyright (c) 2021 DevLogger

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.



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
    #----Loads the example_cog when the bot starts----#
    bot.load_extension("cogs.example_cog")
    
#----A simple command to use in you're bot
@bot.command()
async def hello(ctx):
    await ctx.send("Hello ", ctx.author.mention, "!")
    
#----Used to run this bot----#
bot.run(read["token"])
