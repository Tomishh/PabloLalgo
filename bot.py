import asyncio
from typing import ValuesView
import discord
import time
import random
from discord.ext import commands
import requests
import json
import threading

file= open("token.txt","r") #create a txt file with the discord bot token inside
token= file.read()
client = discord.Client()
bot = commands.Bot(command_prefix="r!")





async def printawait(time):
    while True:
        print("hello")
        await asyncio.sleep(time)



@bot.command(pass_contexte=True) 
async def test(ctx, arg): 
    await ctx.send(arg)

@bot.command(pass_contexte=True) #command for test the bot
async def hi(ctx):
    await ctx.send(f"Hello !")

@bot.command(pass_contexte=True) #command for ping yourself
async def tag(ctx):
    id=ctx.message.author.id
    tagged_id="<@%s>"% id
    await ctx.send(tagged_id)

@bot.command(pass_contexte=True) #command with delay before ping
async def remind_me(ctx,arg):
    await ctx.send(f"Je vous ping dans {arg} secondes")
    sec=int(arg)
    time.sleep(sec)
    id=ctx.message.author.id
    tagged_id="<@%s>"% id
    await ctx.send(tagged_id)

@bot.command(pass_contexte=True) #command for run a D20
async def d20(ctx):
 await ctx.send(f"C'est l'heure de jouer ! :game_die:")
 time.sleep(3)
 nombre = random.randint(1, 20)
 if nombre == 1:
    await ctx.send(f"Aie, echec critique ! Le dé est tombé sur {nombre}")
 if nombre == 20:
    await ctx.send(f"Et c'est une réussite critique !  Le dé est tombé sur {nombre}")
 else:
     await ctx.send(f"Le dé est tombé sur le {nombre}")


@bot.command(pass_contexte=True) #command for run a x die
async def d(ctx,faces):
    await ctx.send(f"Et c'est parti pour un dé à {faces} faces ! :game_die:")
    time.sleep(2)
    nbr_faces=int(faces)
    nombre=random.randint(1,nbr_faces)
    if nombre == 1 :
        await ctx.send(f"Aie, echec critique ! Le dé est tombé sur {nombre}")
    if nombre == nbr_faces :
        await ctx.send(f"Et c'est une réussite critique !  Le dé est tombé sur {nombre}")
    else:
     await ctx.send(f"Le dé est tombé sur le {nombre}")

@bot.command(pass_contexte=True) #Die duel
async def duel(ctx):
    await ctx.send(f"C'est l'heure du Du-du-du-duel !")
    nbr_faces = 20
    id=ctx.message.author.mention
    tagged_id= "%s"% id
    id_guest = ctx.message.mentions[0].mention
    tagged_id_guest="%s"% id_guest

    time.sleep(1)

    # Dice for the author of the command.
    nombre=random.randint(1,nbr_faces)
    if nombre == 1 :
       await ctx.send(f"Aie, echec critique ! Le dé de {tagged_id} est tombé sur {nombre} :grimacing:")
    if nombre == nbr_faces :
        await ctx.send(f"Et c'est une réussite critique !  Le dé de {tagged_id} est tombé sur {nombre} :sparkles:")
    else:
     await ctx.send(f"Le dé de {tagged_id} est tombé sur le {nombre} ")

    time.sleep(1)

    # Dice for the guest 
    nombre_guest=random.randint(1,nbr_faces)
    if nombre_guest == 1 :
       await ctx.send(f"Aie, echec critique ! Le dé de {tagged_id_guest} est tombé sur {nombre_guest} :grimacing:")
    if nombre_guest == nbr_faces :
        await ctx.send(f"Et c'est une réussite critique !  Le dé de {tagged_id_guest} est tombé sur {nombre_guest} :sparkles:")
    else:
     await ctx.send(f"Le dé de {tagged_id_guest} est tombé sur le {nombre_guest}")


@bot.command(pass_contexte=True) #show hour lines
async def tram3(ctx):
    await ctx.send("test")
    heure_min =24
    minute_min =60 
    seconde_min =60
    with open('data_backup.txt') as json_file:
        data = json.load(json_file)
    print(data)
    for i in data:
        if i['fields']['numero_arret_stop_id'] == '1108141' and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
            await ctx.send(i['fields']['horaire_arrivee_theorique'])
            stringtemp=i['fields']['horaire_arrivee_theorique']
            array= stringtemp.split(':')
            heure= array[0]
            await ctx.send(heure)
            minute= array[1]
            await ctx.send(minute)
            seconde= array[2]
            await ctx.send(seconde)
            if heure < heure_min:
                heure_min = heure
                minute_min = minute
                seconde_min = seconde
            if heure == heure_min and minute < minute_min:
                heure_min = heure
                minute_min = minute
                seconde_min = seconde
            if heure == heure_min and minute == minute_min and seconde < seconde_min:
                heure_min = heure
                minute_min = minute
                seconde_min = seconde
    await ctx.send(f"Heure d'arrivé du tram le plus proche : {heure_min}:{minute_min}:{seconde_min}")


print("Bot Read to use :)")
bot.run(token)
random.seed(1)