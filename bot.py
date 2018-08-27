import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os 

Client = discord.client()
client = commands.Bot(command_prefix = "+")


@Clent.event
async def on_ready():
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(client.user.name)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print ("|[       Bot is Online      ]|")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    await client.change_presence(game=discord.Game (name="abokhalil"))
@Cient.event
async def on_message(message):
    if message.content.startswith(command_prefix + 'ping'):
        await client.send_message(message.channel, ":ping_pong: Po0o0nG !!")
    
        
Cient.run(os.environ['BOT_TOKEN']) 
