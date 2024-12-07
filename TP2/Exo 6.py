class Rectangle:
    def __init__(self,largeur,hauteur):
        self.larguer = largeur
        self.hauteur = hauteur
    def calculer_surface(self):
        return self.larguer*self.hauteur
    def calculer_perimetre(self):
        return 2*self.larguer+2*self.hauteur
rectangle = Rectangle(6,2)
print(f"Le rectangle est d'une surface {rectangle.calculer_surface()} et d'un perimetre {rectangle.calculer_perimetre()}")