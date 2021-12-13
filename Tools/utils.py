import json


def get_config(guildId, ctx=None):
    """Return config of requested guild"""

    with open("config.json", "r") as file:
        data = json.load(file)

    if str(guildId) not in data["guilds"]:
        # create new config if guild-config doesn't exits
        default_config = {
            "name": f"{ctx.guild.name}",
            "prefix": "$",
        }
        update_config(guildId, default_config)
        return default_config
    else:
        return data["guilds"][str(guildId)]


def update_config(guildId, data):
    with open("config.json", "r") as file:
        config = json.load(file)

    config["guilds"][str(guildId)] = data
    updated_data = json.dumps(config, indent=4)

    with open("config.json", "w") as file:
        file.write(updated_data)


async def get_prefix(bot, message):
    if not message.guild:
        return "$"
    else:
        data = get_config(message.guild.id, ctx=message)
        return data["prefix"]
