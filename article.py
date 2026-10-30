class Article:
    def __init__(self, reference: str, designation: str, prixHt: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prixHt = prixHt
        self.stock = stock

    def valeur_stock(self) -> float:
        """Calcule de la valeur totale du stock."""
        return self.prixHt * self.stock

    def ajouter_stock(self, quantite: int):
        """Ajoute une quantité au stock actuel."""
        if quantite < 0:
            raise ValueError("La quantité ajoutée doit etre positive.")
        self.stock += quantite

    def __str__(self):
        return f"[{self.reference}] {self.designation} | Stock: {self.stock} | Prix HT: {self.prixHt:.2f} DH"

a1 = Article("EETY-120", "Clavier Mécanique", 75.99, 15)
print(a1.valeur_stock())  
a1.ajouter_stock(5)
print(a1)                