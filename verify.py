import discord
import sheets_api

SPREADSHEET_ID = '1kLzaCOz2lbXxAZTE5e9RbtE-FucRu0Hg9KcehRBfQaY'

async def run(message):

    verifiedRole = None

    for role in message.guild.roles:
        if role.name == 'Verified':
            verifiedRole = role
            break
    else:
        verifiedRole = await message.guild.create_role(name='Verified', color=discord.Colour.purple)
    
    verifiedUsers = sheets_api.get_values(SPREADSHEET_ID,'E2:E').get('values')

    username = message.author.name
    if message.author.discriminator is not 0:
        username = message.author.name + "#" + message.author.discriminator

    if [username] in verifiedUsers:
        print(message.author.display_name + ' has been verified!')
        row = verifiedUsers.index([username]) + 2
        userInfo = sheets_api.get_values(SPREADSHEET_ID, str(row) +':'+ str(row)).get('values')[0]
        print('Member information:')
        print(userInfo)
        roles = message.author.roles
        roles.append(verifiedRole)
        await message.author.edit(nick=get_name(userInfo[2], userInfo[3]), roles=roles)
    else:
        print(message.author.display_name + " was not verified.")
        await message.channel.send('You did not fill out the form or entered the wrong username')


def get_name(full_name, perferred_name):
    full_name = full_name.strip()
    perferred_name = perferred_name.strip()
    full_split = full_name.split(' ')
    if perferred_name == '':
        return full_split[0] + ' ' + full_split[len(full_split) - 1][0:1] + '.'
    else:
        perferred_split = perferred_name.split(' ')
        if len(perferred_split) > 1:
            return perferred_split[0] + ' ' + perferred_split[len(full_split) - 1][0:1] + '.'
        else:
            return perferred_split[0] + ' ' + full_split[len(full_split) - 1][0:1] + '.'