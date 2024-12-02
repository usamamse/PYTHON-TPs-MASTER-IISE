def compte(liste):
    dict={}
    for m in liste:
        nbr=0
        for i in liste:
            if m == i:
                nbr=nbr+1
                dict.update({i:nbr})  
    return dict   
dict = ["a","a","b","c","a"]
print(compte(dict))