import json
from collections import namedtuple
import classes as cl
import requests

noliktava = []
precetuple = []

def usd_rate():
    url = "http://open.er-api.com/v6/latest/EUR"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        usd_rate = json_data["rates"]["USD"]
        return usd_rate
    else:
        print("error")
        return None
    

def readnoliktava():
    global noliktava
    global precetuple
    with open('noliktava.json', 'r') as f:
        try:
            data = json.load(f)
            for item in data:
                if item is not None:
                    if 'Elektronika' in item:
                        precetuple.append(cl.Elektronika(**item))
                    elif 'Apgerbs' in item:
                        precetuple.append(cl.Apgerbs(**item))
                    elif 'Gramata' in item:
                        precetuple.append(cl.Gramata(**item))
                    else:
                        precetuple.append(None)
            noliktava = [prece for prece in precetuple if prece is not None]
        except:
            pass


def refreshnoliktava():
    global precetuple
    precetuple = []
    for i in range(0, len(noliktava)):
        if isinstance(noliktava[i], cl.Elektronika):
            precetuple.append(namedtuple("Elektronika",['nosaukums', 'cena', 'apraksts'])(*noliktava[i]))
        elif isinstance(noliktava[i], cl.Apgerbs):
            precetuple.append(namedtuple("Apgerbs",['nosaukums', 'cena', 'apraksts'])(*noliktava[i]))
        elif isinstance(noliktava[i], cl.Gramata):
            precetuple.append(namedtuple("Gramata",['nosaukums', 'cena', 'apraksts'])(*noliktava[i]))
        else:
            precetuple.append(None)
    with open('noliktava.json', 'w') as f:
            json.dump([obj._asdict() for obj in precetuple], f)

def jaunaprece():
    readnoliktava()
    nosaukums = input("Ievediet preces nosaukumu ")
    cena = input("Ievediet preces cenu ")
    apraksts = input("Ievediet preces aprakstu ")
    tips = input("Ievediet tipu elektro/apgerbs/gramata ")
    if tips == "elektro":
        prece = cl.Elektronika(nosaukums, cena, apraksts)
    elif tips == "apgerbs":
        prece = cl.Apgerbs(nosaukums, cena, apraksts)

    elif tips == "gramata":
        prece = cl.Gramata(nosaukums, cena, apraksts)
    else:
        prece = None
    noliktava.append(prece)
    print(str(noliktava))
    refreshnoliktava()

# run time 

while True:
    print("Sveicināti veikalā")
    # izvade()
    jaunaprece()