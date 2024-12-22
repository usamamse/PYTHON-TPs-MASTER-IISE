import json

etudiants = [
    {"Nom": "RIZKI","Age": 22,"Note":18},
    {"Nom": "HAFIDI","Age": 21,"Note":15},
    {"Nom": "ELMESSAOUDI","Age": 23,"Note":16},
    {"Nom": "SADIKI","Age": 22,"Note":12},
]

with open("g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\etudiants.json",mode="w") as file:
    json.dump(etudiants,file,indent=1)

with open("g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\etudiants.json",mode="r") as file:
    data = json.load(file)
    for etudiant in data:
        print(f"Nom : {etudiant['Nom']} , Age : {etudiant['Age']} , Note : {etudiant['Note']}")
        
