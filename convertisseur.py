
class Convertisseur:
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros):
        """Convertit les euros en dirhams."""
        return euros * Convertisseur.taux_eur_dh

    @classmethod
    def changer_taux(cls, nouveau_taux):
        """Modifie le taux de change."""
        if nouveau_taux <= 0:
            raise ValueError("Erreur: Le taux doit être positif.")
        cls.taux_eur_dh = nouveau_taux

    @classmethod
    def depuis_dh(dirhams, cls): 
        return dirhams / cls.taux_eur_dh
    @classmethod
    def depuis_dh(cls, dirhams):
        """Convertit les dirhams en euros."""
        return dirhams / cls.taux_eur_dh


if __name__ == "__main__":
    print("Test du Convertisseur ")
    
    print("100 EUR en DH =", Convertisseur.vers_dh(100)) 
    Convertisseur.changer_taux(11.0)
    print("Taux changé à:", Convertisseur.taux_eur_dh)
    print("110 DH en EUR =", Convertisseur.depuis_dh(110)) 
    c = Convertisseur()
    print("50 EUR avec instance =", c.vers_dh(50))