import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import time
import os

dancers = []
in_attack = {}
class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def barbut(self, ctx):
        zar1 = random.choice(range(1, 7))
        zar2 = random.choice(range(1, 7))
        await ctx.send(f'<@{ctx.message.author.id}> a dat cu zarul: {zar1} - {zar2} [{zar1 + zar2}]')


    @commands.command(pass_context = True)
    async def dance(self, ctx, action = 'join'):
        global dancers
        if action == 'join':
            if not ctx.message.author in dancers:
                dancers.append(ctx.message.author)
                if len(dancers) == 1:
                    title = f'{ctx.message.author.name} a început o petrecere!\n,dance pentru a te alătura dansului.'
                else:
                    title = f'{ctx.message.author.name} s-a alăturat petrecerii.\n ,dance pentru a te alătura.'
            else:
                title = f'Petrecerea este pe val! <:yo:673946322050744341>'
        elif action == 'stop':
            if len(dancers) > 0:
                if ctx.message.author == dancers[0]:
                    title = f'Gata distractia, {ctx.message.author.name} a decis că am petrecut suficient. <:thatscute:695256837666373692>\nNumărul de dansatori: {len(dancers)}'
                    embed = discord.Embed(
                        color=discord.Color.purple(),
                        title=title
                    )
                    embed.set_image(url = 'https://i.pinimg.com/originals/42/6a/97/426a975d9a18a5a13c2b653cfd3d42a4.gif')
                    dancers.clear()
                    await ctx.send(embed = embed)
                    return 0
                else:
                    await ctx.send(f'<@{ctx.message.author.id}> doar gazda petrecerii, **{dancers[0]}**, poate opri petrecerea.')
                    return 0
            else:
                await ctx.send(f'<@{ctx.message.author.id}> uh ... cum vrei să oprești petrecerea înainte să înceapă?')
                return 0
        else:
            await ctx.send(f'<@{ctx.message.author.id}> aia s-o faci tu, nu eu! <:angrystar:673946308842618910>')
            return 0

        embed = discord.Embed(
            color=discord.Color.purple(),
            title=title
        )

        dancelevels = ['https://i.pinimg.com/originals/d9/a5/ce/d9a5ced7243203fd37cf6cf4bbc5bfd4.gif',
                       'https://media2.giphy.com/media/13p77tfexyLtx6/source.gif',
                       'https://i.pinimg.com/originals/2f/ee/eb/2feeeb692936e347562498ad12e9f6ff.gif',
                       'https://cdn.discordapp.com/attachments/326974694874021890/716627695697657866/tenor.gif']
        if len(dancelevels) - 1 <= len(dancers) / 3:
            level = len(dancelevels) - 1
        else:
            level = int(len(dancers) / 3)
        embed.set_footer(text = f'Dansatori: {len(dancers)} / {int(level * 3 + 3)}')
        embed.set_image(url= dancelevels[level])
        await ctx.send(embed=embed)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context = True, aliases = ['atac','attack'])
    async def atacc(self, ctx, member: discord.Member):
        global in_attack
        if member == self.client.user:
            stardodge = discord.Embed(
                color= discord.Color.red(),
                title='Hit me if you can XDDDDD'
            )
            stardodge.set_image(url= 'https://cdn.discordapp.com/attachments/626096078755725353/697223687891451944/image0_2.gif')
            await ctx.send(embed=stardodge)
            return 0
        if member == ctx.message.author:
            if str(ctx.message.author.id) in in_attack:
                in_attack.pop(str(ctx.message.author.id))
            embedkms = discord.Embed(
                color= discord.Color.dark_red(),
                title= f'{ctx.message.author.name} s-a atacat și a comis \"aliven\'t\". <:monkaAnime:696707691954831391>'
            )
            embedkms.set_author(name=f'{ctx.message.author.name}: 0 / 100', icon_url='https://vignette.wikia.nocookie.net/minecraft/images/7/71/WitheredHeart.png/revision/latest/top-crop/width/220/height/220?cb=20160526041638')
            await ctx.send(embed=embedkms)
            return 0

        damage_dealt = random.choice(range(0, 61))
        if not str(ctx.message.author.id) in in_attack:
            in_attack[str(ctx.message.author.id)] = 100

        if str(member.id) in in_attack:
            in_attack[str(member.id)] -= damage_dealt
        else:
            in_attack[str(member.id)] = 100 - damage_dealt

        embed = discord.Embed(
            color= discord.Color.red(),
            title= f'{ctx.message.author.name} a lovit utilizatorul {member.name}.',
            description=f'Damage: {damage_dealt}'
        )

        if in_attack.get(str(member.id)) < 33:
            theurl = 'https://vignette.wikia.nocookie.net/minecraft/images/7/71/WitheredHeart.png/revision/latest/top-crop/width/220/height/220?cb=20160526041638'
        elif in_attack.get(str(member.id)) < 66:
            theurl = 'https://i.ya-webdesign.com/images/minecraft-heart-png.png'
        else:
            theurl = 'https://i.pinimg.com/originals/e4/5b/be/e45bbe31793e5ca34e44bd6d6f621aa1.png'

        embed.set_author(name= f'{member.name}: {in_attack[str(member.id)]} / 100', icon_url= theurl)
        attacks = ['https://iili.io/JBpFsf.gif','https://iili.io/JBp3WG.gif','https://iili.io/JBpff4.gif','https://iili.io/JBpq0l.gif',
                    'https://iili.io/JBpBg2.gif','https://iili.io/JBpnJS.gif','https://iili.io/JBpo57.gif','https://iili.io/JBpxe9.gif',
                    'https://iili.io/JBpzbe.gif','https://iili.io/JBpuWb.gif','https://iili.io/JBpAsj.gif',
                    'https://iili.io/JBp5qx.gif','https://iili.io/JBp70Q.gif','https://iili.io/JBpYgV.gif','https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956',
                    'https://media1.tenor.com/images/05e52a1fcbcca5f33f0bebeef01b3d0a/tenor.gif?itemid=12372250',
                    'https://media1.tenor.com/images/cb9821d48f96fe91696e4300f9efa222/tenor.gif?itemid=16545882',
                    'https://media1.tenor.com/images/3dae4949c6570b8c78e608347004affc/tenor.gif?itemid=7462957',
                    'https://media1.tenor.com/images/f9777dc82d3e5ba3127618ebf166ac52/tenor.gif?itemid=10519542']
        embed.set_image(url= random.choice(attacks))
        await ctx.send(embed=embed)

        if in_attack.get(str(member.id)) <= 0:
            embeddeath = discord.Embed(
                color= discord.Color.dark_red()
            )
            embeddeath.set_author(name=f'Utilizatorul {member.name} a fost eliminat de {ctx.message.author.name}.')
            ko_img = ['https://media1.tenor.com/images/89309d227081132425e5931fbbd7f59b/tenor.gif?itemid=4880762',
                      'https://media1.tenor.com/images/c03828c5fac2d1342fa5a5462c3a5ac7/tenor.gif?itemid=11610001',
                      'https://media1.tenor.com/images/b858fbf740f162ef370ca22188d6c3ee/tenor.gif?itemid=14791113']
            embeddeath.set_image(url= random.choice(ko_img))
            await ctx.send(embed=embeddeath)
            in_attack.pop(str(member.id))
            in_attack.pop(str(ctx.message.author.id))

    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.command(pass_context = True,aliases = ['protect'])
    async def protecc(self, ctx, member: discord.Member = 'da'):
        if member == 'da':
            member = ctx.message.author
        elif member == self.client.user:
            stardodge = discord.Embed(
                color=discord.Color.red(),
                title='Nu e nevoie să mă aperi, uite ce rapid mă mișc.'
            )
            stardodge.set_image(
                url='https://cdn.discordapp.com/attachments/626096078755725353/697223687891451944/image0_2.gif')
            await ctx.send(embed=stardodge)
            return 0
        global in_attack
        if not str(member.id) in in_attack:
            in_attack[str(member.id)] = 100

        damage_healed = random.choice(range(10, 31))

        if in_attack.get(str(member.id)) + damage_healed > 100:
            damage_healed = 100 - in_attack.get(str(member.id))

        if str(member.id) in in_attack:
            in_attack[str(member.id)] += damage_healed

        if not str(ctx.message.author.id) in in_attack:
            in_attack[str(ctx.message.author.id)] = 100

        if member == ctx.message.author:
            titlu = f'{ctx.message.author.name} își ridică protecția. :shield: '
        else:
            titlu = f'{ctx.message.author.name} ia apărarea utilizatorului {member.name}. <:excitedumb:695989215229509703>'


        embed = discord.Embed(
            color=discord.Color.red(),
            title=titlu,
            description=f'Protection: {damage_healed}'
        )

        if in_attack.get(str(member.id)) < 33:
            theurl = 'https://vignette.wikia.nocookie.net/minecraft/images/7/71/WitheredHeart.png/revision/latest/top-crop/width/220/height/220?cb=20160526041638'
        elif in_attack.get(str(member.id)) < 66:
            theurl = 'https://i.ya-webdesign.com/images/minecraft-heart-png.png'
        else:
            theurl = 'https://i.pinimg.com/originals/e4/5b/be/e45bbe31793e5ca34e44bd6d6f621aa1.png'

        embed.set_author(name=f'{member.name}: {in_attack[str(member.id)]} / 100', icon_url=theurl)
        defences = ['https://media1.tenor.com/images/c6e609f26fd3ab817fb03013ff84afb2/tenor.gif?itemid=4867277',
                    'https://media1.tenor.com/images/a9bfb133403a3c933a5d9b555c95b8bc/tenor.gif?itemid=15903770',
                    'https://media1.tenor.com/images/b1d75abc192402f7309edd5bc150affb/tenor.gif?itemid=5769349',
                    'https://media1.tenor.com/images/79f02ed10368da52ee234b1bf9f2731d/tenor.gif?itemid=12119784',
                    'https://media1.tenor.com/images/3f94a775e89f8c18f3dcd373546a9540/tenor.gif?itemid=13471918']
        embed.set_image(url=random.choice(defences))
        await ctx.send(embed=embed)

    @commands.command(pass_context = True)
    async def doors(self, ctx, pickDoor, ammount = '10'):

        if os.path.exists(f'./economy/{ctx.message.author.id}.txt'):
            authorBalance = open(f'economy/{ctx.message.author.id}.txt','r')
        else:
            authorBalance = open(f'economy/{ctx.message.author.id}.txt', 'a')
            authorBalance.write(str(0))
            authorBalance.close()
            authorBalance = open(f'economy/{ctx.message.author.id}.txt', 'r')

        thedoors = [1, 2, 3, 4]

        balance = authorBalance.read()
        authorBalance.close()

        if not int(pickDoor) in thedoors:
            await ctx.send(f'<@{ctx.message.author.id}> Ușile sunt numerotate de la 1 la 4.')
            return 0

        try:
            if int(ammount) < 0:
                await ctx.send(f'<@{ctx.message.author.id}> `{ctx.message.content}` nu este o valoare valida.')
                return 0
        except:
            await ctx.send(f'<@{ctx.message.author.id}> `{ctx.message.content}` nu este o valoare valida.')
            return 0

        if int(ammount) < 10:
            await ctx.send(f'<@{ctx.message.author.id}> suma minimă ce poate fi jucată este `10`.')
            return 0

        if int(ammount) > int(balance):
            await ctx.send(f'<@{ctx.message.author.id}> nu ai {ammount} <:python:694344808533327875>  în balanța ta.')
            return 0

        baddoor1 = random.choice(thedoors)
        thedoors.remove(int(baddoor1))

        baddoor2 = random.choice(thedoors)

        thedoors.remove(baddoor2)

        neutraldoor = random.choice(thedoors)
        thedoors.remove(neutraldoor)

        authorBalance = open(f'economy/{ctx.message.author.id}.txt','w')

        if int(pickDoor) == baddoor1:
            title= f'{ctx.message.author.name} a deschis ușa {pickDoor}, aceasta fiind goală. -{ammount} <:python:694344808533327875>\nBalanța: {int(balance) - int(ammount)} <:python:694344808533327875>'
            authorBalance.write(str(int(balance) - int(ammount)))
            authorBalance.close()
        elif int(pickDoor) == baddoor2:
            title = f'{ctx.message.author.name} a deschis ușa {pickDoor} și a găsit jumătate din banii investiți. -{int(int(ammount) / 2)} <:python:694344808533327875>\nBalanța: {int(balance) - int(int(ammount) / 2)} <:python:694344808533327875>'
            authorBalance.write(str(int(balance) - int(int(ammount) / 2)))
            authorBalance.close()
        elif int(pickDoor) == neutraldoor:
            title = f'{ctx.message.author.name} a deschis ușa {pickDoor} și a găsit banii investiți.\nBalanța: {int(balance)} <:python:694344808533327875>'
            authorBalance.write(str(balance))
            authorBalance.close()
        else:
            title = f'{ctx.message.author.name} a deschis ușa {pickDoor} și a găsit {int(ammount) + 10} <:python:694344808533327875> + banii investiți.\nBalanța: {int(balance) + int(ammount) + 10} <:python:694344808533327875>'
            authorBalance.write(str(int(balance) + int(ammount) + 10))
            authorBalance.close()

        embed = discord.Embed(
            color=discord.Color.green(),
            title=title

        )
        await ctx.send(embed=embed)

    @doors.error
    async def doors_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> valoare invalidă.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> alege un număr de la 1 la 4.')


    @protecc.error
    async def protecc_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `protecc` este în cooldown pentru încă {int(error.retry_after)}s.')
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(
                f'<@{ctx.message.author.id}> numele introdus este greșit.')

    @atacc.error
    async def atacc_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `atacc` este în cooldown pentru încă {int(error.retry_after)}s.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> ai atacat aierul, dar nu pare să aibă efect, încearcă să ataci o persoană.')
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> la fiecare comandă cu mention spun asta, dar: scrie-i numele așa cum e acolo, nu cum îți vine ție.')


    @barbut.error
    async def barbut_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `barbut` este în cooldown pentru încă {int(error.retry_after)}s.')
            return 0
        raise error


def setup(client):
    client.add_cog(Games(client))
