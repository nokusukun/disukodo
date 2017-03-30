from base import LOADER
from base import ROLES
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


	@on.cmdhelp("sum")
	def hlp_sum():
		return """
		**sum** [num1] [num2] [numn...]
		Prints back the sum of all numbers"""

	@on.command("sum", no_error=True)
	async def getSum(event, client):
		await client.send_message(event.message.channel, sum([int(x) for x in event.args[1:]]))

	@on.message("log")
	async def printLog(event, client):
		print("(LOG)[{0}@{1}]{2}:\t{3}".format(event.server, 
										event.message.channel, 
										event.user.name,
										event.message.content))

	@on.ready("print-ready")
	async def onready(event, client):
		print("Im ready!")

	@on.memberjoin("welcome")
	async def welcome(event, client):
		await client.send_message("Welcome {0}!".format(event.member.name))

	@on.typing("showtype")
	async def type_test(event, client):
		print("{0} last seen {1}".format(event.user.name, event.timestamp))