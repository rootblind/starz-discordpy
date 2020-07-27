import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import time
import os

class Casual(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! :ping_pong: {round(self.client.latency * 1000)}ms")



    @commands.command(pass_context = True)
    async def starz(self, ctx, *, mesaj = 'nimic'):
        if 'iubesc' in mesaj:
            await ctx.send(f'<@{ctx.message.author.id}> Și eu te iubi bubi!')
        elif 'iubesti' in mesaj:
            await ctx.send(f'<@{ctx.message.author.id}> Mereu te-am iubit, de ce întrebi?')
        else:
            await ctx.send(f'Ce?')

    @commands.command(pass_context = True)
    async def reminder(self, ctx, *, mesaj):
        await ctx.author.send(f'**Mesaj**: {mesaj}\n**Trimis la**: {datetime.datetime.now()}')

    @commands.command(pass_context=True)
    async def echo(self, ctx, *, mesaj):
        msg = await ctx.channel.fetch_message(ctx.message.id)
        await msg.delete()
        if '@everyone' in mesaj:
            mesaj = mesaj.replace('@everyone','#everyone')
        if '@here' in mesaj:
            mesaj = mesaj.replace('@here','#here')
        await ctx.send(f'{mesaj}')

    @commands.command(pass_context = True)
    async def loverate(self, ctx, member1: discord.Member, member2: discord.Member = 'da'):
        if member2 == 'da':
            member2 = ctx.message.author
        rata = random.choice(range(0,101))
        embed = discord.Embed(
            color= discord.Color.magenta(),
            title= f'Rata: {rata}%'
        )
        if rata < 33:
            theurl = 'https://vignette.wikia.nocookie.net/minecraft/images/7/71/WitheredHeart.png/revision/latest/top-crop/width/220/height/220?cb=20160526041638'
        elif rata < 66:
            theurl = 'https://i.ya-webdesign.com/images/minecraft-heart-png.png'
        else:
            theurl = 'https://i.pinimg.com/originals/e4/5b/be/e45bbe31793e5ca34e44bd6d6f621aa1.png'

        embed.set_author(name= f'{member1.name} & {member2.name}', icon_url= theurl)
        await ctx.send(embed=embed)

    @commands.command(pass_context = True)
    async def ship(self, ctx, nume1, nume2):
        embed = discord.Embed(
            color= discord.Color.magenta(),
            title = f'{nume1[0:int((len(nume1) + 1) / 2)] + nume2[int((len(nume2))/ 2):len(nume2)]}'
        )
        embed.set_author(name=f' {nume1} + {nume2}:')
        await ctx.send(embed=embed)

    @ship.error
    async def ship_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> Ai nevoie de 2 cuvinte pentru a face ship.')

    @loverate.error
    async def loverate_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> îi scrii numele greșit.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> am nevoie de cel puțin 1 persoana pentru a măsura rata de iubire.')

    @echo.error
    async def echo_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> ai zis ceva?')

    @reminder.error
    async def reminder_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            return 0
            #momentan nimic


def setup(client):
    client.add_cog(Casual(client))