class Chien:
    def __init__(self,nom,race,age):
        self.nom=nom
        self.race=race
        self.age=age
    def aboyer(self):
        print(f"Woof, je m'appelle {self.nom}.")
    
chien = Chien('Rocky','Doberman',2)
chien.aboyer()