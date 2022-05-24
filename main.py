import discord
import os
from dotenv import load_dotenv


client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send("Hi, how are you doing, everything is operational")

    if message.content == '$private':
        await message.author.send("Hey, what can I help you with?")



@client.event
async def on_connect():
    print("Bot Initiated, now online.......Good to Go!")
    channel = client.get_channel(978487223869665313)
    await channel.send("Connected to general")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm.send(f"Hey {member}, thanks for joining")



client.run(TOKEN)