phrases = []
for i in range(3):
    phrases.append(str(input(f'Veuillez entrer la {i+1}éme phrase :')))

fichier = open("g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\phrases.txt","w")
for phrase in phrases:
    fichier.write(f"{phrase}\n")