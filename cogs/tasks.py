import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle([
	"This message changes every 10 seconds",
	"I'm programmed in python with discord.py",
	"My coder is Yaminox7#9900",
	"Use the help command to see my features"
    ])

class Tasks(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.change_status.start()

	def cog_unload(self):
		self.change_status.cancel()

	@tasks.loop(seconds=10)
	async def change_status(self):
		await self.bot.change_presence(activity=discord.Game(next(status)))


async def setup(bot):
	await bot.add_cog(Tasks(bot))