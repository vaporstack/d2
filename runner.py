from discord.client import Client


from duncan import Duncan

import asyncio
import json
import os
import sys

ddir = 'data'
if not os.path.exists(ddir):
	os.makedirs(ddir)

cfile = 'credentials.json'
if not os.path.exists(cfile):
	print("No credentials file.")
	sys.exit()

with open(cfile) as f:
	creds = json.loads(f.read())

key = creds['secret']



client = Client()

def greet(person):
	return "Hello, %s" % person

def grab(grabbee):
	return "Unfortunately .grab is not implemented yet. (workin on it)"


d = Duncan()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_member_join(member):
	server = member.server
	fmt = 'Welcome {0.mention} to {1.name}!'
	await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if not message.content.startswith('.'):
		return

	text = message.content[1:]
	ch = text.split()
	command = ch.pop(0)
	text = " ".join(ch)

	author = '{0.author.mention}'.format(message)
	channel = message.channel
	#commands = [greet, grab]
	cmds = d._list()

	if command not in cmds:
		await client.send_message(message.channel, '[%s] is not in my functions' % command)
	print(cmds)
	method_to_call = getattr(d, command)

	#if command == "list":
	#	await client.send_message(message.channel, d.list())

	await client.send_message(message.channel, 'DEBUG\nsender: %s | channel :%s | command: %s | text :%s' % ( author, channel, command, text))
	result = method_to_call(author=author, channel=channel, text=text)
	await client.send_message(channel, result)



	"""
	if message.content.startswith('.hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
		return

	if message.content.startswith('.test'):
		counter = 0
		tmp = await client.send_message(message.channel, 'Calculating messages...')
		async for log in client.logs_from(message.channel, limit=100):
			if log.author == message.author:
				counter += 1

		await client.edit_message(tmp, 'You have {} messages.'.format(counter))
	elif message.content.startswith('.sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')
	else:
		await client.send_message(message.channel, "i don't know that command")
	"""



def run_bot():


	try:
		client.run(key)
	except Exception as e:
		print(e)

	d.stop()

if __name__ == "__main__":
	run_bot()

