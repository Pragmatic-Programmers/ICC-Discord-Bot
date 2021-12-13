import os
import logging
import discord

from dotenv import load_dotenv
from discord.ext import commands
from pretty_help import PrettyHelp
from rich.logging import RichHandler

from Tools.utils import get_prefix

# Setting up logging
FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")


# discord intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True


bot = commands.Bot(
    command_prefix=get_prefix,
    intents=intents,
    case_insensitivity=True,
    strip_after_prefix=True,
    help_command=PrettyHelp()
)


# Loading Cogs
for cog in os.listdir("Cogs"):
    if cog.startswith("__pycache__"):
        # ignore __pycache__ folder
        log.info("Skipping __pycache__ folder")
    else:
        try:
            bot.load_extension(f"Cogs.{cog[:-3]}")
            log.info(f"Loaded {cog[:-3]} ✅")
        except Exception as e:
            log.fatal(f"Failed to load {cog[:-3]}, error: {e}")


@bot.event
async def on_ready():
    log.info(f"{bot.user} is active now!")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=bot.command_prefix
        )
    )


# Running the bot
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
