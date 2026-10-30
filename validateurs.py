
import functools

def valider_positif(*indices):
    """Décorateur qui valide que les arguments aux indices donnés sont positifs."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for idx in indices:
                if idx < len(args):
                    value = args[idx]
                    if not isinstance(value, (int, float)) or value <= 0:
                        raise ValueError(f"Erreur: L'argument a l'index {idx} (valeur: {value}) doit etre un nombre positif")
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    @valider_positif(1) 
    def aire(self, facteur=1.0):
        """Calcule l'aire du rectangle avec un facteur optionnel."""
        return self.largeur * self.hauteur * facteur


if __name__ == "__main__":
    print("Test du Decorateur de validation")
    
    rect = Rectangle(7, 10)
    
    print("Aire normale =", rect.aire())  
    print("Aire avec facteur 2 =", rect.aire(2.0))
    try:
        print("Tentative avec un facteur negatif...")
        rect.aire(-3)
    except ValueError as e:
        print("Exception attrapee avec succes ->", e)