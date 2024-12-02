def somme_liste(liste):
    somme = 0
    for element in liste:
        somme = somme + element
    return somme
liste = [1,2,3,4]
print(somme_liste(liste))