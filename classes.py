from abc import ABC, abstractmethod

class Produkts:
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
