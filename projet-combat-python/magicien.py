from personnage import Personnage
from random import randint

class Magicien(Personnage): # Definition de la classe Magicien() qui va hériter des méthode de Personnage(), on indique un héritage en mettant la classe parent entre parenthèse
    def __init__(self, nom, vie, degats, experience, tour): # Appel de la fonction constructeur ou je defini les valeurs à entrer à la création d'une instance de la classe
        self.__nom = self.set_nom(nom) # Ici la propriété nom de magicien va devoir réécrire la propriété de Personnage() mais c'est une propriété privée donc je dois utiliser un setter
        self.__vie = self.set_vie(vie)
        self.__degats = self.set_degats(degats)
        self.__experience = self.set_experience(experience)
        self.tour = tour

    FORCE_FRAPPE_1 = 10 # Voici une constante une valeur qui ne doit pas etre modifier
    FORCE_FRAPPE_2 = 15

    def lanceUnSort(self, enemy: Personnage):
        enemy.recoitDegat(self, self.FORCE_FRAPPE_1 + self.get_experience())

    def lanceUnRayonDeLumiereSombre(self, enemy: Personnage):
        enemy.recoitDegat(self, self.FORCE_FRAPPE_2 + self.get_experience())

    def attaque(self, enemy: Personnage): # Réécriture de ma méthode attaque afin qu'elle soit utilisable
        attack_choice = randint(1, 2) # je stock un nombre entre 1 et 2 afin de choisir quel compétence le magicien lance
        if attack_choice == 1:
            self.lanceUnSort(enemy)
        else:
            self.lanceUnRayonDeLumiereSombre(enemy)

