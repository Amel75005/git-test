class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def getAge(self):
        return self.age
personne1 = Personne("Dupont","Armelle",20)
print(f"L'age de {personne1.prenom} {personne1.nom} est {personne1.getAge()} ans.")

