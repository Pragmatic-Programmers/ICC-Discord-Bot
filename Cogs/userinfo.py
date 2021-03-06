import discord

from discord.ext import commands


class UserInfo(commands.Cog):
    """Get info about a member in the server."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo", usage="@member")
    @commands.guild_only()
    async def userinfo(self, ctx, *, user=""):
        """
        Get user-info.
        """

        if user:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                # user is not mentioned
                pass
        else:
            user = ctx.message.author

        top_role = user.top_role

        userinfo_embed = discord.Embed(
            title=f"**UserInfo:** {user.name}",
            timestamp=ctx.message.created_at,
            color=0x0ceded
        )
        if user.nick:
            userinfo_embed.add_field(name="Nick", value=user.nick, inline=True)

        if top_role.name != "@everyone":
            userinfo_embed.add_field(name="Highest Role",
                                     value=top_role.mention,
                                     inline=True
                                     )
        else:
            userinfo_embed.add_field(
                name="Highest Role", value="N/A", inline=True)

        if str(user.status) == 'offline':
            status = '💤 Offline'
        elif str(user.status) == 'dnd':
            status = '⛔ DND'
        else:
            status = '🟢 Online'
        userinfo_embed.add_field(name="Status", value=status, inline=True)

        if user.activities:
            userinfo_embed.add_field(
                name="Activity", value=user.activities[0].name, inline=True)
        else:
            userinfo_embed.add_field(
                name="Activity", value="None", inline=True)
        userinfo_embed.add_field(name="Account Created",
                                 value=user.created_at.__format__(
                                     '%A, %d. %B %Y @ %H:%M:%S'))
        userinfo_embed.add_field(
            name="Joined At",
            value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        userinfo_embed.set_thumbnail(url=user.avatar_url)

        additional_info = ""
        if user.id == ctx.guild.owner.id:
            additional_info += f"👑 Server owner of **{ctx.guild.name}**\n"
        elif user.guild_permissions.administrator:
            additional_info += f"🤴 Admin of **{ctx.guild.name}**\n"

        with open("contributors-discord.txt", 'r') as file:
            print(type(user.id))
            contributors = file.readlines()

        if str(user.id) in contributors:
            additional_info += "😎 Developer of **ICC Discord Bot**"

        if additional_info != "":
            userinfo_embed.add_field(
                name="Additional info", value=additional_info)

        await ctx.channel.send(embed=userinfo_embed)


# Setup
def setup(bot):
    bot.add_cog(UserInfo(bot))
