import math

class Cercle:
    def __init__(self, r: float):
        self.r = r

    @property
    def r(self):
        """Accéder au rayon."""
        return self._r

    @r.setter
    def r(self, val: float):
        """Contrôle de valeur du rayon."""
        if val <= 0:
            raise ValueError("Le rayon ne peut pas etre négatif.")
        self._r = val

    def aire(self) -> float:
        return math.pi * self.r ** 2

    def perimetre(self) -> float:
        return 2 * math.pi * self.r

    def __str__(self):
        return f"Cercle(rayon={self.r}) | Aire={self.aire():.2f} | Périmètre={self.perimetre():.2f}"
    
c = Cercle(3.0)
print("Valeur du rayon:", c.r)
print("Aire du cercle:", c.aire())
print("Périmètre du cercle:", c.perimetre())

try:
    print("Tentative de définir un rayon négatif")
    c.r = -5
except ValueError as e:
    print(f"Erreur interceptée : {e}")