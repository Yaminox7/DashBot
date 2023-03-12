import discord
from discord.ext import commands
import os
from PIL import Image
import qrcode
import random

class Utility(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.__doc__ = "Useful server commands"

	@commands.command(help="Shows the profile picture of a member")
	async def avatar(self, ctx, member:discord.Member=None):
		member = member if member else ctx.message.author
		asset = member.avatar
		file = await asset.to_file(filename=f"{member.name}.png")
		await ctx.send(file=file)

	@commands.command(help="Generate and shows a random color", aliases=["colour"])
	async def color(self, ctx):
		color = (random.choice(range(256)), random.choice(range(256)), random.choice(range(256)))
		hexa = "{:02X}{:02X}{:02X}".format(*color)
		dec = int(hexa, 16)
		name = "color" + ctx.message.author.display_name
		color_image = Image.new("RGB", (80, 50), color=color)
		color_image.save(f"{name}.png")
		color_file = discord.File(f"{name}.png", filename=f"{name}.png")
		embed = discord.Embed(description=f"**Hex**: #{hexa}\n**Dec**: {dec}\n**RGB**: rgb{color}", color=discord.Color.from_rgb(*color))
		embed.set_thumbnail(url=f"attachment://{name}.png")
		await ctx.send(file=color_file, embed=embed)
		os.remove(f"{name}.png")

	@commands.command(help="Solves a mathematical expression", aliases=["maths"])
	async def math(self, ctx, *, exp):
		try:
			embed = discord.Embed(title=f"The result of ```{exp}``` is", description=eval(exp))
			await ctx.send(embed=embed)
		except SyntaxError:
			raise discord.ext.commands.BadArgument()

	@commands.command(help="Generate a qrcode off a link or a text")
	async def qrcode(self, ctx, *, link):
		name = "qrcode" + ctx.message.author.display_name
		qr = qrcode.QRCode(version=1, box_size=21, border=0)
		qr.add_data(link) 
		qr.make(fit=True)
		colors = discord.Color.random()
		qrcode_image = qr.make_image(fill_color=(colors.r, colors.g, colors.b), back_color="transparent")
		qrcode_image.save(f"{name}.png")
		qrcode_file = discord.File(f"{name}.png", filename=f"{name}.png")
		embed = discord.Embed()
		embed.set_image(url=f"attachment://{name}.png")
		await ctx.send(file=qrcode_file, embed=embed)
		try:
			os.remove(f"{name}.png")
		except discord.ext.commands.errors.CommandInvokeError: 
			return

	@commands.command(help="Sends a message under the bot's identity")
	async def say(self, ctx, *, text):
		embed = discord.Embed(description=text)
		await ctx.send(embed=embed)

async def setup(bot):
	await bot.add_cog(Utility(bot))