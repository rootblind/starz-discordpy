import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import time
import os

payment = {}

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.client == message.author or message.author.bot:
            return 0
        if not str(message.author.id) in payment:
            payment[str(message.author.id)] = int(1)
        else:
            payment[str(message.author.id)] += 1
        if payment[str(message.author.id)] % 20 == 0:
            if os.path.exists(f'./economy/{message.author.id}.txt'):
                useradd = open(f'economy/{message.author.id}.txt','r')
                x = int(useradd.read())
                x += 5
                usermoney = open(f'economy/{message.author.id}.txt','w')
                usermoney.write(str(int(x)))
                usermoney.close()
            else:
                usermoney = open(f'economy/{str(message.author.id)}.txt', 'a')
                usermoney.write(str(int(5)))
                usermoney.close()

    @commands.command(pass_context = True)
    async def balance(self, ctx, member: discord.Member = 'nimeni'):
        if member == 'nimeni':
            member = ctx.message.author

        if os.path.exists(f'./economy/{member.id}.txt'):
            usermoney = open(f'economy/{member.id}.txt', 'r')
        else:
            usermoney = open(f'economy/{member.id}.txt', 'a')
            usermoney.write(str(0))
            usermoney.close()
            usermoney = open(f'economy/{member.id}.txt', 'r')

        moneyCount = usermoney.read()
        usermoney.close()
        if member == ctx.message.author:
            titlu = f'Balanța ta:  {moneyCount} <:python:694344808533327875>'
        else:
            titlu = f'Balanța utilizatorului {member.name}:  {moneyCount} <:python:694344808533327875>'
        embed = discord.Embed(
            color= discord.Color.green(),
            title= titlu
        )
        embed.set_image(url='https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024"'.format(member))
        await ctx.send(embed=embed)

    @commands.command(pass_context = True)
    async def pay(self, ctx, member: discord.Member, ammount = '10'):
        if int(ammount) < 10:
            await ctx.send(f'<@{ctx.message.author.id}> valoarea minimă de plată este de 10 <:python:694344808533327875>')
            return 0
        if member == ctx.message.author:
            await ctx.send(f'<@{ctx.message.author.id}> nu te poți plăti singur, dacă chiar vrei sa faci asta, imaginează-ti că merge.  <:idk:671957075496140810>')
            return 0

        if os.path.exists(f'./economy/{member.id}.txt'):
            recieverRead = open(f'economy/{member.id}.txt', 'r')
        else:
            recieverWrite = open(f'economy/{member.id}.txt', 'a')
            recieverWrite.write(str(0))
            recieverWrite.close()
            recieverRead = open(f'economy/{member.id}.txt', 'r')

        if os.path.exists(f'./economy/{ctx.message.author.id}.txt'):
            senderRead = open(f'economy/{ctx.message.author.id}.txt', 'r')
        else:
            senderWrite = open(f'economy/{ctx.message.author.id}.txt', 'a')
            senderWrite.write(str(0))
            senderWrite.close()
            senderRead = open(f'economy/{ctx.message.author.id}.txt', 'r')

        senderValue = senderRead.read()
        recieverValue = recieverRead.read()
        senderRead.close()
        recieverRead.close()

        if int(ammount) > int(senderValue):
            await ctx.send(f'<@{ctx.message.author.id}> Valoare introdusă o depășește pe cea deținută.')
            return 0

        recieverWrite = open(f'economy/{member.id}.txt','w')
        recieverWrite.write(str(int(ammount) + int(recieverValue)))
        recieverWrite.close()
        senderWrite = open(f'economy/{ctx.message.author.id}.txt','w')
        senderWrite.write(str(int(senderValue) - int(ammount)))
        senderWrite.close()

        embed = discord.Embed(
            color= discord.Color.green(),
            title= f'Utilizatorul {member.name} a primit {ammount} <:python:694344808533327875> de la {ctx.message.author.name}.'
        )

        await ctx.send(embed=embed)

    @commands.cooldown(1, 36000, commands.BucketType.user)
    @commands.command()
    async def daily(self, ctx):
        if os.path.exists(f'./economy/{ctx.message.author.id}.txt'):
            authorBalance = open(f'economy/{ctx.message.author.id}.txt','r')
        else:
            authorBalance = open(f'economy/{ctx.message.author.id}.txt', 'a')
            authorBalance.write(str(0))
            authorBalance.close()
            authorBalance = open(f'economy/{ctx.message.author.id}.txt', 'r')

        balance = authorBalance.read()
        authorBalance.close()
        reward = 100 + int(0.05 * int(balance))

        embed = discord.Embed(
            color= discord.Color.green(),
            title= f'{ctx.message.author.name} și-a colectat plata zilnică. <:joker:671090294954917938> Valoare: {reward} <:python:694344808533327875>\nBalanța: {int(balance) + int(reward)} <:python:694344808533327875>'
        )

        authorBalance = open(f'economy/{ctx.message.author.id}.txt', 'w')
        authorBalance.write(str(int(balance) + int(reward)))
        authorBalance.close()

        await ctx.send(embed=embed)

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f'<@{ctx.message.author.id}> poți colecta plata zilnică odată la 10 ore. Timp rămas: {int(error.retry_after / 60)}m și {int(error.retry_after % 60)}s')

    @pay.error
    async def pay_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> argumentul introdus este invalid.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> sintaxa comenzii: `,pay <membru> <număr>`.')

    @balance.error
    async def balance_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> numele introdus este greșit sau nu există.')

def setup(client):
    client.add_cog(Economy(client))