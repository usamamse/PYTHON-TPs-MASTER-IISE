class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre 
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        # Adding a string representation for better display
        return f"'{self.titre}' par {self.auteur} ({self.annee_publication})"

class Bibliotheque:
    def __init__(self, liste_livre=None):
        if liste_livre is None:
            self.liste_livre = []
        else:
            self.liste_livre = liste_livre

    def ajouter_livre(self, livre):
        if livre not in self.liste_livre:
            self.liste_livre.append(livre)

    def afficher_livres(self):
        if not self.liste_livre:
            print("La bibliothèque est vide !")
        else:
            for index, livre in enumerate(self.liste_livre, start=1):
                print(f"{index} - {livre}")

# Creating books
livre1 = Livre("La boîte à merveilles", "Ahmed Sefrioui", 1954)
livre2 = Livre("Antigone", "Jean Anouilh", 1944)
livre3 = Livre("Le dernier jour d'un condamné", "Victor Hugo", 1829)

# Creating a library
biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.ajouter_livre(livre3)

# Displaying books
biblio.afficher_livres()
