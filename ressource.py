
import gc

class Ressource:
    def __init__(self, nom: str):
        self.nom = nom
        print(f"Création de la ressource '{nom}'")

    def __del__(self):
        """Appelé quand l'objet est détruit."""
        print(f"Destruction de la ressource '{self.nom}'")

    def utiliser(self):
        print(f"Utilisation de '{self.nom}'")


if __name__ == "__main__":
    print("Début du test de ressource")
    
    r = Ressource("Fichier de données")
    r.utiliser()
    print("--> On supprime l'objet avec del")
    del r
    gc.collect()
    
    print("Fin du script")