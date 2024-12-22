class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee

    def afficher_info(self):
        return f"Marque : {self.marque}, Modele : {self.modele}, annee : {self.annee}"

class Moteur:
    def __init__(self,puissance,type_moteur):
        self.puissance = puissance
        self.type_moteur=type_moteur

    def afficher_moteur(self):
        return f"Puissance : {self.puissance} CV, Type de moteur : {self.type_moteur}"

class Voiture(Vehicule,Moteur):
    def __init__(self,marque,modele,annee,puissance,type_moteur,nombre_places):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_places=nombre_places

    def afficher_info(self):

        return f"{super().afficher_info()}, {super().afficher_moteur()}, Nombre de places : {self.nombre_places}"

class Moto(Vehicule,Moteur):
    def __init__(self,marque,modele,annee,puissance,type_moteur,type_moto):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        return f"{super().afficher_info()}, {super().afficher_moteur()}, Type de moto : {self.type_moto}"
        

voiture = Voiture("Audi","A4",2022,6,"2.0 tdi",5)
moto = Moto("Kawazaki","Ninja H2R",2021,12,"HONDA","Sport Bike")
print(voiture.afficher_info())
print(moto.afficher_info())

