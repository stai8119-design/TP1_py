class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initiale(self):
        """Retourne la première lettre du nom en MAJUSCULE."""
        return self.nom[0].upper() if self.nom else ""

    def __repr__(self):
        return f"Contact(nom='{self.nom}', email='{self.email}', telephone='{self.telephone}')"