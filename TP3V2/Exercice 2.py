class Personne:
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    @property
    def nom(self):
        return self.__nom
        
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
    
    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self,prenom):
        self.__prenom = prenom
    
    @property 
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age > 0:
            self.__age=age
        else:
            raise ValueError("L'age doit etre positif")
    
    def afficher_informations(self):
        return f'Nom: {self.nom}, Prenom : {self.prenom}, Age: {self.age}'
        
personne = Personne("ELMESSAOUDI","Oussama",23)
print(personne.nom)
print(personne.prenom)

personne.prenom = "Ahmed"

print(personne.prenom)

print(personne.afficher_informations())

        
    