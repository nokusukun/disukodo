import discord
import settings

def err_invalid(string, client):
    print("MAKE: ERROR client")
    em = discord.Embed(title="Invalid Command", description=string)
    em.set_author(name=settings.BOT_NAME, icon_url=client.user.avatar_url)
    return em