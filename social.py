
import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import time
import os

propose = {}

class Social(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def addfriend(self, ctx, member: discord.Member):
        userfriendsid = open(f'ffriends/{ctx.message.author.name}_fid.txt', 'a')
        fileread = open(f'ffriends/{ctx.message.author.name}_fid.txt', 'r')
        counter = 0
        for checkfriends in fileread:
            counter += 1
            if checkfriends[0:len(checkfriends) - 1] == str(member.id):
                await ctx.send(f'<@{ctx.message.author.id}> voi doi sunteți deja prieteni, ai uitat?')
                return 0
        if ctx.message.author.name == member.name:
            await ctx.send(f'<@{ctx.message.author.id}> poate că nu ai mulți prieteni, dar nu fi nici chiar așa.')
            return 0
        if counter > 50:
            await ctx.send(
                f'<@{ctx.message.author.id}> nu poți avea maxim 50 de prieteni, nici eu nu sunt asa populară. <:coolone:673905171272695828>\nDacă doreși sa îți faci lo în lista de prieteni, zic să mai scapi din ei cu `unfriend`.')
            return 0
        userfriendsid.write('{0}\n'.format(member.id))
        counter += 1
        if member == self.client.user:
            await ctx.send(
                f'<@{ctx.message.author.id}> Vrei să fim prieteni?! Vai, multumesc, ne vom înțelege de minune, ai să vezi! <:yo:673946322050744341>\nMai ai {50 - counter} de sloturi libere.')
        else:
            await ctx.send(
                f'<@{ctx.message.author.id}> de acum, tu și **{member.name}** sunteți prieteni, yey! <:yo:673946322050744341>\nMai ai {50 - counter} de sloturi libere.')
        userfriendsid.close()


    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def resetfriendlist(self, ctx):
        if os.path.exists(f'ffriends/{ctx.message.author.name}_fid.txt') and os.stat(
                f'ffriends/{ctx.message.author.name}_fid.txt').st_size != 0:
            os.remove(f'ffriends/{ctx.message.author.name}_fid.txt')
            await ctx.send(f'<@{ctx.message.author.id}> lista ta de prieteni a fost resetată ... cam singuratic fără ei.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> lista ta de prieteni este deja goală.')


    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def friendlist(self, ctx, member: discord.Member = 'da'):
        if member == 'da':
            member = ctx.message.author
        flist = open(f'ffriends/{member.name}_fid.txt', 'r')
        counter = int(0)
        for friends in flist:
            counter += 1
        flist.close()
        embed = discord.Embed(
            title='Lista de prieteni a utilizatorului {0}'.format(member.name),
            colour=discord.Color.blue(),
            description=f'Sloturi: {50 - counter} / 50'
        )
        embed2 = discord.Embed(
            colour=discord.Color.blue()
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(member))
        flist = open(f'ffriends/{member.name}_fid.txt', 'r')
        counter = int(0)
        for friends in flist:
            if counter <= 25:
                embed.add_field(name=f'{counter + 1}', value=f'<@{friends[0:len(friends) - 1]}>', inline=False)
                counter += 1
            else:
                embed2.add_field(name=f'{counter + 1}', value=f'<@{friends[0:len(friends) - 1]}>', inline=False)
                counter += 1

        if counter <= 25 and counter > 0:
            await ctx.send(embed=embed)
        elif counter <= 50 and counter > 0:
            await ctx.send(embed=embed2)

        elif member.name == ctx.message.author.name:
            await ctx.send(
                f'<@{ctx.message.author.id}> lista ta de prieteni este goală, folosește comanda `addfriend` pentru a-ți face niște prieteni, dacă nu ai, pot fi eu prietena ta! <:owo:673946286726184967>')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> lista cerută este goală. :(')
        flist.close()


    @commands.command(pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def unfriend(self, ctx, member: discord.Member, *, mesaj = 'nimic'):
        flistread = open(f"ffriends/{ctx.message.author.name}_fid.txt", 'r')
        if os.path.exists(f'ffriends/{ctx.message.author.name}_fid.txt') and os.stat(
                f'ffriends/{ctx.message.author.name}_fid.txt').st_size != 0:
            flist = []
            counter = 0
            for friend in flistread:
                if friend[0:len(friend) - 1] != str(member.id):
                    counter += 1
                    flist.append(friend[0:len(friend) - 1])

            flistremove = open(f'ffriends/{ctx.message.author.name}_fid.txt', 'w')
            complete_list = 0
            while complete_list < counter:
                flistremove.write(f'{flist[complete_list]}\n')
                complete_list += 1
            flistremove.close()
            flistread.close()
            if member == self.client.user:
                await ctx.send(
                    f'<@{ctx.message.author.id}> Îmi pare rău, este vina mea, trebuia să fiu o prietenă mai bună. <:sadgirl:686479523356868616>\nAcum ai {50 - counter} de sloturi libere.')
            else:
                await ctx.send(
                    f'<@{ctx.message.author.id}> tu și **{member.name}** nu mai sunteți prieteni de acum, păcat, erați prieteni buni. <:sadgirl:686479523356868616>\nAcum ai {50 - counter} de sloturi libere.')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> lista ta de prieteni este deja goală.')

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context = True)
    async def marry(self, ctx, member: discord.Member, *, mesaj = 'nimic'):
        if ctx.message.author.id == member.id:
            await ctx.send(f'<@{ctx.message.author.id}> nu credeam că trebuie să spun asta, dar nu, nu te poți căsători cu tine.')
            return 0
        for filename in os.listdir('./mariaj'):
            if filename[0:-4] == str(ctx.message.author.id):
                autor = open(f'./mariaj/{filename}', 'r')
                partener = autor.readline()
                embed = discord.Embed(
                    color= discord.Color.dark_red()
                )
                embed.add_field(name= 'Nu poți face asta!', value=f'<@{ctx.message.author.id}> ești deja într-un mariaj cu <@{partener}>.', inline=True)
                await ctx.send(embed = embed)
                return 0
            elif filename[0:-4] == str(member.id):
                embed = discord.Embed(
                    color=discord.Color.dark_red()
                )
                embed.add_field(name='Nu poți face asta!',
                                value=f'<@{member.id}> este deja într-un mariaj fericit.',
                                inline=True)
                await ctx.send(embed=embed)
                return 0
        global propose
        if str(ctx.message.author.id) in propose:
            if propose[str(ctx.message.author.id)] == str(member.id):
                await ctx.send(f'<@{ctx.message.author.id}> ai cerut deja în căsătorie pe **{member.name}**, așteaptă să răspundă.')
                return 0
        else:
            propose[str(ctx.message.author.id)] = str(member.id)
        if str(member.id) in propose:
            if propose[str(member.id)] == str(ctx.message.author.id):
                embed = discord.Embed(
                    color= discord.Color.dark_purple(),
                    title= f'{ctx.message.author.name} a acceptat cererea în căsătorie a utilizatorului {member.name}! <:excitedumb:695989215229509703>'
                )
                embed.set_image(url= 'https://media3.giphy.com/media/CPfekkxmfU5Gg/source.gif')
                embed.set_author(name= f'Mesajul de accept: {mesaj}')
                await ctx.send(embed = embed)
                embed2 = discord.Embed(
                    color= discord.Color.dark_purple(),
                    title= f'De acum {ctx.message.author.name} și {member.name} sunt căsătoriți! <:cryingkiss:695989215283904522>'
                )
                embed2.set_image(url= 'https://data.whicdn.com/images/41116961/original.gif')
                await ctx.send(embed=embed2)
                propose.pop(str(ctx.message.author.id))
                propose.pop(str(member.id))
                partner1 = open(f'mariaj/{str(ctx.message.author.id)}.txt', 'a')
                partner2 = open(f'mariaj/{str(member.id)}.txt', 'a')
                partner1.write(f'{str(member.id)}')
                partner2.write(f'{str(ctx.message.author.id)}')
                partner1.close()
                partner2.close()
                return 0
        else:
            embed = discord.Embed(
                color=discord.Color.dark_purple(),
                title=f'{ctx.message.author.name} a cerut în căsătorie pe utilizatorul {member.name}! <:startheart:695256837317984298>'
            )
            embed.set_image(url='https://gifimage.net/wp-content/uploads/2017/09/anime-romance-gif-2.gif')
            embed.set_author(name=f'Mesajul de cerere: {mesaj}')
            await ctx.send(embed=embed)

    @commands.cooldown(1,10, commands.BucketType.user)
    @commands.command(pass_context = True)
    async def divorce(self, ctx, *, mesaj = 'nimic'):
        if os.path.exists(f'mariaj/{str(ctx.message.author.id)}.txt'):
            partner1 = open(f'mariaj/{str(ctx.message.author.id)}.txt','r')
            partner2id = str(partner1.readline())
            embed = discord.Embed(
                color = discord.Color.dark_purple()
            )
            embed.add_field(name='Divorț efectuat.', value= f'<@{ctx.message.author.id}> a divorțat de <@{partner2id}>, păcat, le stătea bine.\nCu un motiv bun: {mesaj}', inline= False)
            partner1.close()
            os.remove(f'mariaj/{str(ctx.message.author.id)}.txt')
            os.remove(f'mariaj/{partner2id}.txt')
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'<@{ctx.message.author.id}> nu poți divorța nefiind căsătorit.')

    @commands.command(pass_context = True)
    async def marrylist(self, ctx):
        allpartners = {}
        for filename in os.listdir('./mariaj'):
            partner = open(f'mariaj/{filename}','r')
            partner2 = str(partner.readline())
            partner.close()
            if not partner2 in allpartners:
                allpartners[str(filename[0:-4])] = partner2
        counter = int(0)
        for x in allpartners:
            counter += 1
        embed = discord.Embed(
            color= discord.Color.magenta(),
            description= f'Total: {counter}',
            title= f'Lista fericitelor cupluri:'
        )
        counter = int(0)
        for x in allpartners:
            embed.add_field(name=f'{counter + 1}',value=f'<@{x}> x <@{allpartners[x]}>', inline= False)
            counter += 1
        await ctx.send(embed=embed)

    @divorce.error
    async def divorce_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'<@{ctx.message.author.id}> a apărut o eroare necunoscută, te rog să o raportezi.')

    @marry.error
    async def marry_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `marry` este în cooldown pentru încă {int(error.retry_after)}s.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> trebuie să specifici partenerul.')
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> nu cunosc acea persoană.')

    @unfriend.error
    async def unfriend_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `unfriend` este în cooldown pentru încă {int(error.retry_after)}s.')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> cine nu-ți mai este prieten?')
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> asigură-te că îi scrii numele cum trebuie.')


    @friendlist.error
    async def friendlist_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `friendlist` este în cooldown pentru încă {int(error.retry_after)}s.')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'<@{ctx.message.author.id}> acea persoană nu are o listă de prieteni.')
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> asigură-te că îi scrii numele cum trebuie sau se va supăra.')
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> lista cui?')


    @resetfriendlist.error
    async def resetfriendlist_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> comanda `resetfriendlist` este în cooldown pentru încă {int(error.retry_after)}s.')


    @addfriend.error
    async def addfriend_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(
                f'<@{ctx.message.author.id}> comanda `addfriend` este în cooldown pentru încă {int(error.retry_after)}s. Prietenii nu se fac așa rapid.')
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> trebuie să precizezi o persoană.')
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> asigură-te că scrii corect numele noului tău prieten.')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'<@{ctx.message.author.id}> numele prietenului tău conține unicode.')


def setup(client):
    client.add_cog(Social(client))