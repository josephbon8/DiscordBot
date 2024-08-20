import discord 
from discord.ext import commands

intents= discord.Intents.all()
intents.members=True
client= commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_start():
    print('The bot has been initialized')

@client.command()
async def hello(ctx):
    await ctx.send("Hey I'm the discord bot")

@client.event
async def member_join(member):
    print("hi")


@client.event
async def on_member_join(member):
    channel= client.get_channel(940030346186080269)
    await channel.send('hello')

client.run('MTI2NDI1NTUxNjQ2MTUwMjQ4NA.G3EHbw.4nsXZgRWEacYA-gvn6m1W0Hh_UETiA6PVr-fd4')
