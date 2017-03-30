from base import ROLES

# Command Prefix
PREFIX = "~"

# Discord Bot Token
BOT_TOKEN = ""

# Bot Nickname, can be overriden through the client.
# Reverts upon bot restart
NICKNAME = ""

#Bot name, should be something similar to the bot's real name
BOT_NAME = "Oprah Winfrey"

# USER ID of the server owner, fallback in case the adminstrator roles are unavailable
OWNER = ""

# User roles (Case sensitive)
ROLE = {
	ROLES.ADMIN:	["Administrator", "Admin", "Owner"],
	ROLES.MOD:		["Moderator", "Mod"],
	ROLES.SPECIAL:	["Cinnamon Bun"],
	ROLES.EVERYONE:	["@everyone"]}
