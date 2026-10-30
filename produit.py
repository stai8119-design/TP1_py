
from dataclasses import dataclass, field
from typing import List

@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0
    tags: List[str] = field(default_factory=list)

    def valeur_totale(self) -> float:
        """Le calcule de la valeur totale du stock pour ce produit."""
        return self.prix * self.quantite


if __name__ == "__main__":
    print("Test de la classe Produit")
    
    p1 = Produit("Café", 3.5, 9, ["boisson", "chaud"])
    p2 = Produit("Café", 3.5, 9, ["boisson", "chaud"])
    
    print("p1 =", p1)
    print("p1 == p2 :", p1 == p2) 
    print("Valeur totale de p1 =", p1.valeur_totale())
    p3 = Produit("Thé", 5.0)
    print("p3 =", p3)
    print("Tags de p3 =", p3.tags)  # []