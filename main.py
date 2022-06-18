from click import command
import discord
from discord.ext import commands
TOKEN = ""
bot = commands.Bot(command_prefix="&")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello " + ctx.message.author.mention)

@bot.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention)
    except:
        await ctx.send("bot does not have the right perms!")



bot.run(TOKEN)