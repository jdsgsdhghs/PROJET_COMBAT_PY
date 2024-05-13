from personnage import Personnage
from random import randint

class RoiSorcier(Personnage): 
    def __init__(self, nom, vie, degats, experience, tour):
        super().__init__()
        self.__nom = self.set_nom(nom)
        self.__vie = self.set_vie(vie)
        self.__degats = self.set_degats(degats)
        self.__experience = self.set_experience(experience)
        self.tour = tour

    FORCE_FRAPPE_1 = 5
    FORCE_FRAPPE_2 = 20

    def frappeAvecSonEpee(self, enemy: Personnage):
        enemy.recoitDegat(self, self.FORCE_FRAPPE_1 + self.get_experience())

    def attaqueAvecSonNazgul(self, enemy: Personnage):
        enemy.recoitDegat(self, self.FORCE_FRAPPE_2 + self.get_experience())

    def attaque(self, enemy: Personnage):
        attack_choice = randint(1, 2)
        if attack_choice == 1:
            self.frappeAvecSonEpee(enemy)
        else:
            self.attaqueAvecSonNazgul(enemy)