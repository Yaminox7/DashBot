import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config")

token = os.getenv("TOKEN")
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
	print("Bot connected")
	for fname in os.listdir("./cogs"):
		if fname.endswith(".py"):
			await bot.load_extension(f"cogs.{fname[:-3]}")
			liste = list(filter(lambda x: True if x.endswith("py") else False, list(os.listdir("./cogs"))))
			percentage = round((liste.index(fname) + 1) * 10000 / len(liste)) / 100
			print(f"loaded `cogs.{fname[:-3]}` successfully    |	{percentage}%")

bot.run(token)