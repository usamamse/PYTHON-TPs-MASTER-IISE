from abc import ABC,abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer():
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture se deplace par les roues qui rolants par le moteur")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette se deplace en pedalant")

voiture = Voiture()
bicyclette = Bicyclette()

voiture.deplacer()
bicyclette.deplacer()