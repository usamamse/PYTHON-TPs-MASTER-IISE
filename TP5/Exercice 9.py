lignes =0
try:
    with open("g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\exemple.txt",mode="r") as file:
        lignes = file.readlines()

        total_lignes = len(lignes)
        total_mots=0
        total_cara =0
        for ligne in lignes:
            total_mots += len(ligne.split())
            total_cara += len(ligne)
        
        print(f"Nombre total e lignes : {total_lignes}")
        print(f"Nombre total de mots : {total_mots}")
        print(f"Nombre total de caracères : {total_cara}")
except FileNotFoundError:
    print(f"File not found !")

