from abc import ABC, abstractmethod
import math

class Forme(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def calculer_surface(self):
        raise NotImplementedError("subclass must define abstract method")

class Cercle(Forme):
    def __init__(self,rayon):
        super().__init__()
        self.rayon = rayon
    
    def calculer_surface(self):
        return math.pi*self.rayon**2
    
class Rectangle(Forme):
    def __init__(self,longeur,largeur):
        super().__init__()
        self.largeur=largeur
        self.longeur=longeur
    
    def calculer_surface(self):
        return self.largeur*self.longeur

def calculer_surface(liste_formes):
    for forme in liste_formes:
        surface = forme.calculer_surface()
        print(f'Surface de {forme.__class__.__name__}  : {surface:.2f}')

cercle = Cercle(5)
rectangle = Rectangle(8,2)

formes = [cercle,rectangle]
calculer_surface(formes)
    