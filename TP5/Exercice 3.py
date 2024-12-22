phrases = []
for i in range(3):
    phrases.append(str(input(f'Veuillez entrer la {i+1}éme phrase :')))

fichier = open("g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\phrases.txt","w")
for phrase in phrases:
    fichier.write(f"{phrase}\n")

while (choix := input("Souhaitez vous ajouter d'autre ligne ? (Oui/Non)")) == "Oui": phrases.append(input('Veuillez entrer la phrase a entrer:')); [fichier.write(f"{phrase}\n") for phrase in phrases]
