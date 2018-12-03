from discord.client import Client
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

dfile = "data/data.json"
data = {}
if os.path.exists(dfile):
	with open(dfile) as f:
		data = json.loads(f.read())
else:
	data = {}

client = Client()

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


try:
	client.run(key)
except Exception as e:
	print(e)

with open(dfile, 'w') as f:
	f.write(json.dumps(data))
#bot.run('NTE5MjE2NTE2NDIwMzM3Njkx.DucGSw.ojlBBQDSNHXeF7x8m4wX4EasaI0')

