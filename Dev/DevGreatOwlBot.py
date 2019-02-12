#!/usr/bin/python3

import re
import discord
import requests

tokenfile = open('token','r')
TOKEN = tokenfile.readline().rstrip()

client = discord.Client()

lectureHalls = ['general','training-requests','ships-and-outfitting','combat','trading','mining','exploration']

@client.event
async def on_message(message):
    #Don't reply to yourself
    if message.author == client.user:
        return

    #Help response
    if message.content.startswith('!help'):
        em = discord.Embed(
            title='Great Owl Help',
            description="""Help Commands:
                        !help: Displays this help message
                        !rolehelp: Role command help
                        !shiphelp: Ship information help\n
                        Website Link Commands:
                        !coriolis: Coriolis website
                        !eddb: Elite Dangerous Database website
                        !edrefcard: EDRefCard website
                        !edsm: Elite Dangerous Star Map website
                        !inara: INARA website\n
                        Other Commands:
                        !vopals: Our stance on core mining
                        !materials: Spreadsheet for engineering materials and their locations""",
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
        )
        await client.send_message(message.channel, embed=em)

    #Coriolis response
    if message.content.startswith('!coriolis'):
        em = discord.Embed(
            title='Coriolis EDCD Edition',
            url='https://coriolis.io',
            description='A ship builder, outfitting and comparison tool for Elite Dangerous',
            color=0xff7700
        )
        em.add_field(
            name='Note', value='***Please use the s.orbis built-in short link when sharing builds! [Link icon on top right of coriolis page]***'
        )
        em.set_image(
            url='https://coriolis.io/mstile-144x144.png'
        )
        await client.send_message(message.channel, embed=em)

    #Fuel Rats response
    if message.content.startswith('!fuelrats'):
        em = discord.Embed(
            title='The Fuel Rats',
            url='https://fuelrats.com',
            description='The Fuel Rats are Elite: Dangerous\'s premier emergency refueling service. Fueling the galaxy, one ship at a time, since 3301.',
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/XHCgDTo.png'
        )
        await client.send_message(message.channel, embed=em)

    #INARA response
    if message.content.startswith('!inara'):
        em = discord.Embed(
            title='INARA - Elite:Dangerous companion',
            url='https://inara.cz',
            description='The companion site for Elite:Dangerous. Market data, CMDR\'s logs, logbooks, wings, galleries, powerplay, engineers, crafting, galaxy info, news and more...',
            color=0xff7700
        )
        em.set_image(
            url='https://inara.cz/mstile-144x144.png'
        )
        await client.send_message(message.channel, embed=em)

    #EDDB response
    if message.content.startswith('!eddb'):
        em = discord.Embed(
            title='Elite: Dangerous Database - EDDB',
            url='https://eddb.io',
            description='A site about systems, bodies, stations, commodities, materials and trade routes in Elite: Dangerous.',
            color=0xff7700
        )
        em.set_image(
            url='https://eddb.io/mstile-144x144.png'
        )
        await client.send_message(message.channel, embed=em)

    #EDRefCard response
    if message.content.startswith('!edrefcard'):
        em = discord.Embed(
            title='EDRefCard',
            url='https://edrefcard.info',
            description='Create and optionally publish a graphical reference card for your Elite: Dangerous keyboard and controller bindings.',
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/qO578Mn.jpg'
        )
        await client.send_message(message.channel, embed=em)

    #EDSM response
    if message.content.startswith('!edsm'):
        em = discord.Embed(
            title='EDSM - Elite Dangerous Star Map',
            url='https://edsm.net',
            description='The Galactic Positioning System of Elite: Dangerous at your service.',
            color=0xff7700
        )
        em.set_image(
            url='https://www.edsm.net/img/favicons/mstile-144x144.png'
        ) 
        await client.send_message(message.channel, embed=em)

    #Role help response
    if message.content.startswith('!rolehelp'):
        em = discord.Embed(
            title='Great Owl Role Help',
            description="""!pc: Add yourself to the PC role
                        !xb1: Add yourself to the Xbox 1 role
                        !ps4: Add yourself to the PS4 role\n
                        If you run a command while already assigned to its role, you will be asked if you wish to be removed from the role.""",
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
        )
        await client.send_message(message.channel, embed=em)

    #Role Assignment PC
    if message.content.startswith('!pc'):
        role = discord.utils.get(message.server.roles, name='PC')
        if discord.utils.get(message.author.roles, name='PC'):
            msg = 'You already have the PC role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content.lower() == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the PC role.')
            elif reply.content.lower() == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content != None:
                await client.send_message(message.channel, 'Unrecognized response. Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the PC role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)

    #Role Assignment XB1
    if message.content.startswith('!xb1'):
        role = discord.utils.get(message.server.roles, name='XBOX 1')
        if discord.utils.get(message.author.roles, name='XBOX 1'):
            msg = 'You already have the Xbox 1 role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content.lower() == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the Xbox 1 role.')
            elif reply.content.lower() == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content != None:
                await client.send_message(message.channel, 'Unrecognized response. Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the Xbox 1 role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)

    #Role Assignment PS4
    if message.content.startswith('!ps4'):
        role = discord.utils.get(message.server.roles, name='PS4')
        if discord.utils.get(message.author.roles, name='PS4'):
            msg = 'You already have the PS4 role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content.lower() == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the PS4 role.')
            elif reply.content.lower() == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content != None:
                await client.send_message(message.channel, 'Unrecognized response. Your roles have not been modified, CMDR')
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
                'action': (None, 'shorturl'),
                'url': (None, url),
                'format': (None, 'json')
            },
            headers = {
                'referer': url,
                'origin': 'https://coriolis.io'
            }
        )
        response = r.json()
        await client.send_message(message.channel, "I've edited your message, {0.author.mention}:\n{1}".format(message, msg.replace(url, response['shorturl'])))
        await client.delete_message(message)

    #Vopals response
    if message.content.startswith('!vopals'):
        em = discord.Embed(
            title='Void Opal Mining',
            description='The Tower of Knowledge doesn\'t prohibit the discussion or practice of lucrative deep-core mining. However, it shouldn\'t come off as the absolute one-and-only way of making Credits ingame. We value enjoyment over Credits at any and all costs.'
                        ' Always let others find what they enjoy the most.',
            color=0xff7700,
        )
        em.set_image(
             url='http://remlok-industries.fr/wp-content/uploads/2017/10/ED-FX17-Mining.jpg'
        )

        await client.send_message(message.channel, embed=em)

    #Engineering materials
    if message.content.startswith('!materials'):
        em = discord.Embed(
             title='Engineering Materials Spreadsheet',
             url='https://docs.google.com/spreadsheets/d/1Mp7l0bSnMp_G7xWUm75M-XuihDfTdi27rm-vB9K8AX0/edit?usp=sharing',
             description='A spreadsheet containing all materials required for engineering and how/where to get them.',
             color=0xff7700,
        )
        em.set_image(
             url='https://yt3.ggpht.com/a-/AAuE7mDaBvvb0xSIVhahkb9hnhQwqOnjmYE50OPxew=s288-mo-c-c0xffffffff-rj-k-no'
        )

        await client.send_message(message.channel, embed=em)

    #Ship help response
    if message.content.startswith('!shiphelp'):
        em = discord.Embed(
            title='Great Owl Ship Help',
            description="""Information pertaining to each ship listed:
                        !sidewinder: Sidewinder
                        !eagle: Eagle
                        !hauler: Hauler
                        !adder: Adder
                        !ieagle: Imperial Eagle
                        !viper3: Viper Mk.III
                        !cobra3: Cobra Mk.III""",
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
        )
        await client.send_message(message.channel, embed=em)

    #Sidewinder card
    if message.content.startswith('!sidewinder'):
        em = discord.Embed(
             title='**Ship Overview - Sidewinder Mk. I**',
             description="""The beginner\'s ship that\'s not good at anything in particular. 
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `32 000 Cr`
                            Hardpoints: `2x Small`
                            Top Speed: `220 m/s`
                            Boost Speed: `321 m/s`
                            Agility: `160`
                            Cargo Capacity: `4T`
                            Unladen Jump Range: `7,56 Ly`
                            ```Its primary use should be for data delivery missions and occasionally combat. Upgrade to higher tier ships is highly recommended.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/JB8bIGL.png'
        )
        await client.send_message(message.channel, embed=em)

    #Eagle card
    if message.content.startswith('!eagle'):
        em = discord.Embed(
             title='**Ship Overview - Eagle Mk. II**',
             description="""The cheapest combat focused ship, fast and packing a little bit of a punch. Doesn\'t stay alive for long.
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `44 800 Cr`
                            Hardpoints: `3x Small`
                            Top Speed: `240 m/s`
                            Boost Speed: `350 m/s`
                            Agility: `178`
                            Cargo Capacity: `2T`
                            Unladen Jump Range: `8,47 Ly`
                            ```Made for combat, and terrible at everything else. Bounty hunting is an option as well as assassination missions.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/6vIyepf.png'
        )
        await client.send_message(message.channel, embed=em)
        
    #Hauler card
    if message.content.startswith('!hauler'):
        em = discord.Embed(
             title='**Ship Overview - Hauler**',
             description="""The first step for aspiring traders. Surprisingly better at exploring rather than trading.
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `52 720 Cr`
                            Hardpoints: `1x Small`
                            Top Speed: `200 m/s`
                            Boost Speed: `305 m/s`
                            Agility: `144`
                            Cargo Capacity: `8T`
                            Unladen Jump Range: `9,87 Ly`
                            ```Decent at trading with the maximum of 22T carried at a time. Combat is not an option, but it can be quite useful for exploration.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/NfNL45G.png'
        )
        await client.send_message(message.channel, embed=em)
        
    #Adder card
    if message.content.startswith('!adder'):
        em = discord.Embed(
             title='**Ship Overview - Adder**',
             description="""The first multipurpose ship and the cheapest option for Multi-Crew.
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `87 808 Cr`
                            Hardpoints: `2x Small, 1x Medium`
                            Top Speed: `220 m/s`
                            Boost Speed: `320 m/s`
                            Agility: `144`
                            Cargo Capacity: `6T`
                            Unladen Jump Range: `9,12 Ly`
                            ```A direct upgrade of the Hauler, it does everything better. It can even go into combat and defend itself, as well as being the cheapest viable exploration vessel.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/REfDYLB.png'
        )
        await client.send_message(message.channel, embed=em)
        
    #IEagle card
    if message.content.startswith('!ieagle'):
        em = discord.Embed(
            title='**Ship Overview - Imperial Eagle**',
            description="""An improved Eagle with better firepower.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `110 825 Cr`
                           Hardpoints: `2x Small, 1x Medium`
                           Top Speed: `302 m/s`
                           Boost Speed: `403 m/s`
                           Agility: `145`
                           Cargo Capacity: `2T`
                           Unladen Jump Range: `8,22 Ly`
                           ```Featuring better firepower and speed than the Eagle, at the cost of a trip to Imperial space and earning a rank. Trading and exploring are not an option.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/0ETb9mN.png'
        )
        await client.send_message(message.channel, embed=em)

    #Viper3 card
    if message.content.startswith('!viper3'):
        em = discord.Embed(
            title='**Ship Overview - Viper Mk. III**',
            description="""A combat oriented vessel with small bits of versatility. 
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `142 931 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `310 m/s`
                           Boost Speed: `388 m/s`
                           Agility: `135`
                           Cargo Capacity: `4T`
                           Unladen Jump Range: `6,92 Ly`
                           ```While not as agile as the Eagles, the Viper Mk. III is tankier and can take on tougher enemies. While non-combat activities aren\'t optimal, they are still a possibility.```""",
            color=0xff7700,
        )
        em.set_image(
             url='https://imgur.com/0vPA1tS.png'
        )
        await client.send_message(message.channel, embed=em)

    #Cobra3 card
    if message.content.startswith('!cobra3'):
        em = discord.Embed(
            title='**Ship Overview - Cobra Mk. III**',
            description="""A multipurpose ship that won\'t hold you back, also with Multi-Crew.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `379 718 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `282 m/s`
                           Boost Speed: `402 m/s`
                           Agility: `140`
                           Cargo Capacity: `18T`
                           Unladen Jump Range: `10,46 Ly`
                           ```The ship is great for combat, trading, exploring, and even mining.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/1OODhnZ.png'
        )
        await client.send_message(message.channel, embed=em)

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
        color=0xff7700
    )
    await client.send_message(joinchan, embed=em)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
