import discord
from discord.ext import commands
from discord import utils
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType
from config import settings, roles
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
DiscordComponents(bot)


# Bot connection
@bot.event
async def on_ready():
    print("--Bot is ready--")


# New member greeting
@bot.event
async def on_member_join(member):
    await member.guild.text_channels[1].\
        send(f" \U0001F44B  **{member} joined Server, let's say him hello !**   \U0001F44B")
    await member.send("**Welcome to the club buddy ! \U0001F609\U0001F4A6\n My name is Giovani, Giovani "
                      "Giorgio\U0001F916, and I can help you (free of course) : type `/giovani` to see all "
                      "my commands.\n`If you have some troubles or anything else, send a message to admin.`**")


# bot commands
@bot.command()
async def giovani(ctx):
    if 'dota-requests' in ctx.channel.name:
        await ctx.channel.send("`/new_team TEAM_NAME POSITIONS` ~ create a new party\n"
                               "`/rdy_team TEAM_NAME` ~ disable searching players\n")


# add role
@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(923619030055669831)
    roles_channel = bot.get_channel(payload.channel_id)
    print(channel.name == roles_channel.name)
    if roles_channel.name == "roles":
        message = await channel.fetch_message(payload.message_id)
        member = utils.get(message.guild.members, id=payload.user_id)
        emoji = payload.emoji.name
        role = utils.get(message.guild.roles, id=roles[emoji])
        await member.add_roles(role)


# remove role
@bot.event
async def on_raw_reaction_remove(payload):
    channel = bot.get_channel(923619030055669831)
    roles_channel = bot.get_channel(payload.channel_id)
    print(channel.name == roles_channel.name)
    if roles_channel.name == "roles":
        message = await channel.fetch_message(payload.message_id)
        member = utils.get(message.guild.members, id=payload.user_id)
        emoji = payload.emoji.name
        role = utils.get(message.guild.roles, id=roles[emoji])
        await member.remove_roles(role)


# new_team command
@bot.command()
async def new_team(ctx, team_name, positions):
    await ctx.channel.send(f">>> **The team {team_name} is searching for new players on positions : {positions}**")

bot.run(settings['token'])


