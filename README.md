# Disukodo - ディスコード

## Modular discord.py API framework
Modular framework for rapid bot development. The process revolves around decorators for setting configuration.

## Example
Sample Code
```
from base import LOADER, ROLES
on = LOADER.CommandLoader()

class Module():

	def __init__(self):
		self.loader = on
		self.scope = None

	@on.cmdhelp("echo")
	def hlp_echo():
		return """
		**echo** [text]
		Prints back the text"""

	@on.command("echo")
	async def echo(event, client):
		await client.send_message(event.message.channel, " ".join(event.args[1:]))


```

### Boilerplate
```
from base import LOADER, ROLES
on = LOADER.CommandLoader()

class Module():

	def __init__(self):
		self.loader = on
		self.scope = None
```
This is the skeleton for every module. It features the loader and the scope.

### Command Help
```
	@on.cmdhelp("echo")
	def hlp_echo():
		return """
		**echo** [text]
		Prints back the text"""
```
This code gets returned in case of a command error, usually in cases where the syntax is invalid.

### Command method
```
	@on.command("echo")
	async def echo(event, client):
		await client.send_message(event.message.channel, " ".join(event.args[1:]))
```
The code gets executed upon the detection of a `<prefix>echo` command with the command name defined in the decorator.

This code contains the actual command code, every event features two arguments, the `event` object and `client` object.

The `event` object is a Mapped dictionary containing event data.
Depending on what event, the `event` object can contain `event.user`, `event.server`, `event.timestamp`, etc.

_`event.server` is almost always present in all events_

## TODO

1. A fair ammount of the events has been completed and are working. Role restrictions are still being developed.

2. Persistent storage is also in the development roadmap so that the modules has a centralized configuration storage.