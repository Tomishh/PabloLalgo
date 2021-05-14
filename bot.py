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
        liste_cut=i
        array=liste_cut.split(':')
        heure=int(array[0])
        minute=int(array[1])
        seconde=int(array[2])
        if heure < h_min:
            h_min = heure
            min_min = minute
            sec_min = seconde
        if heure == h_min and minute < min_min :
            h_min = heure
            min_min = minute
            sec_min = seconde
        if  heure == h_min and minute == min_min and seconde < sec_min:
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

    with open('data.txt') as json_file:
        data = json.load(json_file)
        string_depart = []
        string_arrive = []
    for i in data:
        if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
            stringtemp_arrive_clg=i['fields']['horaire_arrivee_theorique']
            string_arrive.append(stringtemp_arrive_clg)


        if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'CAEN Ch\u00e2teau Quatrans':
            stringtemp_depart_clg=i['fields']['horaire_arrivee_theorique']
            string_depart.append(stringtemp_depart_clg)

    depart=heure_mini_fonc(string_depart)
    arrivee=heure_mini_fonc(string_arrive)

    await ctx.send(f"Le prochain tram en direction de 'Collège HAWKING' arrive à l'arret 'Collège HAWKING' à {arrivee}\n Le prochain tram en direction de 'Chateau Quatran' arrive à l'arret 'Collège HAWKING' à {depart}")


@bot.command(pass_contexte=True) #Display timetable of each line
async def tram(ctx,arg=None):
    if arg == "3":
        with open('data.txt') as json_file:
            data_tram3 = json.load(json_file)
            string_depart_clg_hawking = []
            string_arrive_clg_hawking = []

            string_depart_grace_de_dieu=[]
            string_arrive_grace_de_dieu=[]

            string_depart_lycee_rostand =[]
            string_arrive_lycee_rostand =[]

            string_depart_aviation=[]
            string_arrive_aviation=[]

            # string_depart=[]
            # string_arrive=[]

            # string_depart=[]
            # string_arrive=[]

            # string_depart=[]
            # string_arrive=[]
        for i in data_tram3:

            #Collège Hawking Stop
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'CAEN Ch\u00e2teau Quatrans':
                stringtemp_depart_clg_hawking=i['fields']['horaire_arrivee_theorique']
                string_depart_clg_hawking.append(stringtemp_depart_clg_hawking)           
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
                stringtemp_arrive_clg_hawking=i['fields']['horaire_arrivee_theorique']
                string_arrive_clg_hawking.append(stringtemp_arrive_clg_hawking)

            #Grace de dieu Stop
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-GRACE DE DIEU-GRACE DE DIEU" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'CAEN Ch\u00e2teau Quatrans':
                stringtemp_depart_grace_de_dieu =i['fields']['horaire_arrivee_theorique']
                string_depart_grace_de_dieu.append(stringtemp_depart_grace_de_dieu)
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-GRACE DE DIEU-GRACE DE DIEU" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
                stringtemp_arrive_grace_de_dieu=i['fields']['horaire_arrivee_theorique']
                string_arrive_grace_de_dieu.append(stringtemp_arrive_grace_de_dieu)

            #Lycée Rostand Stop
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-Rostand-Fresnel-ROSTAND FRESNEL" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'CAEN Ch\u00e2teau Quatrans':
                stringtemp_depart_lycee_rostand=i['fields']['horaire_arrivee_theorique']
                string_depart_lycee_rostand.append(stringtemp_depart_lycee_rostand)
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-Rostand-Fresnel-ROSTAND FRESNEL" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
                stringtemp_arrive_lycee_rostand=i['fields']['horaire_arrivee_theorique']
                string_arrive_lycee_rostand.append(stringtemp_arrive_lycee_rostand)

            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-AVIATION-AVIATION" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'CAEN Ch\u00e2teau Quatrans':
                stringtemp_depart_aviation =i['fields']['horaire_arrivee_theorique']
                string_depart_aviation.append(stringtemp_depart_aviation)
            if i['fields']['nom_de_l_arret_stop_name'] == "Caen-AVIATION-AVIATION" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
                stringtemp_arrive_aviation=i['fields']['horaire_arrivee_theorique']
                string_arrive_aviation.append(stringtemp_arrive_aviation)
      

        depart_clg_hawking=heure_mini_fonc(string_depart_clg_hawking)
        arrive_clg_hawking=heure_mini_fonc(string_arrive_clg_hawking)

        depart_grace_de_dieu=heure_mini_fonc(string_depart_grace_de_dieu)
        arrive_grace_de_dieu=heure_mini_fonc(string_arrive_grace_de_dieu)

        depart_lycee_rostand=heure_mini_fonc(string_depart_lycee_rostand)
        arrive_lycee_rostand=heure_mini_fonc(string_arrive_lycee_rostand)

        depart_aviation=heure_mini_fonc(string_depart_aviation)
        arrive_aviation=heure_mini_fonc(string_arrive_aviation)


        depart=heure_mini_fonc(string_depart)
        arrivee=heure_mini_fonc(string_arrive)
        await ctx.send(f""">>> Tram 3 : :trolleybus: :small_red_triangle: : "Direction Chateau Quatrans" | :small_red_triangle_down: : Direction "Collège Hawking"
        Arret Aviation : :small_red_triangle: : {depart_aviation} :small_red_triangle_down: : {arrive_aviation} 
        Arret Lycée Rostand : :small_red_triangle: : {depart_lycee_rostand} :small_red_triangle_down: : {arrive_lycee_rostand}  
        Arret Grace de dieu : :small_red_triangle: : {depart_grace_de_dieu} :small_red_triangle_down: : {arrive_grace_de_dieu}
        Arret Collège Hawking : :small_red_triangle: : {depart_clg_hawking} :small_red_triangle_down: : {arrive_clg_hawking}""")   

        
            # if i['fields']['nom_de_l_arret_stop_name'] == "" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'CAEN Ch\u00e2teau Quatrans':
            #     stringtemp_depart =i['fields']['horaire_arrivee_theorique']
            #     string_depart.append(stringtemp_depart)
            # if i['fields']['nom_de_l_arret_stop_name'] == "" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
            #     stringtemp_arrive=i['fields']['horaire_arrivee_theorique']
            #     string_arrive.append(stringtemp_arrive)

        # depart=heure_mini_fonc(string_depart)
        # arrive=heure_mini_fonc(string_arrive)

        #Arret : :small_red_triangle: : {} :small_red_triangle_down: : {} 
                
    if arg == "2":
        await ctx.send("ligne 2")
    if arg == "1":
        await ctx.send("ligne 1")
    if arg != '1' and arg != '2' and arg != "3":
        await ctx.send("Please choose a number between 1 and 3, use can use the command `r!tram 3`")

print("Bot Read to use :)")
bot.run(token)
random.seed(1)