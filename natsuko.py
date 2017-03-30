import discord
import settings
from base.ModuleLoader import ModuleLoader
from base.Map import Map
import arrow

loader = ModuleLoader()
client = discord.Client()


@client.event
async def on_ready():
    event = None
    await loader.execute(   command=None,
                            cmdtype="Ready", 
                            event=event, 
                            client=client)

@client.event
async def on_message(message):

    event = Map({})
    event.message = message
    event.server = message.server
    event.user = message.author

    # Execute all of the on_message commands first
    await loader.execute(command=None, 
                            cmdtype="Message", 
                            event=event, 
                            client=client)

    # Checks if it actually is a command
    if not message.content.startswith(settings.PREFIX):
        return

    event.args = message.content[len(settings.PREFIX):].split(" ")
    command = message.content.split(" ")[0][len(settings.PREFIX):]
    # Execute any specific commands
    await loader.execute(command=command, 
                            cmdtype="Command", 
                            event=event, 
                            client=client)

@client.event
async def on_typing(channel, user, when):
    event = Map({})
    event.channel = channel
    event.user = user
    event.when = when
    event.arrow = arrow.get(str(when), "YYYY-MM-DD HH:mm:ss")
    event.timestamp = event.arrow.timestamp

    await loader.execute(command=None, 
                            cmdtype="Typing", 
                            event=event, 
                            client=client)

@client.event
async def on_message_delete(message):

    event = Map({})
    event.message = message
    event.user = message.author
    event.server = message.server

    await loader.execute(command=None, 
                            cmdtype="Delete", 
                            event=event, 
                            client=client)

@client.event
async def on_message_edit(pre, post):

    event = Map({})
    event.old = pre
    event.new = post
    event.message = post
    event.user = pre.author
    event.server = pre.server

    await loader.execute(command=None, 
                            cmdtype="Edit", 
                            event=event, 
                            client=client)

    if not post.content.startswith(settings.PREFIX):
        return

    event.args = post.content[len(settings.PREFIX):].split(" ")
    command = post.content.split(" ")[0][len(settings.PREFIX):]
    # Execute any specific commands
    await loader.execute(command=command, 
                            cmdtype="Command", 
                            event=event, 
                            client=client)



@client.event
async def on_reaction_add(reaction, user):

    event = Map({})
    event.reaction = reaction
    event.user = user
    event.server = user.server

    await loader.execute(command=None, 
                            cmdtype="ReactAdd", 
                            event=event, 
                            client=client)

@client.event
async def on_reaction_remove(reaction, user):

    event = Map({})
    event.reaction = reaction
    event.user = user
    event.server = user.server

    await loader.execute(command=None, 
                            cmdtype="ReactRemove", 
                            event=event, 
                            client=client)

@client.event
async def on_reaction_clear(reactions, message):

    event = Map({})
    event.reactions = reactions
    event.message = message
    event.server = message.server

    await loader.execute(command=None, 
                            cmdtype="ReactClear", 
                            event=event, 
                            client=client)

@client.event
async def on_channel_delete(channel):

    event = Map({})
    event.channel = channel
    event.server = channel.server

    await loader.execute(command=None, 
                            cmdtype="ChannelRemove", 
                            event=event, 
                            client=client)

@client.event
async def on_member_join(member):

    event = Map({})
    event.member = member

    await loader.execute(command=None, 
                            cmdtype="MemberJoin", 
                            event=event, 
                            client=client)

@client.event
async def on_member_remove(member):

    event = Map({})
    event.member = member
    event.server = member.server

    await loader.execute(command=None, 
                            cmdtype="MemberLeave", 
                            event=event, 
                            client=client)

@client.event
async def on_member_update(pre, post):

    event = Map({})
    event.old = pre
    event.new = post
    event.server = pre.server

    await loader.execute(command=None, 
                            cmdtype="MemberUpdate", 
                            event=event, 
                            client=client)

@client.event
async def on_member_ban(member):

    event = Map({})
    event.member = member
    event.server = member.server

    await loader.execute(command=None, 
                            cmdtype="MemberBan", 
                            event=event, 
                            client=client)

@client.event
async def on_member_unban(member):

    event = Map({})
    event.member = member
    event.server = member.server

    await loader.execute(command=None, 
                            cmdtype="MemberUnban", 
                            event=event, 
                            client=client)

@client.event
async def on_server_join(server):
    event = Map({})
    event.server = server
    
    await loader.execute(command=None, 
                            cmdtype="BotJoin", 
                            event=event, 
                            client=client)

@client.event
async def on_server_join(server):
    event = Map({})
    event.server = server
    
    await loader.execute(command=None, 
                            cmdtype="BotJoin", 
                            event=event, 
                            client=client)


@client.event
async def on_server_update(post, pre):
    event = Map({})
    event.old = post
    event.new = pre
    
    await loader.execute(command=None, 
                            cmdtype="ServerChange", 
                            event=event, 
                            client=client)

@client.event
async def on_server_available(server):
    event = Map({})
    event.server = server
    
    await loader.execute(command=None, 
                            cmdtype="ServerEnable", 
                            event=event, 
                            client=client)

@client.event
async def on_server_unavailable(server):
    event = Map({})
    event.server = server
    
    await loader.execute(command=None, 
                            cmdtype="ServerDisable", 
                            event=event, 
                            client=client)

@client.event
async def on_server_role_create(role):
    event = Map({})
    event.role = role
    event.server = role.server
    
    await loader.execute(command=None, 
                            cmdtype="RoleAdd", 
                            event=event, 
                            client=client)

@client.event
async def on_server_role_delete(role):
    event = Map({})
    event.role = role
    event.server = role.server

    await loader.execute(command=None, 
                            cmdtype="RoleRemove", 
                            event=event, 
                            client=client)

@client.event
async def on_server_emojis_update(post, pre):
    event = Map({})
    event.old = post
    event.new = pre
    event.server = post[0].server

    if len(old) < len(new):
        event.create = True
        # Sets emoji variable to the changed emoji
        event.emoji = [emoji for emoji in pre if emoji not in post][0]

    if len(old) > len(new):
        event.create = False
        # Sets emoji variable to the changed emoji
        event.emoji = [emoji for emoji in post if emoji not in pre][0]

    await loader.execute(command=None, 
                            cmdtype="EmojiUpdate", 
                            event=event, 
                            client=client)

@client.event
async def on_voice_state_update(pre, post):
    event = Map({})
    event.old = pre
    event.new = post
    event.server = pre.server

    await loader.execute(command=None, 
                            cmdtype="RoleRemove", 
                            event=event, 
                            client=client)

client.run(settings.BOT_TOKEN)
#296671912170618880