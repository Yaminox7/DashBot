import discord

button = discord.ui.Button

import discord
from discord.ui import Button, View
from discord.ext import commands
import json
import os

def get_prefix(bot, message): 
  with open("prefix.json", "r") as f:
    prefixes = json.load(f)

  return commands.when_mentioned_or(prefixes[str(message.guild.id)])(bot, message)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
number = 0
num = 0
n = 0

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Game("Connecté"))
  await bot.get_channel(895040359896338455).send("Connecté")

@bot.command(pass_context=True)
async def prefix(ctx):
  await ctx.message.delete()

@bot.command(pass_context=True)
async def kick(ctx, reason=None):
  global num
  reason = reason if reason is not None else "Aucune raison n'a été donnée."
  num = 0
  not_banned_users = ctx.message.channel.guild.members
  await ctx.message.delete()
  not_banned_ones = []
  for members in not_banned_users:
    user = members
    not_banned_ones.append(user)
  button1 = Button(label="Précédant", style=discord.ButtonStyle.primary)
  button2 = Button(label="Expulser", style=discord.ButtonStyle.danger)
  button3 = Button(label="Suivant", style=discord.ButtonStyle.primary)
  view = View()
  view.add_item(button1)
  view.add_item(button2)
  view.add_item(button3)
  exit_button1 = Button(label="Expulsé", style=discord.ButtonStyle.success, disabled=True)
  exit_button2 = Button(label="Supprimer message", style=discord.ButtonStyle.danger)
  view2 = View()
  view2.add_item(exit_button1)
  view2.add_item(exit_button2)
  def embed():
    member = not_banned_ones[num]
    embed = discord.Embed(colour=discord.Colour.random(), timestamp=ctx.message.created_at)
    embed.set_author(name=f"Info de {member}")
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.avatar.url)
    embed.add_field(name="Pseudo:", value=f"```{member.name}```", inline=True)
    embed.add_field(name="Tag:", value=f"```{member.discriminator}```")
    embed.add_field(name="Id:", value=f"```{member.id}```")
    embed.add_field(name="Raison de l'expulsement:", value=f'*```{reason}```*')
    return embed

  await ctx.send(embed=embed(), view=view)

  async def callback1(interaction):
    global num
    if num < 1:
      num = len(not_banned_ones) - 1
    else:
      num -= 1
    await interaction.response.edit_message(embed=embed())
  async def callback2(interaction):
    user = not_banned_ones[num]
    await user.kick(reason=reason)
    await interaction.response.edit_message(embed=embed(), view=view2)
  async def callback3(interaction):
    global num
    if num == len(not_banned_ones)-1:
      num = 0
    else:
      num += 1
    await interaction.response.edit_message(embed=embed())
  async def exit_callback(interaction):
    await interaction.message.delete()

  button1.callback = callback1
  button2.callback = callback2
  button3.callback = callback3
  exit_button2.callback = exit_callback

