import discord
import random
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah login sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ini adalah echo-bot yang dibuat dengan pustaka discord.py!')

@client.command()
async def info(ctx):
    await ctx.send('saya merupakan bot yang terbatas yang sedang dalam proses')

@client.command()
async def lemparkoin(ctx):
    hasil = random.choice(['Head', 'Tails'])
    await ctx.send(f'Koin dilempar dan hasilnya adalah {hasil}!')

@client.command()
async def angka(ctx):
    hasil2 = random.randint(1, 100)
    await ctx.send(f'Angka acakmu adalah {hasil2}!')

client.run(token)