
class Vecteur2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        """La surcharge de l'operateur +"""
        return Vecteur2D(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre):
        """La surcharge de l'operateur -"""
        return Vecteur2D(self.x - autre.x, self.y - autre.y)

    def __mul__(self, scalaire):
        """La surcharge de l'operateur * (multiplication par un scalaire)"""
        return Vecteur2D(self.x * scalaire, self.y * scalaire)

    def __eq__(self, autre):
        """La surcharge de l'operateur =="""
        if not isinstance(autre, Vecteur2D):
            return False
        return self.x == autre.x and self.y == autre.y

    def __repr__(self):
        return f"Vecteur2D({self.x}, {self.y})"


if __name__ == "__main__":
    print("Test des vecteurs")
    
    v1 = Vecteur2D(2, 3)
    v2 = Vecteur2D(4, 5)

    v3 = v1 + v2
    print("v1 + v2 =", v3) 

    v4 = v2 - v1
    print("v2 - v1 =", v4) 

    v5 = v1 * 2
    print("v1 * 2 =", v5) 
    
    print("v1 == Vecteur2D(1, 2) :", v1 == Vecteur2D(1, 2))