def safe_division(a,b):
    if b == 0:
        raise ZeroDivisionError("Erreur arithemetique: echec d'operation (b est nulle)")
    else:
        return a/b
    
print(safe_division(6,2))
print(safe_division(6,0))