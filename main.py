import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from pretty_help import PrettyHelp
from rich.console import Console

load_dotenv()
console = Console()

TOKEN = os.getenv("TOKEN")


# discord intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True


bot = commands.Bot(
    command_prefix='$',
    intents=intents,
    case_insensitivity=True,
    strip_after_prefix=True,
    help_command=PrettyHelp()
)


@bot.event
async def on_ready():
    console.clear()
    console.log(f"{bot.user} is active now!")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=bot.command_prefix
        )
    )


# Running the bot
bot.run(TOKEN)
