"""Fun - Commandes amusantes
/anniversaire activer: Activer votre anniversaire sur le serveur.
/anniversaire définir: Définir votre date d'anniversaire (lié à tous vos serveurs).
/anniversaire désactiver: Désactiver votre anniversaire sur le serveur.
/anniversaire liste: Voir les prochains anniversaires à venir.
/anniversaire retirer: Supprimer votre date d'anniversaire (lié à tous vos serveurs).
/blague: Demander une blague.
/concours créer: Créer et lancer un giveaway sur le serveur.
/concours relancer: Désigner un nouveau gagnant pour un giveaway.
/concours terminer: Lancer la fin d'un giveaway.
/couple: Trouver le couple parfait.
/lancer-dés: Lanceur de dés (notation de dés).
/sondage créer: Créer et lancer un sondage.
/sondage résultats: Voir les résultats d'un sondage.
/sondage terminer: Mettre fin à un sondage."""
import discord
from discord.ext import commands
import discord.ui
from discord.ui import Button, View
import random
import time

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.__doc__ = "Fun commands"

	@commands.command(name="8ball", help="Asks the mighty 8ball a question")
	async def _8ball(self, ctx, *, question):
		responses = ["Yes", "No", "Maybe", "Maybe not", "Probably", "Probably not", "Can you repeat it ?", 
			"I don't understand", "Don't do it", "Do it"]
		embed = discord.Embed(help=f"**Question:** {question}\n**Answer:** {random.choice(responses)}")
		await ctx.send(embed=embed) 

	@commands.command(help="Flips a coin")
	async def coinflip(self, ctx):
		results = ["tails", "heads"]
		await ctx.send(f"The coin is showing... its {random.choice(results)} 🪙 !") 

	@commands.command(help="Rolls a die")
	async def diceroll(self, ctx):
		numbers = {1: "one ⚀", 2: "two ⚁", 3: "three ⚂", 4: "four ⚃", 5: "five ⚄", 6: "six ⚅"}
		await ctx.send(f"The dice rolled... a {numbers[random.choice(range(6))+1]} !") 

	async def get_result_of_usr_choice(self, interaction, usrchoice, opt):
		await interaction.message.delete()
		bchoice = random.choice(["📄", "🪨", "✂️"])
		string = ""
		if opt[bchoice] == opt[usrchoice]:
			string = "Draw"
		elif opt[bchoice] > opt[usrchoice]:
			string = "Bot Won"
		elif opt[bchoice] < opt[usrchoice]:
			string = "You Won"
		embed = discord.Embed(help=f"**Bot chose**: {bchoice}\n**You chose**: {usrchoice}\n**Result**: {string}")
		await interaction.channel.send(embed=embed)

	async def paper_chosen(self, interaction):
		opt = {"📄": 0, "🪨": -1, "✂️": 1}
		await self.get_result_of_usr_choice(interaction, "📄", opt)

	async def rock_chosen(self, interaction):
		opt = {"📄": 1, "🪨": 0, "✂️": -1}
		await self.get_result_of_usr_choice(interaction, "🪨", opt)

	async def scissors_chosen(self, interaction):
		opt = {"📄": -1, "🪨": 1, "✂️": 0}
		await self.get_result_of_usr_choice(interaction, "✂️", opt)

	@commands.command(help="Plays a rock paper scissors game with the bot")
	async def rps(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Choose one from the following options: ", help="**Paper**, symbol: 📄\n**Rock**, symbol: 🪨\n**Scissors**, symbol: ✂️")
		btn1 = Button(emoji="📄", style=discord.ButtonStyle.secondary)
		btn1.callback = self.paper_chosen	
		btn2 = Button(emoji="🪨", style=discord.ButtonStyle.secondary)
		btn2.callback = self.rock_chosen
		btn3 = Button(emoji="✂️", style=discord.ButtonStyle.secondary)
		btn3.callback = self.scissors_chosen
		view = View(timeout=None)
		view.add_item(btn1)
		view.add_item(btn2)
		view.add_item(btn3)
		await ctx.send(embed=embed, view=view)

async def setup(bot):
	await bot.add_cog(Fun(bot))