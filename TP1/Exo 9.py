def analyse_texte(texte):
    dict={}
    
    texte = texte.strip()

    nombre_cara = len(texte)
    nombre_mots = len(texte.split()) if texte else 0

    dict.update({"nombre_de_mots":nombre_mots,"nombre_de_caracteres":nombre_cara})

    return dict

texte = "Faculte des sciences filiere Ingenierie Informatique et Systemes Embarques"
print(analyse_texte(texte))