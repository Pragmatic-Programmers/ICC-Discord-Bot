import discord

from discord.ext import commands
from Tools.utils import get_prefix


class OnMessageCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_message(self, message):

        # Ignore messages from bots
        if message.author.bot:
            return
        

        # check for mention
        if self.bot.user.mentioned_in(message) and "<@!919509708577067028>" in message.content:
            mention_reply = discord.Embed(
                title="ICC",
                description=f"Hey 👋, list all commands using `{await get_prefix(self.bot, message)}help`",
                color=0x6b03fc
            )

            await message.channel.send(embed=mention_reply)


# Setup cog
def setup(bot):
    bot.add_cog(OnMessageCog(bot))