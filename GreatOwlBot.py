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
                        !cobra3: Cobra Mk.III
                        !viper4: Viper Mk.IV
                        !dbscout: Diamondback Scout
                        !cobra4: Cobra Mk.IV
                        !type6: Type-6 Transporter
                        !dolphin: Dolphin
                        !dbexplorer: Diamondback Explorer
                        !icourier: Imprerial Courier
                        !keelback: Keelback
                        !aspscout: Asp Scout
                        !vulture: Vulture
                        !aspx: Asp Explorer""",
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
        
    #Viper4 card
    if message.content.startswith('!viper4'):
        em = discord.Embed(
            title='**Ship Overview - Viper Mk. IV**',
            description="""Viper III\'s tougher and more versatile brother.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `437 930 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `271 m/s`
                           Boost Speed: `342 m/s`
                           Agility: `140`
                           Cargo Capacity: `18T`
                           Unladen Jump Range: `10,36 Ly`
                           ```Decent at everything, but best at combat. It can!t do exploration too well, though.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/Cai03ei.png'
        )        
        await client.send_message(message.channel, embed=em)

    #DBS card
    if message.content.startswith('!dbscout'):
        em = discord.Embed(
            title='**Ship Overview - Diamondback Scout**',
            description="""The first ship in the line of explorers.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `564 329 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `283 m/s`
                           Boost Speed: `384 m/s`
                           Agility: `150`
                           Cargo Capacity: `0T`
                           Unladen Jump Range: `11,35 Ly`
                           ```Surprisingly good at combat with excellent heat management, but even better as an early exploration ship.```""",
            color=0xff7700
        )
        em.set_image(
            url='https://imgur.com/xDzltVR.png'
        )
        await client.send_message(message.channel, embed=em)

    #Cobra4 card
    if message.content.startswith('!cobra4'):
        em = discord.Embed(
            title='**Ship Overview - Cobra Mk. IV **',
            description="""A pre-order exclusive multipurpose vessel.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `764 720 Cr`
                           Hardpoints: `3x Small, 2x Medium`
                           Top Speed: `200 m/s`
                           Boost Speed: `299 m/s`
                           Agility: `1525`
                           Cargo Capacity: `34T`
                           Unladen Jump Range: `9,37 Ly`
                           ```Trades mobility for durability when compared to Comba Mk. III, it is better in terms of internals and cargo capacity, but lacks in jump range.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/FrJDu7K.png'
        )
        await client.send_message(message.channel, embed=em)

    #Type6 card
    if message.content.startswith('!type6'):
        em = discord.Embed(
              title='**Ship Overview - Type-6 Transporter**',
              description="""The first dedicated freighter-type vessel.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `1 045 945 Cr`
                             Hardpoints: `2x Small`
                             Top Speed: `223 m/s`
                             Boost Speed: `355 m/s`
                             Agility: `140`
                             Cargo Capacity: `50T`
                             Unladen Jump Range: `12,39 Ly`
                             ```One of the worst ships for combat purposes. On the other hand it excels in trading with the capacity of 112T. Not an ideal explorer, but it works.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/lC4epCE.png'
        )
        await client.send_message(message.channel, embed=em)

    #Dolphin card
    if message.content.startswith('!dolphin'):
        em = discord.Embed(
              title='**Ship Overview - Dolphin**',
              description="""An affordable passenger carrier that opens a new set of missions.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `1 337 330 Cr`
                             Hardpoints: `2x Small`
                             Top Speed: `258 m/s`
                             Boost Speed: `361 m/s`
                             Agility: `143`
                             Cargo Capacity: `14T`
                             Unladen Jump Range: `10,67 Ly`
                             ```One of the more cost-effective explorers with good internals and jump range. It can also bring passengers along for long-range trips.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/TrxRcg3.png'
        )
        await client.send_message(message.channel, embed=em)

    #DBX card
    if message.content.startswith('!dbexplorer'):
        em = discord.Embed(
              title='**Ship Overview - Diamondback Explorer**',
              description="""An excellent explorer as well as a capable fighter.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `1 894 760 Cr`
                             Hardpoints: `2x Medium, 1x Large`
                             Top Speed: `242 m/s`
                             Boost Speed: `316 m/s`
                             Agility: `131`
                             Cargo Capacity: `12T`
                             Unladen Jump Range: `14,15 Ly`
                             ```This ship boasts one of the highest possible jump-ranges in the game for its cost. It is also fully capable of being a combat ship with its Large hardpoint.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/ZqzAQ1s.png'
        )
        await client.send_message(message.channel, embed=em)
        
    #ImpCourier card
    if message.content.startswith('!icourier'):
        em = discord.Embed(
              title='**Ship Overview - Imperial Courier**',
              description="""A great combat ship, often nicknamed a super Eagle.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `2 542 931 Cr`
                             Hardpoints: `3x Medium`
                             Top Speed: `277 m/s`
                             Boost Speed: `380 m/s`
                             Agility: `138`
                             Cargo Capacity: `12T`
                             Unladen Jump Range: `7,81 Ly`
                             ```A strong and agile combat vessel with one of the best cockpits, not great at exploring or trade however.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/WLeSfHf.png'
        )
        await client.send_message(message.channel, embed=em)
        
    #Keelback card
    if message.content.startswith('!keelback'):
        em = discord.Embed(
              title='**Ship Overview - Keelback**',
              description="""Type-6 modified for combat, it also has a fighter bay.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `3 126 150 Cr`
                             Hardpoints: `2x Small, 2x Medium`
                             Top Speed: `202 m/s`
                             Boost Speed: `303 m/s`
                             Agility: `135`
                             Cargo Capacity: `38T`
                             Unladen Jump Range: `10,94 Ly`
                             ```It doesn't do trading as well as the Type-6, but it can defend itself very well. The first ideal deep core miner.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/8FT9JE1.png'
        )
        await client.send_message(message.channel, embed=em)
        
    #ASPS card
    if message.content.startswith('!aspscout'):
        em = discord.Embed(
              title='**Ship Overview - Asp Scout**',
              description="""A cheaper variant of the Asp Explorer, a decent fighter-explorer hybrid.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `3 961 150 Cr`
                             Hardpoints: `2x Small, 2x Medium`
                             Top Speed: `223 m/s`
                             Boost Speed: `304 m/s`
                             Agility: `160`
                             Cargo Capacity: `16T`
                             Unladen Jump Range: `11,69 Ly`
                             ```It's a decent combat ship and a decent explorer. At the same time, it gets outclassed by the Asp Explorer in everything.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/ZwNXiwl.png'
        )
        await client.send_message(message.channel, embed=em)

    #Vulture card
    if message.content.startswith('!vulture'):
        em = discord.Embed(
              title='**Ship Overview - Vulture**',
              description="""A pure combat ship - deadly and nimble.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `4 925 615 Cr`
                             Hardpoints: `2x Large`
                             Top Speed: `210 m/s`
                             Boost Speed: `340 m/s`
                             Agility: `162`
                             Cargo Capacity: `8T`
                             Unladen Jump Range: `7,93 Ly`
                             ```It has great firepower thanks to its Large hardpoints, but its jump range and power plant hold it back.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/UKOQ3QA.png'
        )
        await client.send_message(message.channel, embed=em)
        
    #ASPX card
    if message.content.startswith('!aspx'):
        em = discord.Embed(
              title='**Ship Overview - Asp Explorer**',
              description="""An explorer's pick - and good for everything else too.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `6 661 153 Cr`
                             Hardpoints: `4x Small, 2x Medium`
                             Top Speed: `254 m/s`
                             Boost Speed: `345 m/s`
                             Agility: `140`
                             Cargo Capacity: `38T`
                             Unladen Jump Range: `13,12 Ly`
                             ```Exploration is in its name, and it's great. Good at combat as well as mining and trading.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/rziK2Hb.png'
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
