from abc import abstractmethod
from collections import namedtuple 
import requests
import json

class Produkts():
    @abstractmethod
    def __init__(self, nosaukums, cena, apraksts):
        self.nosaukums = nosaukums
        self.cena = cena
        self.apraksts = apraksts
    def print(self):
        print(self.nosaukums  + " " + self.cena + " " + self.apraksts)
    def price(self):
        return self.cena
    def ChangeValuta(self, currency):
        x = requests.get('http://open.er-api.com/v6/latest/EUR')
        data = x.json()
        # data = json.loads(x.json())
        rate = float(data['rates'][currency])
        y = self.cena
        self.cena = y*rate 


        

class Elektronika(Produkts):
    pass

class Apgerbs(Produkts):
    pass

class Gramata(Produkts):
    pass

