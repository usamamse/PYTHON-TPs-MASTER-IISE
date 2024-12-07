class Personne:
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def se_presenter(self):
        print(f"Le nom est : {self.nom}.")
        print(f"Le prenom est : {self.prenom}.")
        print(f"L'age : {self.age} ans.")
class Etudiant(Personne):
    def __init__(self,nom, prenom, age, matricule):
        super().__init__(nom,prenom,age)
        self.matricule = matricule
    def etudier(self):
        print(f"Bonjour je suis un etudiant avec un matricule {self.matricule}")

personne = Personne("Ahmed","ZAHRI",20)
personne.se_presenter()

etudiant = Etudiant("Oussama","ELMESSAOUDI",22,"D134192")
etudiant.se_presenter()
etudiant.etudier()
        
        
            
        
        
        