class Personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
        self.liste_amis = [] 
    
    def ajouter_ami(self,ami):
        if ami not in self.liste_amis:
            self.liste_amis.append(ami)
            
    def afficher_amis(self):
        if not self.liste_amis:
            print(f"{self.nom} n'a pas encore d'amis.")
        else:
            print(f"Liste d'amis de {self.nom} :")
            for index, ami in enumerate(self.liste_amis, start=1):
                print(f"{index} - {ami}")
                
personne = Personne("Oussama",23)

personne.afficher_amis()
personne.ajouter_ami("Ahmed")
personne.ajouter_ami("Yassine")
personne.ajouter_ami("Hassan")

personne.afficher_amis()
        
        
        
        