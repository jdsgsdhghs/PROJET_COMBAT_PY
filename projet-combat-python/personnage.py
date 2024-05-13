from random import randint # Import de la méthode randint du module random.

# Définition de ma classe Personnage()
class Personnage:
    # On nous demande d'empechez l'instanciation de la classe Personnage, on va donc utilisez la méthode __new__, qui est appelée à la création d'une nouvelle instance de classe 
    def __new__(cls, *args): # Dans ma méthode __new__ cls représente ma classe et *args représente les paramêtres passé lors des initialisation de classe
        if cls is Personnage: # J'indique ici que, si lors de la création de ma classe, l'instance de Classe ici représenté par "cls", est Personnage()
            raise TypeError("Vous ne pouvez pas instantiez cette classe.") # Alors tu me fais monter une erreur.
        return object.__new__(cls) # Autrement tu me crée un nouvelle objet "cls".
    
    # Notez que ma classe personnage ici ne possedent pas de constructeur, les propriétés sont directement défini dans ma classe.
    # La consigne étant de créer des propriétés privées, le nom des propriétés est précédé d'un double underscore, car c'est ainsi qu'on indique des propriétés privée en python
    # Les propriétés privée ne sont accessible que par la classe qui les possède, c'est à dire qu'on ne peut pas y acceder autrement que par la classe Personnage()
    # Il existe aussi des propriété public, c'est le cas de tour et il éxiste aussi des propriétés protégée qui sont indiqué avec un underscore avant le nom de la propriété
    # Les propriétés public sont les propriétés de base, les propriété protégée sont utilisables dans la classe qui les défini et dans ses classe enfants
    # Notez que les méthodes peuvent aussi être privée ou protégée. 
    __nom = "nom"
    __vie = 100
    __force = 0
    __experience = 0
    __degats = 0
    tour = 'joueur 1'

    
    # On passe maintenant au méthode crée pour la classe personnage, les méthodes sont utilisable via une instance de classe.
    # Ce sont des fonctions qu'on ne peux utiliser que par le biais d'une classe.

    # Ma méthode frappe possède trois paramètres, self qui représente l'objet donc l'instance de ma classe, ma cible et ma force de frappe
    def frappe(self, target , striking_force):
        # Ma cible étant un objet adverse de sous classe Personnage, elle bénéficiera des méthodes de notre classe personnage 
        target.recoitDegat(self, striking_force) # On appel la méthode recoitDegat de target afin de pouvoir lui infliger des dégats car on ne peux pas le faire autrement

    # La méthode esquive va permettre de déterminer si oui ou non le coup touchera, pour faire ça on va utiliser la méthode randint du module random
    def esquive(self):
        random_number = randint(1, 5) # Je stock le résultat de mon randint dans une variable afin de pouvoir réutiliser ce résultat
        if random_number == 1: # Ici ma condition indique que si le resultat stocké dans ma variable est égale à 1, alors ma fonction renverra vraie autrement elle renvéra faux
            return True
        else:
            return False        

    # La méthode recoitDegat prend à l'instar de frappe 3 paramêtre, mais ici il faut penser cette méthode contraire  à la méthode frappe
    def recoitDegat(self, enemy, taken_striking_force):
        if self.esquive(): # Cette condition verifie que le retour de ma méthode esquive, si le retour est vraie j'indique que l'attaque à été esquivé
            print(f"{self.get_nom()} à esquivé l'attaque de {enemy.get_nom()}.")  # Ici  je fait un "string interpolation afin de pouvoir introduire du code dans ma chaine de caractère"
        else: # Cette condition indique que si esquive est faux dans ce cas la je fait les calculs lié au combats
            self.__degats += taken_striking_force # Ajout de la force de frappe reçue aux dégats
            self.__vie -= taken_striking_force # Soustraction de la force de frappe reçue au points de vie, c'est pas vraiment la consigne mais c'est plus logique pour moi.
            self.__experience += 1 # Ajout de l'expérience
            if self.get_vie() < 0: # Une petite condition pour éviter d'afficher des valeurs négatives
                self.set_vie(0)
            print(f"{self.get_nom()} à été touché par {enemy.get_nom()}. Il subit {taken_striking_force} points de dégats. Il reste à {self.get_nom()}, {self.get_vie()} points de vies.")


    # Place maintenant aux getters et setters, ces méthodes permettent d'acceder à une valeur sans toucher à cette valeur directement, les getters retourne une valeur
    # Tandis que les setters définissent une valeur. 
    def get_nom(self):
        return self.__nom
    
    def set_nom(self, value):
        self.__nom = value

    def get_vie(self):
        return self.__vie
    
    def set_vie(self, value):
        self.__vie = value

    def get_force(self):
        return self.__force
    
    def set_force(self, value):
        self.__force = value

    def get_experience(self):
        return self.__experience
    
    def set_experience(self, value):
        self.__experience = value

    def get_degats(self):
        return self.__degats
    
    def set_degats(self, value):
        self.__degats = value

    def attaque(self, enemy: 'Personnage'): # La méthode attaque, je l'ai fait parce qu'elle est demandé dans Personnage(), mais je la réécris dans les classes enfants   
        attack_choice = randint(1, 2)
        return attack_choice