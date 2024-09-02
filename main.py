import discord
from discord.ext import commands
import os
from random import choice

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

images_meme = os.listdir("images/IT")
util = {'пластик': ["Промойте и просушите", "Удалите этикетки и избавьтесь от крышек", "Сомните бутылку, чтобы она занимала меньше места и откладывайте пластик дома (не выбрасывать!)", "Накопленный пластик отнесите в точку сбора вторсырья."], 
        'алюминий': ["Сожмите банку – так она займет меньше места у вас дома и на свалке", "Утилизируйте её в ближайший контейнер для алюминия"]}
decays = {'пластик': "450 лет в общем",
          'алюминий': "более 500 лет",
          'жвачка': "от 30 до 50 лет зависит от климата"}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="Стримы Bobrickusa")
    if channel:
        await channel.send(f"{member.mention} вступил в канал")
    else:
        print("Канала нет")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def delete(ctx, member: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await member.kick()
        await ctx.send(f'{member.name} был удалён')
    else:
        await ctx.send("у вас нет прав админитстратора")

@bot.command()
async def meme(ctx, theme = "", meme_num = 0):
    if theme.lower() == "it":
        if 1 <= meme_num <= len(images_meme):
            with open(f"images/IT/{images_meme[meme_num - 1]}", "rb") as f:
                await ctx.send(file = discord.File(f)) 
        else:
            await ctx.send("Рандом")
            with open(f"images/IT/{choice(images_meme)}", "rb") as f:
                await ctx.send(file = discord.File(f))        
    else:
        await ctx.send("Такой темы не существует")
@bot.command()
async def disposal(ctx, resource = ""):
    if resource.lower() in util:
        for i in util[resource.lower()]:
            await ctx.send(i)
    elif resource == "":
        await ctx.send("Напишите что должно быть утилизировано")
    else:
        await ctx.send("Утилизируется в обычный контейнер")
@bot.command()
async def decay(ctx, resource = ""):
    if resource.lower() in decays:
        await ctx.send(f"{resource.lower()} разлагается {decays[resource.lower()]}")
    else:
        await ctx.send("Предмет не указан")




bot.run("your token")