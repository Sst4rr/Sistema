import discord
from discord.ext import commands

intents = discord.Intents.default()  # You can customize this based on your bot's needs
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

fichas = {} #dicionário com as fichas dos jogadores

class Ficha: #classe para criar as fichas
    def __init__(self, nome):
        self.nome = nome 
    

@bot.event  # Bot is ready
async def on_ready():
    print(f'{bot.user} has connected to Discord!')



@bot.comand()
async def criar_ficha(ctx):
    #código para criar uma ficha
    if ctx.author.id not in fichas:
        fichas[ctx.author.id] = Ficha(str(ctx.author))
        await ctx.send("Ficha criada com sucesso!")
    else:
        await ctx.send("Sua ficha já existe!")


@bot.comand()
async def ver_ficha(ctx):
    #código para visualizar a ficha 
    if ctx.author.id in fichas:
        ficha = fichas[ctx.author.id]
        await ctx.send(f"Sua ficha:\nNome: {ficha.nome}")
    else:
        await ctx.send("Você não tem ficha!")
# @bot.command()
# async def ping(ctx):
#     await ctx.send('Pong!')



bot.run('MTEzODE5OTk4MzMzNDYyMTIzNA.GXzRRa.tG8aIzrbJ3ZhqOXjcvbZxlDVUqLTVZCq9QSkS8   ')
