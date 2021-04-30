import asyncio
import threading
import time
import requests
import json
import threading


print("let's go chacal")

async def tram_stat():
    while True:
        print("JSON start to load") 
        url = "https://www.data.gouv.fr/fr/datasets/r/76f45f30-b195-48b1-b5fe-67a3658b02b5"
        response = requests.get(url)
        response_txt= response.text
        parse= json.loads(response_txt)
        print("Json Load Succesfully")
        print("- - - - - - - - - - - - - -")
        print("Starting to write Json in txt file")
        with open('data.txt', 'w') as outfile:
            json.dump(parse, outfile)
        print("Data printed in txt file")
        print("- - - - - - - - - - - - - -")
        time.sleep(50)

def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(tram_stat())

loop = asyncio.get_event_loop()
t = threading.Thread(target=loop_in_thread, args=(loop,))
t.start()