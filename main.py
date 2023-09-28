import discord
import verify

COMMAND_CHAR = '>'
VALID_COMMANDS = ['verify']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(COMMAND_CHAR):
        index = message.content.find(' ') if (message.content.find(' ') != -1) else len(message.content)
        command = message.content[1:index]

        if command in VALID_COMMANDS:
            match command:
                case "verify":
                    print('Verifying ' + message.author.display_name + "!")
                    await verify.run(message)
        else:
            await message.channel.send("Unknown Command Sorry ;(")


f = open("token.txt")
token = f.readline()
client.run(token)