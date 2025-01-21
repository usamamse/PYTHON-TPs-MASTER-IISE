def read_file(filename):
    fichier = None  
    try:
        fichier = open(f'{filename}.txt', 'r')  
        lignes = fichier.readlines()
        for ligne in lignes:
            print(ligne.strip())  
    except FileNotFoundError:
        print("Le fichier n'existe pas!")
    finally:
        if fichier is not None:  
            fichier.close()

read_file('testExercice3')
