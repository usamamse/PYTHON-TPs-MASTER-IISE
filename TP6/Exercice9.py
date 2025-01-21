class PositiveNumber(Exception):
    pass


def get_positive_integer():
    while True:
        try: 
            nombre = input("Veuillez entrez un entier positif : ")
            nombre = int(nombre)

            if nombre <= 0:
                print("L'entier doit etre positif")
            else:
                return nombre
        except ValueError:
            print("Ce n'est pas un entier valide. Essayez encore.")

positive_integer = get_positive_integer()
print(f"L'entier positif saisi est : {positive_integer}")