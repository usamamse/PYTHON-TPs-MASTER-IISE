class Voiture:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def affiche_info(self):
        print(f"Marque de voiture : {self.marque}.")
        print(f"Modele de voiture : {self.modele}.")
        print(f"Année de voiture : {self.annee}.")

v1 = Voiture('Volkswagen','Golf 4',2015)
v1.affiche_info()