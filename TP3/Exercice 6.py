class Produit:
    def __init__(self,nom,prix):
        self.__nom = nom
        self.__prix = prix
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nv_nom):
        self.__nom = nv_nom
    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self,nv_prix):
        self.__prix=nv_prix

class Commande:
    def __init__(self,produit,quantite):
        self.produit = produit
        self.quantite = quantite

class Panier:
    def __init__(self,liste_commandes=None):
        self.liste_commandes = liste_commandes if liste_commandes is not None else []


    def ajouter_commande(self,commande):
        for commande in self.liste_commandes:
            if commande.produit in self.liste_commandes:
                print(f'La commande {commande.produit} deja exitée dans panier')

            self.liste_commandes.append(commande)
    
    def calcul_total(self):
        total = 0
        for commande in self.liste_commandes:
            total += commande.produit.prix*commande.quantite
        
        return total
    
produit1 = Produit("Produit 1", 150)
produit2 = Produit("Produit 2",230)
produit3 = Produit("Produit 2",50)

commande1 = Commande(produit1,5)
commande2 = Commande(produit2, 1)
commande3 = Commande(produit3, 4)

panier = Panier([commande1, commande2])

print(f"La somme de panier est : {panier.calcul_total()} DHs")

panier.ajouter_commande(commande3)
print(f"La somme de panier est : {panier.calcul_total()} DHs")

