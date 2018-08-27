import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os 

Client = discord.client()
client = commands.Bot(command_prefix = "+")


@client.event
async def on_ready():
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(client.user.name)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print ("|[       Bot is Online      ]|")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    await client.change_presence(game=discord.Game (name="abokhalil"))
@client.event
async def on_message(message):
    if message.content.startswith(command_prefix + 'ping'):
        msg = :ping_pong: Po0o0nG !!
        await client.send_message(message.channel, msg)
    
        
bot.run(os.environ['BOT_TOKEN']) 
