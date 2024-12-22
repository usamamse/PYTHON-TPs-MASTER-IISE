import csv
path = r'g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\contacts.csv'

def AppFinale(choix):
    if choix == 1:
        data = [input("Nom :").upper(),input("Age :"),input("Ville :")]
        with open(path, mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Nom", "Age", "Ville"])
            writer.writerow(data)
            print("Contact added successfully!")
    elif choix == 2:
        try:
            with open(path,mode='r') as file:
                print("==== Liste des contacts ====")
                for row in csv.reader(file):
                    print(row)
        except FileNotFoundError:
            print("File not found!")
    elif choix == 3:
        nom = input("Nom :").upper()
        try:
            with open(path,mode="r") as file:
                for row in csv.reader(file):
                    if row and row[0].upper() == nom:
                        print("Contact existed!")
                        return
                print("Contacts not existed!")
        except FileNotFoundError:
            print("File not found!")
    elif choix==4:
        nom = input("Nom : ").upper()
        try:
            with open(path,mode="r") as file:
                lignes = [ligne for ligne in csv.reader(file) if ligne and ligne[0].upper() != nom]
            with open(path,mode="w",newline="") as file:
                csv.writer(lignes)
            print("Contact deleted succefully!")
        except FileNotFoundError:
            print("File not found!")
    else:
        print("Choix invalide !")
        

print("=============== MENU ===============")
print("     1- ajouter des contacts")
print("     2- afficher tous les contacts")
print("     3- rechercher un contact par nom")
print("     4- supprimer un contact")
print("====================================")
choix = int(input("Veuillez choisir une fonctionnalité (Numero) :"))
AppFinale(choix)