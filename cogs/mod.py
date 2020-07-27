import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import time

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members = True)
    async def clear(self, ctx, amount = 1):
        amount = int(amount)
        if amount < 0:
            amount = - amount
        if amount == 0:
            amount = 1
        await ctx.channel.purge(limit=amount + 1)


    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member.guild_permissions.ban_members or member.bot:
            await ctx.send(f'<@{ctx.message.author.id}> nu poți elimina un moderator!')
            return 0
        embed = discord.Embed(
            title= f'Motivul: {reason}',
            colour=discord.Color.red()
        )

        embed.set_author(name= f'{member.name} has been banned by {ctx.message.author.name}', icon_url= 'https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(member))
        embed.set_image(url= 'https://i.pinimg.com/originals/3d/d0/05/3dd005f01a920d354b42930a52a65017.gif')
        await ctx.send(embed=embed)
        await member.ban(reason=reason)


    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'<@{ctx.message.author.id}> nu ești în măsură să-mi spui ce sa fac! <:angrystar:673946308842618910>')
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> uh, acela nu este un număr.')


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'<@{ctx.message.author.id}> nu ești în măsură să-mi spui ce sa fac! <:angrystar:673946308842618910>')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'<@{ctx.message.author.id}> ideea este că am nevoie de o victimă.')
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f'<@{ctx.message.author.id}> {ctx.message.content[4:]}? Nu avem niciun {ctx.message.content[5:]}.')
    
def setup(client):
    client.add_cog(Mod(client))
