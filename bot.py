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
        counter = 0
        tmp = await client.send_message(message.channel, 'pong...!')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith(command_prefix + 'sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        
    
        
bot.run(os.environ['BOT_TOKEN']) 
