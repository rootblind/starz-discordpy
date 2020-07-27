
import random
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import time
import os

lolroid = int(527143176415477770)
roppid = int(625737079187439638)

pickEmoji = ['<:yo:673946322050744341>', '<:uwu:626392514844295168>', '<:sipp_tea:673904944377495582>',
             '<:princessuwu:673946318040727586>', '<:owo:673946286726184967>', '<:kannasipp:671957156467310631>', '<:gnargnaw:690194560055509033>', ':purple_heart:', ':heart:']

pickActivity = ['the stars.', 'a comet.', 'the dark stars.', 'black holes.', 'over yuwu.', 'distant galaxies fading away.', 'Blind while coding me.',
                'the Universe getting old.', 'Youjo Senki.', 'RATIRL\'s stream.', 'my favorite anime.', 'cats on YouTube.', 'the screen all day and night.','some memes.']

msgCount = 1
client = commands.Bot(command_prefix = ",")
client.remove_command("help")


def im_owner(ctx):
    return ctx.message.author.id == 224131162996473856

@client.event
async def on_disconnect():
    print("Starz#8096 has been disconnected!")



@client.event
async def on_ready():
    global pickActivity
    activity = discord.Activity(name= random.choice(pickActivity), type=discord.ActivityType.watching)
    await client.change_presence(status = discord.Status.online,
                                 activity = activity)
    print("Logged on Starz#8096")




cooldownMsg = 0
@client.event
async def on_message(message):
    global cooldownMsg
    global msgCount
    if msgCount % 50 == 0:
        activity = discord.Activity(name=random.choice(pickActivity), type=discord.ActivityType.watching)
        await client.change_presence(status=discord.Status.online,
                                     activity=activity)
    if message.author == client.user or message.author.bot:
        return 0

    if isinstance(message.channel, discord.DMChannel):
        return 0
    original_message = message.content
    message.content = message.content.lower()
    try:
        if message.content.startswith('noapte buna') or message.content.startswith("nb") or message.content.startswith("somn usor") or message.content.startswith("gn"):
            if cooldownMsg == 0:
                pickGn = ['Somn ușor și vise plăcute! {0}'.format(random.choice(pickEmoji)),
                          'Noapte bună! {0}'.format(random.choice(pickEmoji)),
                          'Să dormi bine, vreau să ne vedem mâine zâmbind. {0}'.format(random.choice(pickEmoji)),
                          'Nb, pwp! {0}'.format(random.choice(pickEmoji))
                          ]
                await message.channel.send(random.choice(pickGn))
                cooldownMsg = time.time()
            elif time.time() - cooldownMsg >= 15:
                cooldownMsg = 0
    except:
        return 0
    message.content = original_message
    msgCount += 1
    await client.process_commands(message)

@commands.command(pass_context=True)
@commands.check(im_owner)
async def reloado(ctx):
    client.unload_extension(f'cogs.owner')
    client.load_extension(f'cogs.owner')
    await ctx.send(f'```Owner reloaded.```')
client.add_command(reloado)


@reloado.error
async def reloado_error(ctx, error):
   if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(f'<@{ctx.message.author.id}> doar Blind poate folosi acea comandă.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f'Nah, nu cred că o să fac aia.')
        return 0
    raise error


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("NTU2NjQ3Mzk5MDQ1NTk1MTM2.Xjx_YA.9BL6BfP1bvKac8xk1WH9KCHRsYM")