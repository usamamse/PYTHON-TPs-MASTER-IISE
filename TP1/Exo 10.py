def fusionner_dicts(dict1,dict2):

    dict_fus = dict1

    for cle, valeur in dict2.items():
        if cle in dict_fus:
            dict_fus[cle] += valeur
        else:
            dict_fus[cle] = valeur

    return dict_fus

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 5, 'd': 50}

print(fusionner_dicts(dict1,dict2))