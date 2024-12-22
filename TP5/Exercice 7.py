import shutil

phrases = []
for i in range(3):
    phrases.append(str(input(f'Veuillez entrer la {i+1}éme phrase :')))

fichier = open("g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\journal.txt","w")
for phrase in phrases:
    fichier.write(f"{phrase}\n")

source = r"g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\journal.txt"
destination = r"g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\journal_copie.txt"
try:
    shutil.copy(source,destination)
    print("File copied succefully")
except FileNotFoundError:
    print("File not found !")
except IOError:
    print("Can't copy the file !")