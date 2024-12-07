class Compte:
    def __init__(self,titulaire,solde):
        self.titulaire = titulaire
        self.solde = solde
    def deposer(self,montant):
        self.solde +=montant
    def retirer(self,montant):
        self.solde -=montant
    def afficher_solde(self):
        print(f"Votre solde est : {self.solde} DHs.")
compte = Compte("Oussama",0)
compte.deposer(100)
compte.afficher_solde()
compte.retirer(30)
compte.afficher_solde()