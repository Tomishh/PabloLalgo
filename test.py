import asyncio
from typing import ValuesView
import discord
import time
import random
from discord.ext import commands
import requests
import json
import threading

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

def tram3():

    with open('data.txt') as json_file:
        data = json.load(json_file)
        string_depart = []
    for i in data:
        if i['fields']['nom_de_l_arret_stop_name'] == "Caen-COLLEGE HAWKING-COLLEGE HAWKING" and i['fields']['ligne'] == 'T3' and i['fields']['destination_stop_headsign'] == 'FLEURY Clg Hawking':
            stringtemp_arrive_clg=i['fields']['horaire_arrivee_theorique']
            string_depart.append(stringtemp_arrive_clg)
            print(stringtemp_arrive_clg)
        print(heure_mini_fonc(string_depart))


tram3()
time.sleep(10000)