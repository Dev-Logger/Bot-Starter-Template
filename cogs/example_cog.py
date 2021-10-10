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



#----Imports needed for the cog----#
from discord.ext import commands

#----Main Cog code starts----#
class example_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #----An event that happen when the cog is loaded----#
    @commands.Cog.listiener()
    async def on_ready(self):
        print("example cog loaded")
        
    #----A simple command to use in you're bot
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("Hello, " ctx.author.mention, "!")
        
#----Used to add this cog to the bot----#
def setup(self, bot):
    bot.add_cog(example_cog(bot))
