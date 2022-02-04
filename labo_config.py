#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Classes de base pour le laboratoire.

Permet de configurer le système et simplifier la modification du fichier labo.py

Copyright 2007-2022, F. Mailhot et Université de Sherbrooke
"""

import numpy


class PgcdBase:
    """Classe PGCD_BASE, utilisée pour définir les types de base:

    - PGCD_EUCLIDE: utilisation de l'algorithme de Euclide
    - PGCD_BINAIRE: utilisation de la méthode binaire du calcul du pgcd

    Cette classe doit être héritée par la classe PGCD du fichier labo.py
    """

    PGCD_EUCLIDE = 1
    PGCD_BINAIRE = 2
    PGCD_STD = 3

    def __init__(self, op_type):
        """Constructeur d'un objet de type PgcdBase:

        Args:
            op_type (int): Le type de calcul de pgcd effectué (PGCD_EUCLIDE, PGCD_BINAIRE ou PGCD_STD)

        Returns:
            void: ne fait que l'initialisation de l'objet de type PgcdBase
        """
        self.type = op_type
        self.res_ok = False
        if self.type == self.PGCD_EUCLIDE:
            self.pgcd = self.pgcd_euclide
        elif self.type == self.PGCD_BINAIRE:
            self.pgcd = self.pgcd_binaire
        elif self.type == self.PGCD_STD:
            self.pgcd = self.pgcd_std

        else:
            print("Erreur: Pas de pgcd de ce type")
            self.pgcd = None
        return

    @staticmethod
    def pgcd_euclide(a, b):
        """L'algorithme d'Euclide est fourni

        Args:
            a (long): Le premier nombre
            b (long): Le deuxième nombre

        Returns:
            long: Le plus grand common diviseur (pgcd) entre les nombres a et b
        """
        if a < b:
            t = a
            a = b
            b = t
        while b != 0:
            t = a // b
            t = a - b * t
            a = b
            b = t
        return a

    @staticmethod
    def pgcd_binaire(a, b):
        """L'algorithme de calcul binaire du pgcd doit apparaître dans le fichier labo.py

        La méthode pgcd_binaire n'est qu'un espace réservé (placeholder):
            - Doit être redéfinie par les classes qui héritent de PGCD_BASE

        Args:
            a (long): Le premier nombre
            b (long): Le deuxième nombre

        Returns:
            long: Le plus grand common diviseur (pgcd) entre les nombres a et b
        """
        return 42

    @staticmethod
    def pgcd_std(a, b):
        """Calcule le pgcd en utilisant la version de numpy (méthode statique de la classe PgcdBase)

        Args:
            a (long): Le premier nombre
            b (long): Le deuxième nombre

        Returns:
            long: Le plus grand common diviseur (pgcd) entre les nombres a et b
        """
        return numpy.gcd(a, b)


class PowerModBase:
    """Classe PowerModBase, utilisée pour définir les types de base:

    - MULT_STANDARD: utilisation de la multiplication standard pour la mise à une puissance
    - MULT_MONTGOMERY: utilisation de la multiplication de Montgomery pour la mise à une puissance
    - POWER_MOD_STD: utilisation de la méthode d'exponentiation de numpy

    """

    MULT_STANDARD = 1
    MULT_MONTGOMERY = 2
    POWER_MOD_STD = 3

    def init_Montgomery(self):
        """Initialise l'objet de type PowerModBase pour préparer l'utilisation de la multiplication de Montgomery

        Returns:
            void : Si utilisée, cette méthode doit être redéfinie dans labo.py
        """
        return

    def set_mult(self):
        """Définit l'opérateur de multiplication à utiliser:

            - MULT_STANDARD et POWER_MOD_STD utilisent la multiplication standard
            - MULT_MONTGOMERY utilise la multiplication de Montgomery

        Returns:
            void: Ne fait que définir l'opérateur de multiplication dans l'objet
        """
        if self.type == self.MULT_STANDARD:
            self.mult = self.mult_standard
            self.power = self.power_mod
        elif self.type == self.MULT_MONTGOMERY:
            self.mult = self.mult_montgomery
            self.power = self.power_monty
        elif self.type == self.POWER_MOD_STD:
            self.mult = self.mult_standard
            self.power = self.power_std
        else:
            print("Erreur: Pas de mise à une puissance de ce type")
        return

    def __init__(self, op_type, n, base=10):
        """La méthode __init__ est utilisée par le constructeur des objets de type POWER_MOD_BASE:

            - Appelle self.init_Montgomery, qui doit être définie dans la classe qui hérite de POWER_MOD_BASE

        Args:
            op_type (int): Le type de calcul à effectuer (MULT_STANDARD ou MULT_MONTGOMERY)
            n (long): Le nombre avec lequel le modulo sera réalisé
            base (long): La base de calcul.  Utilisé pour les multiplications de Montgomery.  Inutilisé autrement.

        Returns:
            void: L'objet de type POWER_MOD_BASE est annoté avec les paramètres requis
        """
        self.type = op_type
        self.N = n
        self.base = base
        self.unite = 1
        self.res_ok = False
        self.mult = None
        self.power = None
        self.num_shift = 0
        self.B2 = 1
        self.ordered_multiples = []
        self.set_mult()
        self.util = UtilFuncs(self.base)
        if self.type == self.MULT_MONTGOMERY:
            self.init_Montgomery()

        return

    def mult_standard(self, a, b):
        """Méthode de multiplication standard:

            - Cette méthode est une coquille vide et doit être redéfinie dans labo.py
            - self.N (long): Le nombre avec lequel le modulo est effectué

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de a * b mod(n)
        """
        return 42

    def mult_montgomery(self, a, b):
        """Méthode de multiplication de Montgomery:

            - Cette méthode est une coquille vide et doit être redéfinie dans labo.py
            - self.N (long): Le nombre avec lequel le modulo est effectué

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de a * b mod(n)
        """
        return 42

    def power_std(self, a, w):
        """Méthode de mise à une puissance utilisant la méthode standard fournie par Python:

            - Cette méthode est fournie, pour comparaison avec vos implémentations
            - self.N (long): Le nombre avec lequel le modulo est effectué

        Args:
            a (long): Le nombre à élever à une puissance
            w (long): La puissance

        Returns:
            long: La valeur de a^w mod(n)
        """
        return pow(a, w, self.N)

    def power_mod(self, _, __):
        """Méthode binaire des exposants traditionnelle:
            - Calcul habituel de la mise à une puissance, modulo un nombre
            - Une validation doit être faite pour assurer que le nombre "a" est plus petit que "n"
            - self.n (long): Le nombre avec lequel le modulo est effectué

        Args:
            _ (long): Le nombre à élever à une puissance
            __ (long): La puissance


        Returns:
            long: La valeur de a^w mod(n)
        """
        return 42

    def power_monty(self, _, __):
        """Méthode de mise à une puissance utilisant la multiplication de Montgomery:

            - Vous devez coder cette méthode
            - Déterminez ce qui doit être fait pour préparer l'utilisation de la multiplication de Montgomery
            - Inclure ces calculs préliminaires dans la méthode POWER_MOD.init_montgomery,
                qui est appelée automatiquement par le constructeur
            - Vous pouvez réutiliser la méthode POWER_MOD.power_struct,
                qui utilise la méthode de multiplication appropriée:
                + Le constructeur pointe POWER_MOD.mult vers la méthode de multiplication requise
                par le type de calcul demandé (standard ou Montgomery)
            - self.n (long): Le nombre avec lequel le modulo est effectué

        Args:
            _ (long): Le nombre à élever à une puissance
            __ (long): La puissance

        Returns:
            long: La valeur de a^w mod(n)
        """
        return 42


class MultBase:
    """Classe MultBase, utilisée pour définir les types de base:

    - MULT_STANDARD: utilisation de la multiplication standard
    - MULT_N2: utilisation de la multiplication apprise au primaire, un "chiffre" à la fois
    - MULT_KO: utilisation de la multiplication de Montgomery
    """

    MULT_STANDARD = 1
    MULT_N2 = 2
    MULT_KO = 3

    def __init__(self, op_type, base=10):
        """La méthode __init__ est utilisée par le constructeur des objets de type MULT_BASE

        Args:
            op_type (int): Le type de multiplication à effectuer (MULT_STANDARD, MULT_N2 ou MULT_KO)
            base (long): La base de calcul.  Utilisé pour les multiplications de type n^2 et de type Karatsuba-Ofman

        Returns:
            long: L'objet de type MULT_BASE est annoté avec les paramètres requis

        Note: Le constructeur appelle une méthode d'initialisation pour les types MULT_N2 et MULT_KO:
            - MULT_N2 fait appel à self.init_mult_n2:
                + Ne fait rien par défaut, mais peut être redéfini au besoin
            - MULT_KO fait appel à self.init_mult_ko:
                + Ne fait rien par défaut, mais peut être redéfini au besoin
        """
        self.type = op_type
        self.base = base
        self.util = UtilFuncs(self.base)
        self.res_ok = False
        if self.type == self.MULT_STANDARD:
            self.mult = self.mult_std
        elif self.type == self.MULT_N2:
            self.mult = self.mult_n2
            self.init_mult_n2()
        elif self.type == self.MULT_KO:
            self.mult = self.mult_ko
            self.init_mult_ko()
        else:
            print("Erreur: Pas de multiplication de ce type")
            self.mult = None
        return

    @staticmethod
    def mult_std(a, b):
        """Méthode de multiplication standard de Python:

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de (a * b)
        """
        return a * b

    def mult_n2(self, a, b):
        """Méthode de multiplication apprise à l'école primaire:
            - Cette méthode doit être définie dans labo.py

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de (a * b)
        """
        return 42

    def mult_ko(self, a, b):
        """Méthode de multiplication de Karatsuba-Ofman:
            - Cette méthode doit être définie dans labo.py

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de (a * b)
        """
        return 42

    def init_mult_n2(self):
        """Méthode pour initialiser l'objet pour utiliser la multiplication apprise à l'école primaire:

        Si utilisée, doit être redéfinie dans le fichier labo.py

        Rien n'est passé en paramètre, tout le nécessaire est déjà contenu dans l'objet

        Returns:
            void: Rien n'est retourné, cette méthode prépare l'utilisation de la multiplication apprise au primaire
        """
        return

    def init_mult_ko(self):
        """Méthode pour initialiser l'objet pour utiliser la multiplication de Karatsuba-Ofman:

        Si utilisée, doit être redéfinie dans le fichier labo.py

        Rien n'est passé en paramètre, tout le nécessaire est déjà contenu dans l'objet

        Returns:
            void: Rien n'est retourné, cette méthode prépare l'utilisation de la multiplication de Karatsuba-Ofman
        """
        return


class UtilFuncs:
    """Classe UtilsFuncs contient un certain nombre de fonctions statiques génériques utiles pour le laboratoire:

    - inverse_exposant(w):
        + Inverse les bits d'un nombre, utile pour les exposants dans la méthode binaire des exposants
    - is_power2(number):
        + indique si un nombre est une puissance de 2.  Utilise un truc élégant pour faire ce calcul efficacement
    - log2(number):
        + retourne le plancher du logarithme en base 2 du nombre passé en paramètre

    Cette classe contient aussi des méthodes qui sont liées à la base de calcul choisie:
        - remainder_standard(a) retourne le dernier chiffre modulo la base de calcul (qui n'est pas une puissance de 2)
        - remainder_power2(a) retourne le dernier chiffre, obtenu avec un masque binaire (base = puissance de 2)
        - shift_left_binary(a) retourne le nombre multiplié par la base (décalage de bits vers les MSB)
        - shift_right_binary(a) retourne le nombre divisé par la base (décalage de bits vers les LSB)
        - shift_left_standard(a) retourne le nombre multiplié par la base (multiplication, base != puissance de 2)
        - shift_right_standard(a) retourne le nombre divisé par la base (division, base != puissance de 2)
        - tous les paramètres requis sont calculés par le constructeur, qui appelle init_shift()

    """

    @staticmethod
    def inverse_exposant(w):
        """Inverse les bits d'un nombre (msb devient lsb, msb-1 devient lsb+1, etc.
        Utile pour le calcul binaire des exposants

        Args:
            w (long) : L'exposant à traiter

        Returns:
            long: wi,  l'exposant dont les bits ont été inversés
        """
        wi = 0
        while w != 0:
            wi = wi << 1
            wi = wi + (w & 1)
            w = w >> 1
        return wi

    @staticmethod
    def is_power2(number):
        """Méthode pour déterminer si un nombre est une puissance de 2:
            + Utile pour la méthode de Montgomery
            + Utile pour déterminer s'il est possible d'effectuer des décalages binaires
            + Si la base de calcul n'est pas une puissance de 2, il faut faire une vraie division par la base (coûteux)
            + Truc intéressant (et performant) pour déterminer si un nombre est une puissance de 2,
                tiré de "Hacker's Delight" de Henry S. Warren

        Args:
            number (long): La valeur de la base de calcul proposée

        Returns:
            boolean: Le nombre est une puissance de 2 (ou non)
        """
        return number and (not (number & (number - 1)))

    @staticmethod
    def log2(a):
        """Méthode pour déterminer le logarithme en base 2:
            + Utile pour l'initialisation de la méthode de Montgomery

        Args:
            a (long): Le nombre dont on cherche le logarithme en base 2

        Returns:
            long: Le logarithme entier (arrondi vers la valeur la plus basse) en base 2 du nombre a
        """
        log_a = 0
        while a != 0:
            a = a >> 1
            log_a = log_a + 1
        return log_a

    def remainder_standard(self, a):
        """Méthode pour déterminer le plus petit "chiffre" d'un nombre:
            + Utile pour la méthode de Montgomery, lorsque la base utilisée n'est pas une puissance de 2

        Args:
            a (long): Le nombre dont on cherche le plus petit chiffre

        Returns:
            long: Le reste du nombre a modulo la base de calcul utilisée
        """
        r = a % self.base
        return r

    def remainder_power2(self, a):
        """Méthode pour déterminer le plus petit "chiffre" d'un nombre:
            + Utile pour la méthode de Montgomery, lorsque la base est une puissance de 2
            + Ce calcul n'exige pas de division et est donc très efficace

        Args:
            a (long): Le nombre dont on cherche le plus petit chiffre

        Returns:
            long: Le reste du nombre a modulo la base de calcul utilisée
        """
        r = a & self.mask
        return r

    def shift_right_binary(self, a):
        """Décale à droite le nombre a d'un certain nombre de bits, définis dans le champs self.bit_shift_param
        Utile pour la multiplication de Montgomery, pour les bases de calcul qui sont une puissance de 2
        Utile aussi pour la multiplication de Karatsuba-Ofman et celle apprise au primaire (bases puissances de 2)

        Par exemple, en base 2, 0b1011 (11 en base 10) devient 0b0101 (5 en base 10)

        Args:
            a (long) : Le nombre à décaler

        Returns:
            long: Le nombre a décalé de self.bit_shift_param bits
        """
        return a >> self.bit_shift_size

    def shift_left_binary(self, a):
        """Décale à gauche le nombre a d'un certain nombre de bits, définis dans le champs self.bit_shift_param
        Utile pour la multiplication de Montgomery, pour les bases de calcul qui sont une puissance de 2
        Utile aussi pour la multiplication de Karatsuba-Ofman et celle apprise au primaire (bases puissances de 2)

        Par exemple, en base 2, 0b1011 (11 en base 10) devient 0b0101 (5 en base 10)

        Args:
            a (long) : Le nombre à décaler

        Returns:
            long: Le nombre a décalé de self.bit_shift_param bits
        """
        return a << self.bit_shift_size

    def shift_right_standard(self, a):
        """Décale à droite le nombre a d'un seul chiffre (dépend de la base de calcul utilisée)
        Utile pour la multiplication de Montgomery, pour les bases de calcul qui ne sont pas des puissances de 2.
        Utile aussi pour la multiplication de Karatsuba-Ofman et celle apprise au primaire (bases non puissances de 2)

        Par exemple, en base 10, 246 devient 24

        Args:
            a (long) : Le nombre à décaler

        Returns:
            long: Le nombre dont on a retiré de plus petit chiffre, ce dernier défini par la base
        """
        return a // self.base

    def shift_left_standard(self, a):
        """Décale à gauche le nombre a d'un seul chiffre (dépend de la base de calcul utilisée)
        Utile pour la multiplication de Montgomery, pour les bases de calcul qui ne sont pas des puissances de 2.
        Utile aussi pour la multiplication de Karatsuba-Ofman et celle apprise au primaire (bases non puissances de 2)

        Par exemple, en base 10, 246 devient 24

        Args:
            a (long) : Le nombre à décaler

        Returns:
            long: Le nombre dont on a retiré de plus petit chiffre, ce dernier défini par la base
        """
        return a * self.base

    def init_shift(self):
        """Prépare tous les champs nécessaires au décalage binaire ou normal:
            + Détermine si la base de calcul est une puissance de 2
            + Utilise la bonne méthode de décalage (binaire ou non, si la base est une puissance de 2 ou non)
            + Utilise la bonne méthode pour obtenir le reste modulo la base (binaire ou non)
            + Pour les bases qui sont des puissances de 2:
                - Détermine le nombre de bits à décaler lors des décalages
                - Détermine le masque pour obtenir le "chiffre" le plus faible (en faisant un ET avec le masque)

        Returns:
            void: Tous le champs sont initialisés directement dans l'objet
        """
        if self.is_power2(self.base):
            self.base_is_power2 = True
            self.div_op = self.shift_right_binary
            self.bit_shift_size = self.log2(self.base) - 1
            self.mask = self.base - 1
            self.remainder = self.remainder_power2
        else:
            self.base_is_power2 = False
            self.div_op = self.shift_right_standard
            self.remainder = self.remainder_standard

    def __init__(self, base=10):
        self.base = base
        self.base_is_power2 = False
        self.div_op = None
        self.bit_shift_size = 0
        self.mask = 1
        self.remainder = None
        self.init_shift()
        return
