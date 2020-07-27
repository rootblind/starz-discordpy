"""
imagine = os.listdir('./images/cry')
        imgSelect = random.choice(imagine)
        path = './images/cry/' + imgSelect
"""


import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import time
import os
import praw

class Images(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def test(self, ctx):
        embed = discord.Embed(
            color= discord.Color.magenta()
        )
        embed.set_image(url='https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657')
        await ctx.send(embed = embed)

    @commands.command(pass_context=True)
    async def avatar(self, ctx, member: discord.Member = 'nimic'):
        if member == 'nimic':
            member = ctx.message.author

        embed = discord.Embed(
            title='Poza utilizatorului {0}'.format(member.name),
            colour=discord.Color.green()
        )
        embed.set_image(url='https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(member))
        await ctx.send(embed=embed)


    @commands.cooldown(1,3,commands.BucketType.user)
    @commands.command()
    async def cats(self, ctx):
        reddit = praw.Reddit(
            client_id= 'C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent= 'discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('cats').hot(), reddit.subreddit('cats').new(),reddit.subreddit('cats').top(), reddit.subreddit('cats').rising()]
        cats_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in cats_submissions if not x.stickied and x.over_18 == False)
        embed = discord.Embed(
            color=discord.Color.purple(),
            title= f'{submission.title}'
        )
        embed.set_image(url= f'{submission.url}')
        await ctx.send(embed = embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def earthporn(self, ctx):
        reddit = praw.Reddit(
            client_id='C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent='discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('EarthPorn').hot(), reddit.subreddit('EarthPorn').new(), reddit.subreddit('EarthPorn').top(), reddit.subreddit('EarthPorn').rising()]
        earthporn_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in earthporn_submissions if not x.stickied and x.over_18 == False)
        embed = discord.Embed(
            color=discord.Color.purple()
        )
        embed.set_image(url=f'{submission.url}')
        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(pass_context = True)
    async def animegirl(selfs, ctx):
        reddit = praw.Reddit(
            client_id='C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent='discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('AnimeGirls').hot(), reddit.subreddit('AnimeGirls').new(), reddit.subreddit('AnimeGirls').top(), reddit.subreddit('AnimeGirls').rising()]
        animegirl_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in animegirl_submissions if not x.stickied and x.over_18 is False)

        embed = discord.Embed(
            color=discord.Color.purple()
        )
        embed.set_image(url=f'{submission.url}')
        await ctx.send(embed=embed)



    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def dogs(self, ctx):
        reddit = praw.Reddit(
            client_id='C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent='discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('lookatmydog').hot(), reddit.subreddit('lookatmydog').new(), reddit.subreddit('lookatmydog').top(), reddit.subreddit('lookatmydog').rising()]
        dogs_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in dogs_submissions if not x.stickied and x.over_18 == False)
        embed = discord.Embed(
            color=discord.Color.purple(),
            title=f'{submission.title}'
        )
        embed.set_image(url=f'{submission.url}')
        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def pmemes(selfs, ctx):
        reddit = praw.Reddit(
            client_id='C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent='discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('ProgrammerHumor').hot(), reddit.subreddit('ProgrammerHumor').new(), reddit.subreddit('ProgrammerHumor').top(), reddit.subreddit('ProgrammingHumor').rising()]
        pmemes_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in pmemes_submissions if not x.stickied and x.over_18 == False)

        embed = discord.Embed(
            color=discord.Color.purple(),
            title= f'{submission.title}'
        )
        embed.set_image(url=f'{submission.url}')
        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def memes(selfs, ctx):
        reddit = praw.Reddit(
            client_id='C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent='discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('memes').hot(), reddit.subreddit('memes').new(),reddit.subreddit('memes').top(), reddit.subreddit('memes').rising()]
        memes_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in memes_submissions if not x.stickied and x.over_18 == False)
        embed = discord.Embed(
            color=discord.Color.purple(),
            title = f'{submission.title}'
        )
        embed.set_image(url=f'{submission.url}')
        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def foodporn(selfs, ctx):
        reddit = praw.Reddit(
            client_id='C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent='discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('foodporn').hot(), reddit.subreddit('foodporn').new(), reddit.subreddit('foodporn').top(), reddit.subreddit('foodporn').rising()]
        foodporn_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in foodporn_submissions if not x.stickied and x.over_18 == False)

        embed = discord.Embed(
            color=discord.Color.purple()
        )
        embed.set_image(url=f'{submission.url}')
        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def cmemes(selfs, ctx):
        reddit = praw.Reddit(
            client_id='C9UQ87btv1hPmg',
            client_secret='RaAm42WIXvE-dPbIE3_ZHfEN3GU',
            user_agent='discord bot: discord.me/ropp: v1.0 (by u/rootblind)'
        )
        list = [reddit.subreddit('mathmemes').hot(), reddit.subreddit('mathmemes').new(), reddit.subreddit('mathmemes').top(), reddit.subreddit('mathmemes').rising()]
        cmemes_submissions = random.choice(list)
        postPick = random.randint(1, 100)
        for i in range(0, postPick):
            submission = next(x for x in cmemes_submissions if not x.stickied and x.over_18 == False)

        embed = discord.Embed(
            color=discord.Color.purple(),
            title=f'{submission.title}'
        )
        embed.set_image(url=f'{submission.url}')
        await ctx.send(embed=embed)

    @commands.command(pass_context = True)
    async def cry(self, ctx, member: discord.Member):
        if member == self.client.user:
            titlu = f'**{ctx.message.author.name}**, nu te întrista, doar glumeam! hahah... scuze ;c'
        elif member != ctx.message.author:
            titlu = f'**{member.name}** l-a făcut pe utilizatorul **{ctx.message.author.name}** să pângă. <:imsad:695256837276041268>'
        else:
            titlu = f'**{ctx.message.author.name}** s-a întristat, putem face ceva în legătură cu asta?'


        embed = discord.Embed(
            color = discord.Color.purple(),
            title= titlu
        )
        imagine = ['https://iili.io/JB4lR4.gif','https://iili.io/JB40Ol.gif','https://iili.io/JB41b2.gif',
                    'https://iili.io/JB4GxS.gif','https://iili.io/JB4MW7.gif','https://iili.io/JB4Vs9.gif',
                    'https://iili.io/JB4Xfe.gif','https://iili.io/JB4h0u.gif','https://iili.io/JB4jUb.gif',
                    'https://iili.io/JB4NJj.gif','https://iili.io/JB4O5x.gif','https://iili.io/JB4eOQ.gif',
                    'https://iili.io/JB48zB.gif','https://iili.io/JB4kbV.gif','https://iili.io/JB4SWP.gif',
                    'https://iili.io/JB4Us1.gif','https://iili.io/JB4rqF.gif','https://media1.tenor.com/images/ae4138661bc1930d32c0435ef788c456/tenor.gif?itemid=15805005',
                    'https://media1.tenor.com/images/e59bd255f933ab786de2de0eb9b49cb9/tenor.gif?itemid=5012100',
                    'https://media1.tenor.com/images/dfe71ed2a46d64a2f662f8f3646f998f/tenor.gif?itemid=5947987',
                    'https://media1.tenor.com/images/8bf80a790c9ff78097dced38ea7f12fd/tenor.gif?itemid=16236259',
                    'https://media1.tenor.com/images/70616d7738bf7efccb08427fa6ae9333/tenor.gif?itemid=9911641',
                    'https://media1.tenor.com/images/2c8cfa2d1f72c8d12f0ddd180ba8536a/tenor.gif?itemid=5793886',
                    'https://media1.tenor.com/images/50e57eb7946b3da802c60aab7144c792/tenor.gif?itemid=15967180',
                    'https://media1.tenor.com/images/711641c2f21e75dc6018c97d89df1ac9/tenor.gif?itemid=4718167',
                    'https://media1.tenor.com/images/82d0122da8016f0d2ab9df573ff00dba/tenor.gif?itemid=7991414']
        imgSelect = random.choice(imagine)
        embed.set_image(url= imgSelect)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def kiss(self, ctx, member: discord.Member):
        if member == self.client.user:
            titlu = f'**{ctx.message.author.name}** mă pupă! Nu sumt om, utilizator porstuț! <:02woah:695256837867569222>'
        elif member != ctx.message.author:
            titlu = f'OMG! **{ctx.message.author.name}** și **{member.name}** se pupă! <:starheart:695256837317984298>'
        else:
            titlu = f'Utilizatorul **{ctx.message.author.name}** se ... pupă singur? <:yuubi:695256837825495050>'

        embed = discord.Embed(
            color=discord.Color.purple(),
            title=titlu
        )
        imagine = ['https://cdn.weeb.sh/images/SydfnauPb.gif', 'https://cdn.weeb.sh/images/HJkxXNtjZ.gif','https://cdn.weeb.sh/images/B1NwJg9Jz.gif',
                    'https://iili.io/JBtwNa.gif','https://iili.io/JBtNDJ.gif','https://iili.io/JBteov.gif',
                    'https://iili.io/JBtkVR.gif','https://iili.io/JBtvPp.gif','https://iili.io/JBtSKN.gif',
                    'https://iili.io/JBtUlI.gif','https://iili.io/JBtgSt.gif','https://iili.io/JBt4HX.gif',
                    'https://iili.io/JBt6Rn.gif','https://iili.io/JBtPNs.gif','https://data.whicdn.com/images/198163986/original.gif',
                    'https://media.giphy.com/media/ZRSGWtBJG4Tza/giphy.gif',
                    'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657',
                    'https://media1.tenor.com/images/2f23c53755a5c3494a7f54bbcf04d1cc/tenor.gif?itemid=13970544',
                    'https://media1.tenor.com/images/86b2783ea71f013f4c2dabc1e0cb6574/tenor.gif?itemid=3990323',
                    'https://media1.tenor.com/images/5cf6c2fef93911111538d837ec71c24c/tenor.gif?itemid=5448064',
                    'https://media1.tenor.com/images/e2041500e95fe895dc19fad6aeac73d3/tenor.gif?itemid=14702585',
                    'https://media.tenor.com/images/b8058bdd703fd6b7817b4cf6e22bebd8/tenor.gif',
                    'https://media1.tenor.com/images/705373be55629cf85c48f0b9c797f681/tenor.gif?itemid=14478612',
                    'https://media1.tenor.com/images/21520a115cfa99761d44cb6827d13909/tenor.gif?itemid=16585116',
                    'https://media1.tenor.com/images/77b755b246126dca1a1c6880cb0a0174/tenor.gif?itemid=14701003',
                    'https://media1.tenor.com/images/6e51db439e83836a2190750df30e55fd/tenor.gif?itemid=5739146']
        imgSelect = random.choice(imagine)
        embed.set_image(url=imgSelect)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def hug(self, ctx, member: discord.Member):
        if member == self.client.user:
            titlu = f'Oooh! Ce dulce, **{ctx.message.author.name}**, vino aici! <:gnargnaw:690194560055509033>'
        elif member != ctx.message.author:
            titlu = f'Pare că **{ctx.message.author.name}** și **{member.name}** au o îmbrățișare călduroasă <:foxheart:695256837431230505>'
        else:
            titlu = f'**{ctx.message.author.name}** simte nevoia unei îmbrățișări, se oferă cineva? <:yuubi:695256837825495050>'

        embed = discord.Embed(
            color=discord.Color.purple(),
            title=titlu
        )
        imagine = ['https://iili.io/JBmAcN.gif','https://iili.io/JBmuFp.gif','https://iili.io/JBmRSI.gif',
                    'https://iili.io/JBm79t.gif','https://iili.io/JBmYAX.gif','https://iili.io/JBmaNn.gif',
                    'https://iili.io/JBmcts.gif','https://iili.io/JBm0oG.gif','https://iili.io/JBm1Vf.gif',
                    'https://iili.io/JBmEP4.gif','https://iili.io/JBmMKl.gif','https://iili.io/JBmVl2.gif',
                    'https://iili.io/JBmWSS.gif','https://iili.io/JBmhH7.gif','https://iili.io/JBmjR9.gif',
                    'https://iili.io/JBmwNe.gif','https://iili.io/JBmNDu.gif','https://iili.io/JBmeob.gif',
                    'https://iili.io/JBmkVj.gif','https://iili.io/JBmvix.gif','https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935',
                    'https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587',
                    'https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716',
                    'https://media1.tenor.com/images/3ce31b15c2326831a8de9f0b693763ff/tenor.gif?itemid=16787485',
                    'https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460',
                    'https://tenor.com/view/anime-hug-catgirl-neko-gif-9383138','https://tenor.com/view/anime-choke-hug-too-tight-gif-14108949',
                    'https://media1.tenor.com/images/b068ce2d77691f684197799fc0e876a9/tenor.gif?itemid=16057337',
                    'https://media1.tenor.com/images/e7797629681a227c12bc112513bef070/tenor.gif?itemid=9383100',
                    'https://media1.tenor.com/images/cd321aa5d055a7e02b52eea806b9797c/tenor.gif?itemid=12861205',
                    'https://media1.tenor.com/images/0e0a399c34e533edf0ab00e20fb6e0a1/tenor.gif?itemid=6118800',
                    'https://media1.tenor.com/images/33562a9e9ce3dc9500bbaeb98a413a4e/tenor.gif?itemid=8164652']

        imgSelect = random.choice(imagine)
        embed.set_image(url=imgSelect)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def slap(self, ctx, member: discord.Member):
        if member == self.client.user:
            await ctx.send(f'<@{ctx.message.author.id}> doar nu credeai că o să te las pur și simplu să-mi dai palme. <:MaikaSmug:673921437182197840>')
            return 0
        elif member != ctx.message.author:
            titlu = f'{ctx.message.author.name} îi dă mare capac utilizatorului {member.name} de l-a troznit. <:angrystar:673946308842618910>'
        else:
            titlu = f'**{ctx.message.author.name}** își dă palme singur ... oare să-l oprim? <:yuubi:695256837825495050>'

        embed = discord.Embed(
            color=discord.Color.purple(),
            title=titlu
        )
        imagine = ['https://iili.io/JBpFsf.gif','https://iili.io/JBp3WG.gif','https://iili.io/JBpff4.gif','https://iili.io/JBpq0l.gif',
                    'https://iili.io/JBpBg2.gif','https://iili.io/JBpnJS.gif','https://iili.io/JBpo57.gif','https://iili.io/JBpxe9.gif',
                    'https://iili.io/JBpzbe.gif','https://iili.io/JBpTzu.gif','https://iili.io/JBpuWb.gif','https://iili.io/JBpAsj.gif',
                    'https://iili.io/JBp5qx.gif','https://iili.io/JBp70Q.gif','https://iili.io/JBpYgV.gif','https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956',
                    'https://media1.tenor.com/images/89309d227081132425e5931fbbd7f59b/tenor.gif?itemid=4880762',
                    'https://media1.tenor.com/images/05e52a1fcbcca5f33f0bebeef01b3d0a/tenor.gif?itemid=12372250',
                    'https://media1.tenor.com/images/cb9821d48f96fe91696e4300f9efa222/tenor.gif?itemid=16545882',
                    'https://media1.tenor.com/images/3dae4949c6570b8c78e608347004affc/tenor.gif?itemid=7462957',
                    'https://media1.tenor.com/images/f9777dc82d3e5ba3127618ebf166ac52/tenor.gif?itemid=10519542']
        imgSelect = random.choice(imagine)
        embed.set_image(url=imgSelect)
        await ctx.send(embed=embed)


    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.purple(),
                title=f'**{ctx.message.author.name}** își dă palme singur ... oare să-l oprim? <:yuubi:695256837825495050>'
            )
            imagine = ['https://iili.io/JBpFsf.gif','https://iili.io/JBp3WG.gif','https://iili.io/JBpff4.gif','https://iili.io/JBpq0l.gif',
                    'https://iili.io/JBpBg2.gif','https://iili.io/JBpnJS.gif','https://iili.io/JBpo57.gif','https://iili.io/JBpxe9.gif',
                    'https://iili.io/JBpzbe.gif','https://iili.io/JBpTzu.gif','https://iili.io/JBpuWb.gif','https://iili.io/JBpAsj.gif',
                    'https://iili.io/JBp5qx.gif','https://iili.io/JBp70Q.gif','https://iili.io/JBpYgV.gif','https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956',
                    'https://media1.tenor.com/images/89309d227081132425e5931fbbd7f59b/tenor.gif?itemid=4880762',
                    'https://media1.tenor.com/images/05e52a1fcbcca5f33f0bebeef01b3d0a/tenor.gif?itemid=12372250',
                    'https://media1.tenor.com/images/cb9821d48f96fe91696e4300f9efa222/tenor.gif?itemid=16545882',
                    'https://media1.tenor.com/images/3dae4949c6570b8c78e608347004affc/tenor.gif?itemid=7462957',
                    'https://media1.tenor.com/images/f9777dc82d3e5ba3127618ebf166ac52/tenor.gif?itemid=10519542']
            imgSelect = random.choice(imagine)
            embed.set_image(url=imgSelect)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> ori îi scrii numele greșit, ori îți un imaginezi nume.')
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> așteaptă 3 secunde, utilizator arțăgos!')

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.purple(),
                title=f'**{ctx.message.author.name}** simte nevoia unei îmbrățișări, se oferă cineva? <:yuubi:695256837825495050>'
            )
            imagine = ['https://iili.io/JBmAcN.gif','https://iili.io/JBmuFp.gif','https://iili.io/JBmRSI.gif',
                    'https://iili.io/JBm79t.gif','https://iili.io/JBmYAX.gif','https://iili.io/JBmaNn.gif',
                    'https://iili.io/JBmcts.gif','https://iili.io/JBm0oG.gif','https://iili.io/JBm1Vf.gif',
                    'https://iili.io/JBmEP4.gif','https://iili.io/JBmMKl.gif','https://iili.io/JBmVl2.gif',
                    'https://iili.io/JBmWSS.gif','https://iili.io/JBmhH7.gif','https://iili.io/JBmjR9.gif',
                    'https://iili.io/JBmwNe.gif','https://iili.io/JBmNDu.gif','https://iili.io/JBmeob.gif',
                    'https://iili.io/JBmkVj.gif','https://iili.io/JBmvix.gif','https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935',
                    'https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587',
                    'https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716',
                    'https://media1.tenor.com/images/3ce31b15c2326831a8de9f0b693763ff/tenor.gif?itemid=16787485',
                    'https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460',
                    'https://tenor.com/view/anime-hug-catgirl-neko-gif-9383138','https://tenor.com/view/anime-choke-hug-too-tight-gif-14108949',
                    'https://media1.tenor.com/images/b068ce2d77691f684197799fc0e876a9/tenor.gif?itemid=16057337',
                    'https://media1.tenor.com/images/e7797629681a227c12bc112513bef070/tenor.gif?itemid=9383100',
                    'https://media1.tenor.com/images/cd321aa5d055a7e02b52eea806b9797c/tenor.gif?itemid=12861205',
                    'https://media1.tenor.com/images/0e0a399c34e533edf0ab00e20fb6e0a1/tenor.gif?itemid=6118800',
                    'https://media1.tenor.com/images/33562a9e9ce3dc9500bbaeb98a413a4e/tenor.gif?itemid=8164652']
            imgSelect = random.choice(imagine)
            embed.set_image(url=imgSelect)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> ori îi scrii numele greșit, ori îți imaginezi un nume.')
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> așteaptă 3 secunde, utilizator cu nevoie de atenție!')


    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.purple(),
                title=f'Utilizatorul **{ctx.message.author.name}** se ... pupă singur? <:yuubi:695256837825495050>'
            )
            imagine = ['https://cdn.weeb.sh/images/SydfnauPb.gif', 'https://cdn.weeb.sh/images/HJkxXNtjZ.gif','https://cdn.weeb.sh/images/B1NwJg9Jz.gif',
                    'https://iili.io/JBtwNa.gif','https://iili.io/JBtNDJ.gif','https://iili.io/JBteov.gif',
                    'https://iili.io/JBtkVR.gif','https://iili.io/JBtvPp.gif','https://iili.io/JBtSKN.gif',
                    'https://iili.io/JBtUlI.gif','https://iili.io/JBtgSt.gif','https://iili.io/JBt4HX.gif',
                    'https://iili.io/JBt6Rn.gif','https://iili.io/JBtPNs.gif','https://data.whicdn.com/images/198163986/original.gif',
                    'https://media.giphy.com/media/ZRSGWtBJG4Tza/giphy.gif',
                    'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657',
                    'https://media1.tenor.com/images/2f23c53755a5c3494a7f54bbcf04d1cc/tenor.gif?itemid=13970544',
                    'https://media1.tenor.com/images/86b2783ea71f013f4c2dabc1e0cb6574/tenor.gif?itemid=3990323',
                    'https://media1.tenor.com/images/5cf6c2fef93911111538d837ec71c24c/tenor.gif?itemid=5448064',
                    'https://media1.tenor.com/images/e2041500e95fe895dc19fad6aeac73d3/tenor.gif?itemid=14702585',
                    'https://media.tenor.com/images/b8058bdd703fd6b7817b4cf6e22bebd8/tenor.gif',
                    'https://media1.tenor.com/images/705373be55629cf85c48f0b9c797f681/tenor.gif?itemid=14478612',
                    'https://media1.tenor.com/images/21520a115cfa99761d44cb6827d13909/tenor.gif?itemid=16585116',
                    'https://media1.tenor.com/images/77b755b246126dca1a1c6880cb0a0174/tenor.gif?itemid=14701003',
                    'https://media1.tenor.com/images/6e51db439e83836a2190750df30e55fd/tenor.gif?itemid=5739146']
            imgSelect = random.choice(imagine)
            embed.set_image(url = imgSelect)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> ori îi scrii numele greșit, ori îți imaginezi un nume.')
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> așteaptă 3 secunde, utilizator pupăcios!')


    @cry.error
    async def cry_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):

            embed = discord.Embed(
                color=discord.Color.purple(),
                title= f'**{ctx.message.author.name}** s-a întristat, putem face ceva în legătură cu asta?'
            )
            imagine = ['https://iili.io/JB4lR4.gif','https://iili.io/JB40Ol.gif','https://iili.io/JB41b2.gif',
                    'https://iili.io/JB4GxS.gif','https://iili.io/JB4MW7.gif','https://iili.io/JB4Vs9.gif',
                    'https://iili.io/JB4Xfe.gif','https://iili.io/JB4h0u.gif','https://iili.io/JB4jUb.gif',
                    'https://iili.io/JB4NJj.gif','https://iili.io/JB4O5x.gif','https://iili.io/JB4eOQ.gif',
                    'https://iili.io/JB48zB.gif','https://iili.io/JB4kbV.gif','https://iili.io/JB4SWP.gif',
                    'https://iili.io/JB4Us1.gif','https://iili.io/JB4rqF.gif','https://media1.tenor.com/images/ae4138661bc1930d32c0435ef788c456/tenor.gif?itemid=15805005',
                    'https://media1.tenor.com/images/e59bd255f933ab786de2de0eb9b49cb9/tenor.gif?itemid=5012100',
                    'https://media1.tenor.com/images/dfe71ed2a46d64a2f662f8f3646f998f/tenor.gif?itemid=5947987',
                    'https://media1.tenor.com/images/8bf80a790c9ff78097dced38ea7f12fd/tenor.gif?itemid=16236259',
                    'https://media1.tenor.com/images/70616d7738bf7efccb08427fa6ae9333/tenor.gif?itemid=9911641',
                    'https://media1.tenor.com/images/2c8cfa2d1f72c8d12f0ddd180ba8536a/tenor.gif?itemid=5793886',
                    'https://media1.tenor.com/images/50e57eb7946b3da802c60aab7144c792/tenor.gif?itemid=15967180',
                    'https://media1.tenor.com/images/711641c2f21e75dc6018c97d89df1ac9/tenor.gif?itemid=4718167',
                    'https://media1.tenor.com/images/82d0122da8016f0d2ab9df573ff00dba/tenor.gif?itemid=7991414']
            imgSelect = random.choice(imagine)
            embed.set_image(url=imgSelect)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> ori îi scrii numele greșit, ori îți imaginezi un nume.')
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> așteaptă 3 secunde, utilizator plângăcios!')


    @foodporn.error
    async def cmemes_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `cmemes` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @foodporn.error
    async def foodporn_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `foodporn` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @memes.error
    async def memes_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `memes` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @pmemes.error
    async def pmemes_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `pmemes` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @dogs.error
    async def dogs_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `dogs` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @cats.error
    async def cats_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `cats` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @animegirl.error
    async def animegirl_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `animegirl` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @earthporn.error
    async def earthporn_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `earthporn` este în cooldown pentru încă {int(error.retry_after)}s.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare încercând să deschid imaginea, mai încearcă.')

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> va trebui să specifici a cui steluță vrei să o vezi.')
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> uh, am impresia că inventezi nume.')
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `addfriend` are un cooldown de 10 secunde. Prietenii nu se fac așa rapid.')







def setup(client):
    client.add_cog(Images(client))
