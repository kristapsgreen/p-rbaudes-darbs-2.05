import json
import classes as cl
import requests

def PrecuIevade():
    noliktava = []
    noliktava.append(cl.Elektronika('Datorpele', 39.50, 'Razer Basilisk bezvadu datorpele'))
    noliktava.append(cl.Elektronika('Monitors', 299.50, '4k 144hz gaming monitors'))
    noliktava.append(cl.Apgerbs('Kurpes',77.45,'Ādas kurpes'))
    noliktava.append(cl.Gramata('1984', 34.58, 'grāmata par politiku'))
    return noliktava

def Izvade(preces):
    for i in range(len(preces)):
        preces[i].print()

def pievienotGrozam(grozs, obj, numb):
    grozs.update({obj : numb})

def izvgrozs(grozs):
    for x , y in grozs.items():
        for i in range(y):
            x.print()

def nongrozs(grozs, obj):
        grozs.pop(obj)

def valutmaina(noliktava,valuta):
    for i in  range(len(noliktava)):
        noliktava[i].ChangeValuta(valuta)

def main():
    grozs = {}
    noliktava = PrecuIevade()
    # Izvade(noliktava)
    valutmaina(noliktava, 'GBP')
    pievienotGrozam(grozs, noliktava[0],5) #pievienoju daudz datorpeļu savam grozam 
    pievienotGrozam(grozs, noliktava[1],1)
    pievienotGrozam(grozs, noliktava[2],2)
    nongrozs(grozs, noliktava[0]) #noņemu datorpeli
    izvgrozs(grozs)
    print ("hello")


if __name__ == "__main__":
    main()
