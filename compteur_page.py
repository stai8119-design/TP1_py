class CompteurPage:
    total_visite = 0

    def __init__(self, nomPage):
        self.nomPage = nomPage
        self.visites = 0
        
        CompteurPage.total_visite += 1

    def ajouter_visite(self):
        self.visites += 1
        CompteurPage.total_visite += 1

    def afficher_statistiques(self):
        return f"Page '{self.nomPage}': {self.visites} visites. Le total global: {CompteurPage.total_visite}"


page1 = CompteurPage("Home")
page2 = CompteurPage("Contact")

page1.ajouter_visite()
page1.ajouter_visite()
page2.ajouter_visite()

print(page1.afficher_statistiques())
print(page2.afficher_statistiques()) 
print(CompteurPage.total_visite)    