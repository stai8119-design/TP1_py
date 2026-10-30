class JournalTaches:
    def __init__(self, nomFichier: str = "journal.txt"):
        self.nomFichier = nomFichier
        self.fichier = None

    def __enter__(self):
        """Appelé au début du bloc with."""
        self.fichier = open(self.nomFichier, 'a', encoding='utf-8')
        return self

    def __exit__(self, excType, excVal, excTb):
        """Appelé à la fin du bloc with."""
        if self.fichier:
            self.fichier.close()
        return False

    def ajouter_tache(self, description: str):
        """L'ajout d'une tâche au journal."""
        if self.fichier:
            self.fichier.write(f"- {description}\n")
        else:
            raise RuntimeError("Le journal n'est pas ouvert. Utilisez 'with'.")
        
with JournalTaches("taches_demo.txt") as journal:
    journal.ajouter_tache("Reviser la POO en Python")
    journal.ajouter_tache(" A faire TP 1")

with open("taches_demo.txt", "r") as f:
    print(f.read())