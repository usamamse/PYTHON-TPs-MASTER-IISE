import os
import datetime
import math

rep_courant= os.getcwd()
print(f'Le repertoire courant : {rep_courant}')

date_act= datetime.datetime.now()
print(f'La date et l\'heure actuelles : {date_act}')

try:
    nombre = float(input("Veuillez entrez un nombre : "))
    if nombre < 0 :
        print("Erreur : la racine carree d'un nombre negatif")
    else: 
        print(f"La racine carree de {nombre} est : {math.sqrt(nombre)}")
except ValueError:
    print("Erreur: Veuillez entrer un nombre valide.")
