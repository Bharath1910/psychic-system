import time as t
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.command()
async def latency(ctx):
    await ctx.send({round(client.latency*1000)})

@client.event
async def on_disconnect():
    chat = client.get_channel(775230000542515232)
    await chat.send("you kicked me :(")


@client.event
async def on_ready():
    print("bot is ready")
    chat = client.get_channel(775230000542515232)
    await chat.send("I'm online")
    await chat.send("command lists,")
    await chat.send("1.who are you")
    await chat.send("2.what is the version")
    await chat.send("3.hello")

@client.event
async def on_message(message):
    if message.content == 'who are you':
        chat = client.get_channel(775230000542515232)
        await chat.send("a bot made by @incognito and I don't know what to do till now")
    
    elif message.content == "latency":
        chat = client.get_channel(775230000542515232)
        await chat.send("don't know")
        

    elif message.content == 'version':
        chat = client.get_channel(775230000542515232)
        await chat.send("v0.1.0-beta")
    
    elif message.content == 'hello':
        chat = client.get_channel(775230000542515232)
        await chat.send("hi")

    elif message.content == 'hmmm':
        chat = client.get_channel(775230000542515232)
        await chat.send("hmmmmmmm")

    elif message.content == 'what':
        chat = client.get_channel(775230000542515232)
        await chat.send("what??")
    
    elif message.content == 'go offline':
        chat = client.get_channel(775230000542515232)
        await chat.send("shutting down system...")



client.run('Nzc0MjcyMjYyNDE2MjM2NTU0.X6VXPA.kV63vVS5wHnBhBE1IdJDP-Sjjl4')



