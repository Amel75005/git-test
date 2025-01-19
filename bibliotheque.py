class Livre :
    def __init__(self,titre,auteur,nbpages):
        self.titre=titre
        self.auteur=auteur
        self.nbpages=nbpages
        self.disponible=True
    
    def emprunter(self):
        if self.disponible:
            self.disponible=False
            return True
        return False
    
    def retourner(self):
        self.disponible=True

    def __str__(self):
        return f"'{self.titre}' par {self.auteur} de {self.nbpages} pages ({'Disponible' if self.disponible else 'Emprunté'})"
class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
            return
        print(f"Livres dans la bibliothèque '{self.nom}':")
        for livre in self.livres:
            print(f" - {livre}")

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.disponible:
                livre.emprunter()
                print(f"Vous avez emprunté '{titre}'.")
                return
        print(f"Le livre '{titre}' n'est pas disponible.")

    def retourner_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and not livre.disponible:
                livre.retourner()
                print(f"Vous avez retourné '{titre}'.")
                return
        print(f"Le livre '{titre}' n'est pas enregistré comme emprunté.")

ma_bibliotheque = Bibliotheque("Bibliothèque 1")
ma_bibliotheque.ajouter_livre(Livre("1984", "George Orwell",652))
ma_bibliotheque.ajouter_livre(Livre("Le Petit Prince", "Antoine de Saint-Exupéry",296))
ma_bibliotheque.ajouter_livre(Livre("L'Alchimiste", "Paulo Coelho",412))
ma_bibliotheque.afficher_livres()
ma_bibliotheque.emprunter_livre("1984")
ma_bibliotheque.afficher_livres()
ma_bibliotheque.retourner_livre("1984")
ma_bibliotheque.afficher_livres()