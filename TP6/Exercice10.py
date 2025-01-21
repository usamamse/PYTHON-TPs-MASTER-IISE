def Combinez_Tout():
    while True:
        fichiernom = input("Veuillez saisir le nom du fichier avec l'extension (.txt)")

        try:
            with open(fichiernom,'r') as fichier:
                print(f"Le contenu du fichier {fichiernom} est :")
                print(fichier.read())
            break
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{fichiernom} n'existe pas. Veuillez essayer avec une autre nom'")
        except IOError:
            print(f"Erreur: Impossible d'ouvrir le fichier '{fichiernom}'. Verifiez le nom")
    
    while True:
        try:
            nombre = input("Veuillez saisir un entier : ")
            nombre = int(nombre)

            print(f"L'entier saisi est : {nombre}")
            break

        except ValueError:
            print("Erreur : Ce n'est pas un entier valide")
        except Exception as e:
            print(f"Erreur : {e}")

Combinez_Tout()