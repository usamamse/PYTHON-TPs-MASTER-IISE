from abc import ABC,abstractmethod
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
        return self.rayon**2*math.pi
        
class Rectangle(Forme):
    def __init__(self,longeur,largeur):
        super().__init__()
        self.longeur = longeur
        self.largeur = largeur
    
    def calculer_surface(self):
        return self.largeur*self.longeur
    
cercle = Cercle(5)
rectangle = Rectangle(8,2)

print(f'Surface du cercle : {cercle.calculer_surface()}')
print(f'Surface de rectangle : {rectangle.calculer_surface()}')