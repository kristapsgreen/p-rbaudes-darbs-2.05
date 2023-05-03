from abc import ABC, ABCMeta , abstractmethod
from collections import namedtuple 

class Produkts(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, nosaukums, cena, apraksts):
        self.nosaukums = nosaukums
        self.cena = cena
        self.apraksts = apraksts
    def print(self):
        print(self.nosaukums  + " " + self.cena + " " + self.apraksts)

class Elektronika(Produkts):
    pass

class Apgerbs(Produkts):
    pass

class Gramata(Produkts):
    pass

class ElektronikaTuple(namedtuple):
    nosaukums: str
    cena: str
    apraksts: str

class ApgerbsTuple(namedtuple):
    nosaukums: str
    cena: str
    apraksts: str

class GramataTuple(namedtuple):
    nosaukums: str
    cena: str
    apraksts: str