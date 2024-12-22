class Produit:
    def __init__(self,nom,prix,seuil_remise,pourcentage_remise):
        self.__nom = nom
        self.__prix=prix
        self.__seuil_remise=seuil_remise
        self.__pourcentage_remise=pourcentage_remise
    
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,nom):
        self.__nom = nom

    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self,nv_prix):
        self.__prix = nv_prix

    def calculer_prix_avec_remise(self):
        if self.__prix > self.__seuil_remise:
            remise = self.__prix * (self.__pourcentage_remise/100)
            prix_finale = self.__prix - remise
        else:
            prix_finale = self.__prix
        return prix_finale

produit = Produit("Produit 1",150,100,20)

print(f"Produit : {produit.nom}")
print(f"Prix de base : {produit.prix} DHs")
print(f"Prix après remise : {produit.calculer_prix_avec_remise()} DHs")
