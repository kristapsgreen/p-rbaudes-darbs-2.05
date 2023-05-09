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

def main():
    noliktava = PrecuIevade()
    Izvade(noliktava)
    print ("hello")

if __name__ == "__main__":
    main()
