"""Informations - Commandes permettant d'obtenir des informations
/info rôle: Afficher les informations d'un rôle.
/info salon: Afficher les informations d'un salon.
/info serveur: Afficher les informations du serveur.
/info utilisateur: Afficher les informations d'un utilisateur.
/profil: Afficher le profil d'un utilisateur."""
import discord
from discord.ext import commands

class Informations(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.__doc__ = "Commands that lets you obtain informations"

	@commands.group(help="Gets the informations about a user, a channel, role and the server")
	async def info(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('You need to specify something to get its informations')

	@info.command(aliases=["member"])
	async def user(self, ctx, member: discord.Member=None):
		member = member if member else ctx.author
		await ctx.send(user.display_name)

async def setup(bot):
	await bot.add_cog(Informations(bot))