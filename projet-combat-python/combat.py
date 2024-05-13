from magicien import Magicien
from roi_sorcier import RoiSorcier
from random import randint

class Combat: # Création d'une classe combat

    # Je crée une méthode afin de définir qui prendra le premier tour
    def tour_joueur(self, magicien: Magicien, roi_sorcier: RoiSorcier): 
        first_turn = randint(1, 2)
        if first_turn == 1:
            return magicien.tour # Je fais un retour de la propriété tour du joueur qui prendra le premier tour pour pouvoir l'utiliser plus tard
        else:
            return roi_sorcier.tour

    def demarrerCombat(self, magicien: Magicien, roi_sorcier: RoiSorcier):
        # Ma variable tour qui va me permettre de gérer le tour des joueurs, je la défini une première fois pour décider qui prend le premier tour
        tour = self.tour_joueur(magicien, roi_sorcier)
        while magicien.get_vie() > 0 and roi_sorcier.get_vie() > 0: # Je fais une boucle qui tourne tant que personne n'a atteint 0 PV
            if tour == magicien.tour: # Ma condition qui verifie si c'est le tour du magicien
                magicien.attaque(roi_sorcier)
                tour = roi_sorcier.tour # Si oui alors je change la variable tour pour que ça soit le roi_sorcier le prochain
            else:
                roi_sorcier.attaque(magicien)
                tour = magicien.tour
        if magicien.get_vie() <= 0 : # Ici si le magicien atteint 0 pv, j'annonce la victoire du roi_sorcier
            print(f"{roi_sorcier.get_nom()} a battu {magicien.get_nom()}.")
        elif roi_sorcier.get_vie() <= 0 : # sinon j'annonce la victoire du magicien
            print(f"{magicien.get_nom()} a battu {roi_sorcier.get_nom()}.")