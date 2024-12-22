import os

ancien_nom = r"g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\phrases.txt"
nv_nom = r"g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\anciennes_phrases.txt"

try:
    os.rename(ancien_nom,nv_nom)
    print(f"Fichier renommé en {nv_nom}")
except FileNotFoundError:
    print("Le fichier à renommer n'a pas été trouvé")
except IOError:
    print("Erreur lors du renommage du fichier.")