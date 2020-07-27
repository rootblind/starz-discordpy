import discord
from discord.ext import commands
import os

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name = 'commands', aliases = ['c','cmd','comenzi'])
    async def command(self, ctx):
        casualList = discord.Embed(
            title = "Modulul Casual:",
            color=discord.Color.red()
        )
        socialList = discord.Embed(
            title="Modulul Social:",
            color=discord.Color.orange()
        )
        economyList = discord.Embed(
            title="Modulul Economy:",
            color=discord.Color.gold()
        )
        gamesList = discord.Embed(
            title="Modulul Games:",
            color=discord.Color.green()
        )
        imagesList = discord.Embed(
            title="Modulul Images:",
            color= discord.Color.blue()
        )
        modList = discord.Embed(
            title="Modulul Mod:",
            color= discord.Color.magenta()
        )
        ownerList  = discord.Embed(
            title="Modulul Owner:",
            color= discord.Color.purple()
        )
        helpList = discord.Embed(
            title = "Modulul Commands:"
        )

        helpList.add_field(name='cmd', value='Afișează toate comenzile.', inline=False)
        helpList.add_field(name='help <modul>', value='Afișează toate comenzile unui modul.', inline=False)

        casualList.add_field(name = 'echo <text>', value = 'Trimite un mesaj sub identitatea mea.', inline = False)
        casualList.add_field(name = 'loverate <persoana 1> [persoana 2]', value = 'Măsoară cât de bine se înțeleg 2 persoane.', inline = False)
        casualList.add_field(name='ping', value='Conexiunea mea la internet.', inline=False)
        casualList.add_field(name='reminder <text>', value='Îți voi da un mesaj în DMs ca să nu uiți.', inline=False)
        casualList.add_field(name='ship <text 1> <text 2>', value='Numele cuplului format din cele 2 persoane precizate.', inline=False)

        economyList.add_field(name='balance [persoana]', value='Se va afișa balanța cuiva.', inline=False)
        economyList.add_field(name='daily', value='Obține un bonus zilnic de bani egal cu 100 + 5% din balanța ta.', inline=False)
        economyList.add_field(name='pay <persoana> [suma default = 10]', value='Plătește pe cineva o sumă specificată.', inline=False)

        gamesList.add_field(name='atacc <persoana>', value='Atacă pe cineva într-o luptă.', inline=False)
        gamesList.add_field(name='protecc [persoana]', value='Protejează pe cineva oferindu-i viață.', inline=False)
        gamesList.add_field(name='dance [join/stop]', value='Ia parte la un e-party sau încheie-l dacă tu l-ai început.', inline=False)
        gamesList.add_field(name='doors <1/2/3/4> [suma pariată default = 10]', value='Alege un număr de la 1 la 4 și pariază o sumă.', inline=False)
        gamesList.add_field(name='barbut', value='Dai cu zaru', inline=False)

        imagesList.add_field(name='avatar [persoana]', value='Afișează avatarul actual al cuiva.', inline=False)
        imagesList.add_field(name='animegirl', value='Imagini de pe reddit cu fete anime.', inline=False)
        imagesList.add_field(name='cats', value='Imagini de pe reddit cu pisici.', inline=False)
        imagesList.add_field(name='dogs', value='Imagini de pe reddit cu câini.', inline=False)
        imagesList.add_field(name='cmemes', value='Meme-uri de pe reddit cu matematică.', inline=False)
        imagesList.add_field(name='pmemes', value='Meme-uri de pe reddit cu programare.', inline=False)
        imagesList.add_field(name='memes', value='Meme-uri de pe reddit.', inline=False)
        imagesList.add_field(name='earthporn', value='Imagini de pe reddit cu planeta noastră.', inline=False)
        imagesList.add_field(name='foodporn', value='Imagini de pe reddit cu mâncare.', inline=False)
        imagesList.add_field(name='cry [persoana]', value='Cineva te face să plângi.', inline=False)
        imagesList.add_field(name='hug [persoana]', value='Ia în brațe pe cineva.', inline=False)
        imagesList.add_field(name='kiss [persoana]', value='Sărută pe cineva.', inline=False)
        imagesList.add_field(name='slap [persoana]', value='Pălmuiește pe cineva.', inline=False)

        modList.add_field(name='ban <persoana> [motivul]', value='Elimină permanent un membru de pe server.', inline=False)
        modList.add_field(name='clear [numar]', value='Șterge ultimele N mesaje.', inline=False)

        ownerList.add_field(name='allmodules', value='Afișează toate modulele încărcate.', inline=False)
        ownerList.add_field(name='load <modul>', value='Încarcă un modul dezactivat.', inline=False)
        ownerList.add_field(name='unload <modul>', value='Dezactivează un modul încărcat.', inline=False)
        ownerList.add_field(name='reload <modul>', value='Reîncarcă un modul încărcat.', inline=False)
        ownerList.add_field(name='reloadall <modul>', value='Reîncarcă toate modulele, dacă sunt toate încărcate.', inline=False)
        ownerList.add_field(name='reloado', value='Reîncarcă modulul owner.', inline=False)

        socialList.add_field(name='addfriend <persoana>', value='Adaugă o persoană în lista ta de prieteni.', inline=False)
        socialList.add_field(name='unfriend <persoana>', value='Elimină o persoană din lista ta de prienei.', inline=False)
        socialList.add_field(name='friendlist [persoana]', value='Afișează lista de prieteni a cuiva.', inline=False)
        socialList.add_field(name='resetfriendlist', value='Golește-ți lista de prieteni.', inline=False)
        socialList.add_field(name='marry <persoana> [text]', value='Cere în căsătorie pe cineva.', inline=False)
        socialList.add_field(name='marrylist', value='Afișează toate căsătoriile actuale.', inline=False)
        socialList.add_field(name='divorce [text]', value='Divorțează, ai grijă să iei copiii că să primești alocația și pensia.', inline=False)

        await ctx.send(f'```<parametru obligatoriu>\n[parametru opțional]```')
        await ctx.send(embed = casualList)
        await ctx.send(embed=socialList)
        await ctx.send(embed=economyList)
        await ctx.send(embed=gamesList)
        await ctx.send(embed=imagesList)
        await ctx.send(embed=modList)
        await ctx.send(embed=ownerList)
        await ctx.send(embed = helpList)

    @commands.command(pass_context=True)
    async def help(self, ctx, modul):
        modul = modul.lower()
        modules = []
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                modules.append(f'{filename[:-3]}')
        if modul not in modules:
            await ctx.send(f'<@{ctx.message.author.id}> nu am un astfel de modul!\nFolosește `,c` pentru a vedea toate modulele.')
            return

        if modul == 'casual':
            casualList = discord.Embed(
                title="Modulul Casual:",
                color=discord.Color.red()
            )
            casualList.add_field(name='echo <text>', value='Trimite un mesaj sub identitatea mea.', inline=False)
            casualList.add_field(name='loverate <persoana 1> [persoana 2]',
                                 value='Măsoară cât de bine se înțeleg 2 persoane.', inline=False)
            casualList.add_field(name='ping', value='Conexiunea mea la internet.', inline=False)
            casualList.add_field(name='reminder <text>', value='Îți voi da un mesaj în DMs ca să nu uiți.',
                                 inline=False)
            casualList.add_field(name='ship <text 1> <text 2>',
                                 value='Numele cuplului format din cele 2 persoane precizate.', inline=False)
            await ctx.send(embed=casualList)
        elif modul == 'social':
            socialList = discord.Embed(
                title="Modulul Social:",
                color=discord.Color.orange()
            )
            socialList.add_field(name='addfriend <persoana>', value='Adaugă o persoană în lista ta de prieteni.',
                                 inline=False)
            socialList.add_field(name='unfriend <persoana>', value='Elimină o persoană din lista ta de prienei.',
                                 inline=False)
            socialList.add_field(name='friendlist [persoana]', value='Afișează lista de prieteni a cuiva.',
                                 inline=False)
            socialList.add_field(name='resetfriendlist', value='Golește-ți lista de prieteni.', inline=False)
            socialList.add_field(name='marry <persoana> [text]', value='Cere în căsătorie pe cineva.', inline=False)
            socialList.add_field(name='marrylist', value='Afișează toate căsătoriile actuale.', inline=False)
            socialList.add_field(name='divorce [text]',
                                 value='Divorțează, ai grijă să iei copiii că să primești alocația și pensia.',
                                 inline=False)
            await ctx.send(embed=socialList)
        elif modul == 'economy':
            economyList = discord.Embed(
                title="Modulul Economy:",
                color=discord.Color.gold()
            )
            economyList.add_field(name='balance [persoana]', value='Se va afișa balanța cuiva.', inline=False)
            economyList.add_field(name='daily', value='Obține un bonus zilnic de bani egal cu 100 + 5% din balanța ta.',
                                  inline=False)
            economyList.add_field(name='pay <persoana> [suma default = 10]',
                                  value='Plătește pe cineva o sumă specificată.', inline=False)
            await ctx.send(embed=economyList)
        elif modul == 'games':
            gamesList = discord.Embed(
                title="Modulul Games:",
                color=discord.Color.green()
            )
            gamesList.add_field(name='atacc <persoana>', value='Atacă pe cineva într-o luptă.', inline=False)
            gamesList.add_field(name='protecc [persoana]', value='Protejează pe cineva oferindu-i viață.', inline=False)
            gamesList.add_field(name='dance [join/stop]',
                                value='Ia parte la un e-party sau încheie-l dacă tu l-ai început.', inline=False)
            gamesList.add_field(name='doors <1/2/3/4> [suma pariată default = 10]',
                                value='Alege un număr de la 1 la 4 și pariază o sumă.', inline=False)
            gamesList.add_field(name='barbut', value='Dai cu zaru', inline=False)
            await ctx.send(embed=gamesList)
        elif modul == 'images':
            imagesList = discord.Embed(
                title="Modulul Images:",
                color=discord.Color.blue()
            )
            imagesList.add_field(name='avatar [persoana]', value='Afișează avatarul actual al cuiva.', inline=False)
            imagesList.add_field(name='animegirl', value='Imagini de pe reddit cu fete anime.', inline=False)
            imagesList.add_field(name='cats', value='Imagini de pe reddit cu pisici.', inline=False)
            imagesList.add_field(name='dogs', value='Imagini de pe reddit cu câini.', inline=False)
            imagesList.add_field(name='cmemes', value='Meme-uri de pe reddit cu matematică.', inline=False)
            imagesList.add_field(name='pmemes', value='Meme-uri de pe reddit cu programare.', inline=False)
            imagesList.add_field(name='memes', value='Meme-uri de pe reddit.', inline=False)
            imagesList.add_field(name='earthporn', value='Imagini de pe reddit cu planeta noastră.', inline=False)
            imagesList.add_field(name='foodporn', value='Imagini de pe reddit cu mâncare.', inline=False)
            imagesList.add_field(name='cry [persoana]', value='Cineva te face să plângi.', inline=False)
            imagesList.add_field(name='hug [persoana]', value='Ia în brațe pe cineva.', inline=False)
            imagesList.add_field(name='kiss [persoana]', value='Sărută pe cineva.', inline=False)
            imagesList.add_field(name='slap [persoana]', value='Pălmuiește pe cineva.', inline=False)
            await ctx.send(embed=imagesList)
        elif modul == 'mod':
            modList = discord.Embed(
                title="Modulul Mod:",
                color=discord.Color.magenta()
            )
            modList.add_field(name='ban <persoana> [motivul]', value='Elimină permanent un membru de pe server.',
                              inline=False)
            modList.add_field(name='clear [numar]', value='Șterge ultimele N mesaje.', inline=False)
            await ctx.send(embed=modList)
        elif modul == '':
            ownerList = discord.Embed(
                title="Modulul Owner:",
                color=discord.Color.purple()
            )
            ownerList.add_field(name='allmodules', value='Afișează toate modulele încărcate.', inline=False)
            ownerList.add_field(name='load <modul>', value='Încarcă un modul dezactivat.', inline=False)
            ownerList.add_field(name='unload <modul>', value='Dezactivează un modul încărcat.', inline=False)
            ownerList.add_field(name='reload <modul>', value='Reîncarcă un modul încărcat.', inline=False)
            ownerList.add_field(name='reloadall <modul>', value='Reîncarcă toate modulele, dacă sunt toate încărcate.',
                                inline=False)
            ownerList.add_field(name='reloado', value='Reîncarcă modulul owner.', inline=False)
            await ctx.send(embed=ownerList)
        else:
            helpList = discord.Embed(
                title="Modulul Commands:"
            )

            helpList.add_field(name='cmd', value='Afișează toate comenzile.', inline=False)
            helpList.add_field(name='help <modul>', value='Afișează toate comenzile unui modul.', inline=False)
            await ctx.send(embed=helpList)











def setup(client):
    client.add_cog(Commands(client))
