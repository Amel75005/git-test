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


