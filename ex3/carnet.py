from Contact import Contact

class Carnet:
    def __init__(self):
        self.contacts = []

    def ajouter(self, contact: Contact):
        self.contacts.append(contact)

    def chercher(self, nom_partiel: str) -> list:
        """Liste des contacts dont le nom contient la chaîne donnée."""
        nom_partiel_lower = nom_partiel.lower()
        return [c for c in self.contacts if nom_partiel_lower in c.nom.lower()]

    def __len__(self):
        return len(self.contacts)


if __name__ == "__main__":
    carnet = Carnet()
    c1 = Contact("Ali", "0612345678", "ali@exemple.com")
    c2 = Contact("Sarah", "0698765432", "sara@eeample.com")
    c3 = Contact("Alice", "0690876453", "alice@exemple.com")
    
    carnet.ajouter(c1)
    carnet.ajouter(c2)
    carnet.ajouter(c3)
    
    print(c1.initiale)
    print(carnet.chercher("ali"))
    print(len(carnet))