def safe_division(a,b):
    try:
        if b != 0:
            resultat = a/b
        else:
            raise ZeroDivisionError("Erreur arithemetique: echec d'operation (b est nulle)")
    except ZeroDivisionError as e:
        print(e)
    else:
        print("la division a été effectuée avec succès")
        return resultat
    finally:
        print(" la fonction est terminée")

print(safe_division(6,2))
print(safe_division(6,0))