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

def heure_mini_fonc(liste_timing):
    h_min = 24
    min_min = 60
    sec_min = 60
    for i in liste_timing:
        liste_cut=liste_timing[i]
        array=liste_cut.split(':')
        heure=int(array[0])
        minute=int(array[1])
        seconde=int(array[2])
        if heure < h_min:
            h_min = heure
            min_min = minute
            sec_min = seconde
        if heure < h_min and minute < min_min :
            h_min = heure
            min_min = minute
            sec_min = seconde
        if  heure < h_min and minute < min_min and seconde < sec_min:
            h_min = heure
            min_min = minute
            sec_min = seconde
    string_min=f"{h_min}:{min_min}:{sec_min}"
    return string_min



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
 await ctx.send(f"C'est l'heure_arrive_clg de jouer ! :game_die:")
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
    await ctx.send(f"C'est l'heure_arrive_clg du Du-du-du-duel !")
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
    #Initialise the maximum date of the tram entry.
    heure_min_arrive_clg =24
    minute_min_arrive_clg =60 
    seconde_min_arrive_clg =60

    heure_min_depart_clg =24
    minute_min_depart_clg =60
    seconde_min_depart_clg=60

    with open('data.txt') as json_file:
        data = json.load(json_file)
        string_arrive = []
        string_depart = []
    for i in data:
        if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
            stringtemp_arrive_clg=i['fields']['horaire_arrivee_theorique']
            string_depart.append(stringtemp_arrive_clg)
            # array_arrive_clg= stringtemp_arrive_clg.split(':')
            # heure_arrive_clg= int(array_arrive_clg[0])
            # minute_arrive_clg= int(array_arrive_clg[1])
            # seconde_arrive_clg= int(array_arrive_clg[2])
            # if heure_arrive_clg < heure_min_arrive_clg:
            #     heure_min_arrive_clg = heure_arrive_clg
            #     minute_min_arrive_clg = minute_arrive_clg
            #     seconde_min_arrive_clg = seconde_arrive_clg
            # if heure_arrive_clg == heure_min_arrive_clg and minute_arrive_clg < minute_min_arrive_clg:
            #     heure_min_arrive_clg = heure_arrive_clg
            #     minute_min_arrive_clg = minute_arrive_clg
            #     seconde_min_arrive_clg = seconde_arrive_clg
            # if heure_arrive_clg == heure_min_arrive_clg and minute_arrive_clg == minute_min_arrive_clg and seconde_arrive_clg < seconde_min_arrive_clg:
            #     heure_min_arrive_clg = heure_arrive_clg
            #     minute_min_arrive_clg = minute_arrive_clg
            #     seconde_min_arrive_clg = seconde_arrive_clg

        if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'CAEN Ch\u00e2teau Quatrans':
            stringtemp_depart_clg=i['fields']['horaire_arrivee_theorique']
            # array_depart_clg = stringtemp_depart_clg.split(':')
            # heure_depart_clg = int(array_depart_clg[0])
            # minute_depart_clg = int(array_depart_clg[1])
            # seconde_depart_clg = int(array_depart_clg[2])
            # if heure_depart_clg < heure_min_depart_clg:
            #     heure_min_depart_clg=heure_depart_clg
            #     minute_min_depart_clg=minute_depart_clg
            #     seconde_min_depart_clg=seconde_depart_clg
            # if heure_depart_clg == heure_min_depart_clg and minute_depart_clg < minute_min_depart_clg:
            #     heure_min_depart_clg=heure_depart_clg
            #     minute_min_depart_clg=minute_depart_clg
            #     seconde_min_depart_clg=seconde_depart_clg
            # if heure_depart_clg == heure_min_depart_clg and minute_depart_clg == minute_min_depart_clg and seconde_depart_clg < seconde_min_depart_clg:
            #     heure_min_depart_clg=heure_depart_clg
            #     minute_min_depart_clg=minute_depart_clg
            #     seconde_min_depart_clg=seconde_depart_clg
        await ctx.send(heure_mini_fonc(string_depart))
        await ctx.send(string_depart)


    await ctx.send(f"Le prochaine tram en provenance de Chateau Quatran arrivera à {heure_min_arrive_clg}:{minute_min_arrive_clg}:{seconde_min_arrive_clg} et le prochain tram direction du Chateau partira à {heure_min_depart_clg}:{minute_min_depart_clg}:{seconde_min_depart_clg}")


@bot.command(pass_contexte=True) #Display timetable of each line
async def tram(ctx,arg=None):
    if arg == "3":
        with open('data.txt') as json_file:
            data_tram3 = json.load(json_file)

        for i in data_tram3:
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
                stringtemp_arrive_clg=i['fields']['horaire_arrivee_theorique']
                print(stringtemp_arrive_clg)
    if arg == "2":
        await ctx.send("ligne 2")
    if arg == "1":
        await ctx.send("ligne 1")
    if arg != '1' and arg != '2' and arg != "3":
        await ctx.send("Please choose a number between 1 and 3, use can use the command `r!tram 3`")

print("Bot Read to use :)")
bot.run(token)
random.seed(1)