@bot.command(pass_context=True)
async def ban(ctx, reason=None):
  global num
  reason = reason if reason is not None else "Aucune raison n'a été donnée."
  num = 0
  not_banned_users = ctx.message.channel.guild.members
  await ctx.message.delete()
  not_banned_ones = []
  for members in not_banned_users:
    user = members
    not_banned_ones.append(user)
  button1 = Button(label="Précédant", style=discord.ButtonStyle.primary)
  button2 = Button(label="Bannir", style=discord.ButtonStyle.danger)
  button3 = Button(label="Suivant", style=discord.ButtonStyle.primary)
  view = View()
  view.add_item(button1)
  view.add_item(button2)
  view.add_item(button3)
  exit_button1 = Button(label="Banni", style=discord.ButtonStyle.success, disabled=True)
  exit_button2 = Button(label="Supprimer message", style=discord.ButtonStyle.danger)
  view2 = View()
  view2.add_item(exit_button1)
  view2.add_item(exit_button2)
  def embed():
    member = not_banned_ones[num]
    embed = discord.Embed(colour=discord.Colour.random(), timestamp=ctx.message.created_at)
    embed.set_author(name=f"Info de {member}")
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.avatar.url)
    embed.add_field(name="Pseudo:", value=f"```{member.name}```", inline=True)
    embed.add_field(name="Tag:", value=f"```{member.discriminator}```")
    embed.add_field(name="Id:", value=f"```{member.id}```")
    embed.add_field(name="Raison du bannissement:", value=f'*```{reason}```*')
    return embed

  await ctx.send(embed=embed(), view=view)

  async def callback1(interaction):
    global num
    if num < 1:
      num = len(not_banned_ones) - 1
    else:
      num -= 1
    await interaction.response.edit_message(embed=embed())
  async def callback2(interaction):
    user = not_banned_ones[num]
    await user.ban(reason=reason)
    await interaction.response.edit_message(embed=embed(), view=view2)
  async def callback3(interaction):
    global num
    if num == len(not_banned_ones)-1:
      num = 0
    else:
      num += 1
    await interaction.response.edit_message(embed=embed())
  async def exit_callback(interaction):
    await interaction.message.delete()

  button1.callback = callback1
  button2.callback = callback2
  button3.callback = callback3
  exit_button2.callback = exit_callback

@bot.command(pass_context=True)
async def unban(ctx):
  await ctx.message.delete()
  global number
  number = 0
  banned_users = await ctx.guild.bans()
  banned_ones = []
  for ban_entry in banned_users:
    user = ban_entry
    banned_ones.append(user)
  if len(banned_ones) == 0:
    await ctx.send("Personne n'est banni sur ce serveur.")
  else: 
    button1 = Button(label="Précédant", style=discord.ButtonStyle.primary)
    button2 = Button(label="Débannir", style=discord.ButtonStyle.success)
    button3 = Button(label="Suivant", style=discord.ButtonStyle.primary)
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    exit_button1 = Button(label="Débanni", style=discord.ButtonStyle.success, disabled=True)
    exit_button2 = Button(label="Supprimer message", style=discord.ButtonStyle.danger)
    view2 = View()
    view2.add_item(exit_button1)
    view2.add_item(exit_button2)
    def embed():
      member = banned_ones[number]
      if member.reason == None:
        reason = "Aucune raison n'a été donnée."
      else:
        reason = member.reason
      embed = discord.Embed(colour=discord.Colour.random(), timestamp=ctx.message.created_at)
      embed.set_author(name=f"Info de {member.user}")
      embed.set_thumbnail(url=member.user.avatar.url)
      embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.avatar.url)
      embed.add_field(name="Pseudo:", value=f"```{member.user.name}```", inline=True)
      embed.add_field(name="Tag:", value=f"```{member.user.discriminator}```")
      embed.add_field(name="Id:", value=f"```{member.user.id}```")
      embed.add_field(name="Raison du bannissement:", value=f'*```{reason}```*')
      return embed

    await ctx.send(embed=embed(), view=view)

    async def callback1(interaction):
      global number
      if number < 1:
        number = len(banned_ones) - 1
      else:
        number -= 1
      await interaction.response.edit_message(embed=embed())
    async def callback2(interaction):
      user = banned_ones[number].user
      await ctx.guild.unban(user)
      await interaction.response.edit_message(embed=embed(), view=view2)
    async def callback3(interaction):
      global number
      if number == len(banned_ones)-1:
        number = 0
      else:
        number += 1
      await interaction.response.edit_message(embed=embed())
    async def exit_callback(interaction):
      await interaction.message.delete()
    button1.callback = callback1
    button2.callback = callback2
    button3.callback = callback3
    exit_button2.callback = exit_callback

@bot.command(pass_context=True)
async def say(ctx, message, times=1, delete=2.5):
  await ctx.message.delete()
  i = times if times <= 20 else 20
  while i >= 1:
    i -= 1
    if type(message) == str:
      await ctx.send(message, delete_after=delete)
    elif type(message) == discord.Member:
      await ctx.send(message.mention, delete_after=delete)

bot.run(os.getenv("DISCORD_TOKEN"))
