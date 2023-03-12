import discord
from discord.ext import commands
import os

class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def clear(self, ctx):
		appinfo = await self.bot.application_info()
		owner = appinfo.owner
		owners_id = owners.id
		if ctx.message.author.id in owners_id:
			os.system("cls")
			for fname in os.listdir("./cogs"):
				if fname.endswith(".py"):
					try:
						await self.bot.unload_extension(f"cogs.{fname[:-3]}")
						await self.bot.load_extension(f"cogs.{fname[:-3]}")
					except discord.ext.commands.errors.ExtensionNotLoaded:
						await self.bot.load_extension(f"cogs.{fname[:-3]}")
					finally:
						print(f"Successfully reloaded `{fname[:-3]}`")
			await ctx.send("Console cleared")
		else:
			raise discord.ext.commands.CommandNotFound()

	@commands.command()
	async def load(self, ctx, extension):
		appinfo = await self.bot.application_info()
		owner = appinfo.owner
		owners_id = owners.id
		if ctx.message.author.id in owners_id:
			if extension == "all":
				for fname in os.listdir("./cogs"):
					if fname.endswith(".py"):
						await self.bot.load_extension(f"cogs.{fname[:-3]}")
						await ctx.send(f"Successfully loaded `{fname[:-3]}`")
			else:
				await self.bot.load_extension(f"cogs.{extension}")
				await ctx.send(f"Successfully loaded `{extension}`")
		else:
			raise discord.ext.commands.CommandNotFound()

	@commands.command()
	async def reload(self, ctx, extension=None):
		appinfo = await self.bot.application_info()
		owner = appinfo.owner
		owners_id = owners.id
		if ctx.message.author.id in owners_id:
			if extension == "all" or extension == None:
				for fname in os.listdir("./cogs"):
					if fname.endswith(".py"):
						try:
							await self.bot.unload_extension(f"cogs.{fname[:-3]}")
							await self.bot.load_extension(f"cogs.{fname[:-3]}")
						except discord.ext.commands.errors.ExtensionNotLoaded:
							await self.bot.load_extension(f"cogs.{fname[:-3]}")
						finally:
							await ctx.send(f"Successfully reloaded `{fname[:-3]}`")
			else:
				try:
					await self.bot.unload_extension(f"cogs.{extension}")
					await self.bot.load_extension(f"cogs.{extension}")
				except discord.ext.commands.errors.ExtensionNotLoaded:
					await self.bot.load_extension(f"cogs.{extension}")
				finally:
					await ctx.send(f"Successfully reloaded `{extension}`")
		else:
			raise discord.ext.commands.CommandNotFound()

	@commands.command()
	async def unload(self, ctx, extension):
		appinfo = await self.bot.application_info()
		owner = appinfo.owner
		owners_id = owners.id
		if ctx.message.author.id in owners_id:
			if extension == "all":
				for fname in os.listdir("./cogs"):
					if fname.endswith(".py"):
						await self.bot.unload_extension(f"cogs.{fname[:-3]}")
						await ctx.send(f"Successfully unloaded `{fname[:-3]}`")
			else:
				await self.bot.unload_extension(f"cogs.{extension}")
				await ctx.send(f"Successfully unloaded `{extension}`")
		else:
			raise discord.ext.commands.CommandNotFound()

async def setup(bot):
	await bot.add_cog(Owner(bot))