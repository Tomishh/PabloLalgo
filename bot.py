import asyncio
import discord
import time
import random
from discord.ext import commands


file= open("token.txt","r") #create a txt file with the discord bot token inside
token= file.read()
client = discord.Client()
bot = commands.Bot(command_prefix="r!")


@bot.event
async def on_ready():
    print("Bot is ready for use.") #cmd indication

    await bot.change_presence(activity=discord.Game(name="r!help", type=0)) #bot description

@bot.command(pass_contexte=True) 
async def test(ctx, arg): 
    await ctx.send(arg)

@bot.command(pass_contexte=True) #command for test the bot
async def hi(ctx):
    await ctx.send("Hello !")

@bot.command(pass_contexte=True) #command for ping yourself
async def tag(ctx):
    id=ctx.message.author.id
    tagged_id="<@%s>"% id
    await ctx.send(tagged_id)

@bot.command(pass_contexte=True) #command with delay before ping
async def remind_me(ctx,arg):
    await ctx.send("Je vous ping dans %s secondes" % arg)
    sec=int(arg)
    time.sleep(sec)
    id=ctx.message.author.id
    tagged_id="<@%s>"% id
    await ctx.send(tagged_id)

@bot.command(pass_contexte=True) #command for run a D20
async def d20(ctx):
 await ctx.send("C'est l'heure de jouer ! :game_die:")
 time.sleep(3)
 nombre = random.randint(1, 20)
 if nombre == 1:
    await ctx.send("Aie, echec critique ! Le dé est tombé sur %s" %nombre )
 if nombre == 20:
    await ctx.send("Et c'est une réussite critique !  Le dé est tombé sur %s" %nombre)
 else:
     await ctx.send("Le dé est tombé sur le %s" %nombre)


@bot.command(pass_contexte=True) #command with delay before ping
async def d(ctx,faces):
    await ctx.send("Et c'est parti pour un dé à %s faces ! :game_die:" % faces)
    time.sleep(2)
    nbr_faces=int(faces)
    nombre=random.randint(1,nbr_faces)
    if nombre == 1 :
        await ctx.send("Aie, echec critique ! Le dé est tombé sur %s" %nombre )
    if nombre == faces :
        await ctx.send("Et c'est une réussite critique !  Le dé est tombé sur %s" %nombre)
    else:
     await ctx.send("Le dé est tombé sur le %s" %nombre)


bot.run(token)
random.seed(1)
