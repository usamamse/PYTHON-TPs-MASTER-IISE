class Animal:
    def faire_du_bruit(self):
        print("L'animal fait du bruit")
class Chien(Animal):
    def faire_du_bruit(self):
        print("Woof! Woof!")
class Chat(Animal):
    def faire_du_bruit(self):
        print("Miaw! Miaw!")
animal = Animal()
animal.faire_du_bruit()
chien = Chien()
chien.faire_du_bruit()
chat = Chat()
chat.faire_du_bruit()
        
            