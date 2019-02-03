#!/usr/bin/python3

import re
import discord
import requests

TOKEN = ''

client = discord.Client()

lectureHalls = ['general','training-requests','ships-and-outfitting','combat','trading','mining','exploration']

@client.event
async def on_message(message):
    #Don't reply to yourself
    if message.author == client.user:
        return

    #Help response
    if message.content.startswith('go!help'):
        em = discord.Embed(
            title='Great Owl Help',
            description='Help Commands:\ngo!help: Displays this help message\ngo!rolehelp: Displays role command help\n\nWebsite Link Commands:\ngo!coriolis: Coriolis website\ngo!eddb: Elite Dangerous Database website\ngo!edrefcard: EDRefCard website\ngo!edsm: Elite Dangerous Star Map website\ngo!inara: INARA website',
            color=0x00fcff
            )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
            )
        await client.send_message(message.channel, embed=em)

    #Coriolis response
    if message.content.startswith('go!coriolis'):
        em = discord.Embed(
            title='Coriolis EDCD Edition',
            url='https://coriolis.io',
            description='A ship builder, outfitting and comparison tool for Elite Dangerous',
            color=0x00fcff
            )
        em.add_field(
            name='Note', value='***Please use the s.orbis built-in short link when sharing builds! [Link icon on top right of coriolis page]***'
            )
        em.set_image(
            url='https://coriolis.io/mstile-144x144.png'
            )
        await client.send_message(message.channel, embed=em)

    #Fuel Rats response
    if message.content.startswith('go!fuelrats'):
        em = discord.Embed(
            title='The Fuel Rats',
            url='https://fuelrats.com',
            description='The Fuel Rats are Elite: Dangerous\'s premier emergency refueling service. Fueling the galaxy, one ship at a time, since 3301.',
            color=0x00fcff
            )
        em.set_image(
            url='https://i.imgur.com/XHCgDTo.png'
            )
        await client.send_message(message.channel, embed=em)

    #INARA response
    if message.content.startswith('go!inara'):
        em = discord.Embed(
            title='INARA - Elite:Dangerous companion',
            url='https://inara.cz',
            description='The companion site for Elite:Dangerous. Market data, CMDR\'s logs, logbooks, wings, galleries, powerplay, engineers, crafting, galaxy info, news and more...',
            color=0x00fcff
            )
        em.set_image(
            url='https://inara.cz/mstile-144x144.png'
            )
        await client.send_message(message.channel, embed=em)

    #EDDB response
    if message.content.startswith('go!eddb'):
        em = discord.Embed(
            title='Elite: Dangerous Database - EDDB',
            url='https://eddb.io',
            description='A site about systems, bodies, stations, commodities, materials and trade routes in Elite: Dangerous.',
            color=0x00fcff
            )
        em.set_image(
            url='https://eddb.io/mstile-144x144.png'
            )
        await client.send_message(message.channel, embed=em)

    #EDRefCard response
    if message.content.startswith('go!edrefcard'):
        em = discord.Embed(
            title='EDRefCard',
            url='https://edrefcard.info',
            description='Create and optionally publish a graphical reference card for your Elite: Dangerous keyboard and controller bindings.',
            color=0x00fcff
            )
        em.set_image(
            url='https://i.imgur.com/qO578Mn.jpg'
            )
        await client.send_message(message.channel, embed=em)

    #EDSM response
    if message.content.startswith('go!edsm'):
        em = discord.Embed(
            title='EDSM - Elite Dangerous Star Map',
            url='https://edsm.net',
            description='The Galactic Positioning System of Elite: Dangerous at your service.',
            color=0x00fcff
            )
        em.set_image(
            url='https://www.edsm.net/img/favicons/mstile-144x144.png'
            ) 
        await client.send_message(message.channel, embed=em)

    #Role help response
    if message.content.startswith('go!rolehelp'):
        em = discord.Embed(
            title='Great Owl Role Help',
            description='go!pc: Add yourself to the PC role\ngo!xb1: Add yourself to the Xbox 1 role\ngo!ps4: Add yourself to the PS4 role\n\nIf you run a command while already assigned to its role, you will be asked if you wish to be removed from the role.',
            color=0x00fcff
            )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
            )
        await client.send_message(message.channel, embed=em)

    #Role Assignment PC
    if message.content.startswith('go!pc'):
        role = discord.utils.get(message.server.roles, name='PC')
        if discord.utils.get(message.author.roles, name='PC'):
            msg = 'You already have the PC role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the PC role.')
            elif reply.content == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the PC role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)

    #Role Assignment XB1
    if message.content.startswith('go!xb1'):
        role = discord.utils.get(message.server.roles, name='XBOX 1')
        if discord.utils.get(message.author.roles, name='XBOX 1'):
            msg = 'You already have the Xbox 1 role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the Xbox 1 role.')
            elif reply.content == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the Xbox 1 role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)

    #Role Assignment PS4
    if message.content.startswith('go!ps4'):
        role = discord.utils.get(message.server.roles, name='PS4')
        if discord.utils.get(message.author.roles, name='PS4'):
            msg = 'You already have the PS4 role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the PS4 role.')
            elif reply.content == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the PS4 role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)

    #Coriolis autoshortener
    if all(chunk in message.content for chunk in ('coriolis.io/outfit/', '?code=')):
        msg = message.content
        url = re.findall(r'(https?://\S+)', msg)[0]
        r = requests.post(
            'https://s.orbis.zone/api.php',
            files = {
                'action': (None, 'shorturl'), 'url': (None, url), 'format': (None, 'json')
            },
            headers = {
                'referer': url,
                'origin': 'https://coriolis.io'
            }
        )
        response = r.json()
        await client.send_message(message.channel, "I've edited your message, {0.author.mention}:\n{1}".format(message, msg.replace(url, response['shorturl'])))
        await client.delete_message(message)

#Welcome new users
@client.event
async def on_member_join(member):
    joinchan = discord.utils.get(member.server.channels, name='cmdr-lounge', type=discord.ChannelType.text)
    chanlist = ''
    for server in client.servers:
        if member.server == server:
            for channel in server.channels:
                if str(channel) in lectureHalls:
                    chanlist += channel.mention + '\n'
    em = discord.Embed(
        title='',
        description='Welcome, CMDR {0.mention}.\nIf you have any questions, use one of these Lecture Halls:\n{1}\nIf, however, you want to become a guide, please mention an Overseer or Admin in this channel to start the process. Enjoy your stay and fly safe CMDR, o7'.format(member,chanlist),
        color=0x00fcff
        )
    await client.send_message(joinchan, embed=em)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
