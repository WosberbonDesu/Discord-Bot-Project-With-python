#MAKE SURE YOU INSTALLED EVERYTHING CORRECTLY 
#BOT WILL ONLINE ONLY THIS CODE RUNNING 
#TOKEN PART IS IMPORTANT MAKE SURE USING YOUR ON TOKEN
#DON'T FORGET PASTE YOUT TOKEN TO THE LAST CODE LINE
#IF YOU DON'T KNO HOW TO CREATE TOKEN YOU MUST GO TO DISCORD DEVOLOPER PANEL THEN YOU CAN EASILY MAKE TOKEN FOR YOUR BOT


import discord
from discord import channel
from discord.ext import commands
import random
from pathlib import Path
import youtube_dl
from discord import FFmpegPCMAudio
from discord.utils import get

client = commands.Bot(command_prefix = ".") #you can easily change inside nail if you type in * it will understand command when you put * front of commands

players = {}

@client.event 

async def on_ready():
    print("Bot is ready.")     #it means when you run this code it will be print this you can understand your code is runnig or not



@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms") #when you type .ping it will be print your ping 
@client.command(aliases=["hi","hello"])    #same thing here .hi or .hello will be print randomly theree of them
async def _hi(ctx, *,question):
    resp = ["Hello there",
            "Hello miss",
            "Hello mister"]
    await ctx.send(f"İşte Cevabın: {random.choice(resp)}")

@client.command(aliases=["c","test"])
async def _c(ctx, *,question):
    responses = [
                 "Bir cisim yaklaşıyor efendim"
                ]
    await ctx.send(f"Sorduğun:{question}\nİşte Cevabın: {random.choice(responses)}")
 #MUSIC BOT PART
@client.command(pass_context =True)
async def join(ctx):                                 #First of all you must type .join when you are in voice channel
    channel = ctx.message.author.voice.voice_channel
    await  client.join_voice_channel(channel)

@client.command(pass_context=True)       #if you type .leave it means bot is leaving
async def leave(ctx):
    server = ctx.message.server 
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context = True)     #play command .play and music name or muisc link in youtube
async def play(ctx, url):
    server = ctx.message.server 
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context = True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id]
    players[id].pause()

@client.command(pass_context = True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id]
    players[id].stop()

@client.command(pass_context = True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id]
    players[id].resume()

    

client.run("PASTE YOUR TOKEN HERE OTHERWISE YOUR BOT IS NOT GONNA WORK")

