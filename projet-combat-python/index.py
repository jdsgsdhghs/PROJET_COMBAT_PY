from combat import Combat # Import de ma classe Combat() de mon fichier combat afin de pouvoir créer une instance de classe Combat().
from magicien import Magicien # Import de ma classe Magicien() de mon fichier magicien afin de pouvoir crée une instance de classe Magicien().
from roi_sorcier import RoiSorcier # Import de ma classe RoiSorcier() de mon fichier roi_sorcier afin de pouvoir crée une instance de classe RoiSorcier().
 
combat = Combat() # Création d'une instance de ma classe Combat(), je la stock dans une variable afin de pouvoir la réutiliser.
player1 = Magicien("Gandalf le gris", 80, 0, 0,'Joueur 1') # Création d'une instance de ma classe Magicien(), avec initialisation des propriétés.
player2 = RoiSorcier("Le Roi Sorcier", 80, 0, 0,'Joueur 2') # Création d' une instance de ma classe RoiSorcier(), avec initialisation des propriétés.

combat.demarrerCombat(player1, player2) # Lancement de la méthode démarrerCombat de mon instance de classe combat afin de lancer le combat.