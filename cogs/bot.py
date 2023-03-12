import discord
from discord.errors import Forbidden
from discord.ext import commands
import pkg_resources
import platform
import time

async def send_embed(ctx, embed):
	try:
		await ctx.send(embed=embed)
	except Forbidden:
		try:
			await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
		except Forbidden:
			await ctx.author.send(
				f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
				f"May you inform the server team about this issue? :slight_smile: ", embed=embed)

class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.__doc__ = "Informations about Dash Bot"

	@commands.command(help="Shows some of the bot's informations")
	async def botinfo(self, ctx):	
		appinfo = await self.bot.application_info()
		owner = appinfo.owner
		owner_id = owner.id
		prefix = "-"
		version = 1.4
		owner_id = owner_id
		owner_name = owner.name + "#" + owner.discriminator
		python_version = platform.python_version()
		discord_version = pkg_resources.get_distribution("discord.py").version
		servers = self.bot.guilds
		first = second = third = None
		for server in list(servers):
			if not first:
				first = server
			elif server.member_count > first.member_count:
				third = second
				second = first
				first = server
			elif not second:
				second = server
			elif server.member_count > second.member_count:
				third = second
				second = server
			elif not third:
				third = server
			elif server.member_count > third.member_count:
				third = server
		first = "-" + first.name if type(first) == discord.Guild else ""
		second = ",\n-" + second.name if type(second) == discord.Guild else ""
		third = ",\n-" + third.name if type(third) == discord.Guild else ""
		first = "``" + first if second else first
		third = third + "``" if second else third
		embed = discord.Embed(title="Bot infos") 
		embed.add_field(name="Prefix:", value=f"`{prefix}`")
		embed.add_field(name="Owner:", value=f"`{owner_name}`")
		embed.add_field(name="Owner id:", value=f"`{owner_id}`")
		embed.add_field(name="Version:", value=f"`{version}`")
		embed.add_field(name="Python version:", value=f"`{python_version}`")
		embed.add_field(name="Discord.py version:", value=f"`{discord_version}`")
		embed.add_field(name="Servers number:", value=f"`{len(list(servers))}`")
		embed.add_field(name="Top 3 servers:", value=f"`{first}{second}{third}`")
		await ctx.send(embed=embed)

	@commands.command(help="Shows list of Dash Bot's modules and commands with their descriptions")
	# @commands.bot_has_permissions(add_reactions=True,embed_links=True)
	async def help(self, ctx, *input):
		donshow = ["events", "tasks", "owner"]
		appinfo = await self.bot.application_info()
		owner = appinfo.owner
		owner_id = owner.id

		prefix = "-"
		version = 1.0
	 
		owner = owner_id

		if not input:
			try:
				owner = ctx.guild.get_member(owner).mention
			except AttributeError as e:
				owner = owner

			emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
								description=f'Use `{prefix}help <module>` to gain more information about that module\n')

			cogs_desc = ''
			for cog in self.bot.cogs:
				cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n' if not (cog.lower() in donshow) else ""

			emb.add_field(name='Modules', value=cogs_desc, inline=False)

		elif len(input) == 1:
			for cog in self.bot.cogs:
				if cog.lower() == input[0].lower() and not (input[0].lower() in donshow):

					emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
										color=discord.Color.green())

					for command in self.bot.get_cog(cog).get_commands():
						if not command.hidden:
							emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
					break
			else:
				emb = discord.Embed(title="What's that?!",
									description=f"I've never heard from a module called `{input[0]}` before",
									color=discord.Color.orange())

		elif len(input) > 1:
			emb = discord.Embed(title="That's too much.",
								description="Please request only one module at once :sweat_smile:",
								color=discord.Color.orange())

		else:
			emb = discord.Embed(title="It's a magical place.",
								description="I don't know how you got here. But I didn't see this coming at all.\n"
											"Would you please be so kind to report that issue to me on github?\n"
											"https://github.com/nonchris/discord-fury/issues\n"
											"Thank you! ~Chris",
								color=discord.Color.red())
		await send_embed(ctx, emb)

	@commands.command(help="Checks the bot's ping on the server")
	async def ping(self, ctx):
		start_time = time.time()
		msg = await ctx.send("Pong 🏓!")
		end_time = time.time()
		await msg.edit(content=f"Pong 🏓! {round((end_time - start_time) * 1000)}ms")

async def setup(bot):
	await bot.add_cog(Bot(bot))