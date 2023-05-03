import classes as cl
import json
from collections import namedtuple

# pagaidām nestrādā - nav sakārtota pāreja uz tuple, un api call nav  
# noliktava ir lists
# groza vietā izveidoju noliktavu, kas dara ko līdzīgu 
noliktava = []
# lieto namedtuple
def readnoliktava():
    global noliktava  # use global laikam 
    with open('noliktava.json', 'r') as f:
        noliktava = json.load(f)

def refreshnoliktava():
    with open('noliktava.json', 'w') as f:
        json.dump([obj.__dict__ for obj in noliktava], f)

def izvade():
    readnoliktava()  
    for obj in noliktava:
        print(obj.nosaukums)

def jaunaprece():
    readnoliktava()
    nosaukums = input("Ievediet preces nosaukumu ")
    cena = input("Ievediet preces cenu ")
    apraksts = input("Ievediet preces aprakstu ")
    tips = input("Ievediet tipu elektro/apgerbs/gramata ")
    if tips == "elektro":
        preceTuple= namedtuple("Elektronika",[nosaukums, cena, apraksts])
        prece = cl.Elektronika(nosaukums, cena, apraksts)
    elif tips == "apgerbs":
        preceTuple= namedtuple("Apgerbs",[nosaukums, cena, apraksts])
        prece = cl.Apgerbs(nosaukums, cena, apraksts)

    elif tips == "gramata":
        preceTuple= namedtuple("Gramata",[nosaukums, cena, apraksts])
        prece = cl.Gramata(nosaukums, cena, apraksts)
    else:
        prece = None
    noliktava.append(prece)
    print(noliktava)
    refreshnoliktava()

# run time 

while True:
    print("Sveicināti veikalā")
    # izvade()
    jaunaprece()