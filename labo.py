#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Ce fichier contient trois classes et toutes les méthodes nécessaires pour le laboratoire.
    Certaines méthodes sont complètes et servent d'exemple.
    Les autres méthodes doivent être complétées.



    Les trois classes à compléter sont:
        - Pgcd: Touche le calcul du pgcd et contient trois méthodes de calcul:
            + pgcd_euclide(a, b), la méthode traditionnelle (cette méthode est déjà codée dans PgcdBase)
            + pgcd_binaire(a,b), la méthode binaire de calcul du pgcd (doit être codée)
            + pgcd_std(a,b), la méthode de calcul du pgcd disponible avec numpy
                (cette méthode est déjà codée dans la classe de base PgcdBase de labo_config.py)

            Vous pouvez tester le temps d'exécution et la validité de ces méthodes en utilisant testlabo.py,
            avec les arguments -pgcd_euclide, -pgcd_binaire, -pgcd_std
            ou -pgcd (ce dernier argument teste les trois méthodes de calcul du pgcd)

        - PowerMod: Effectue le calcul de mise à une puissance modulo un nombre et contient trois méthodes de calcul:
            + power_mod(a, w, n), la méthode traditionnelle (cette méthode est déjà codée)
            + power_monty(a, w, n),  la méthode basée sur la multiplication de Montgomery (doit être codée)
            + power_std(a, w, n), la méthode standard de mise à une puissance de Python
                (cette méthode est déjà codée dans la classe de base PowerModBase de labo_config.py)

            Vous pouvez tester le temps d'exécution et la validité de ces méthodes en utilisant testlabo.py,
            avec les arguments -exposant_binaire, -exposant_Montgomery, -exposant_std
            ou -exposant (ce dernier argument teste les trois méthodes de calcul de l'exponentiation)

        - Mult: Trois méthodes de calcul de la multiplication:
            + mult_n2(a, b), la multiplication apprise au primaire, un chiffre à la fois (doit être codée)
            + mult_ko(a, b), la multiplication de Karatsuba-Ofman (doit être codée)
            + mult_std(a, b), la multiplication standard de Python
                (cette méthode est déjà codée dans la classe de base MultBase de labo_config.py)

            Vous pouvez tester le temps d'exécution et la validité de ces méthodes en utilisant testlabo.py,
            avec les arguments -mult_prim, -mult_ko, -mult_std
            ou -mult (ce dernier argument teste les trois méthodes de multiplication)

        - Note: vous pouvez tester votre code en utilisant les commandes:
            + "python testlabo.py -all" (teste l'ensemble des méthodes)
            + "python testlabo.py -h" (donne la liste des arguments possibles)
            + "python testlabo.py -v" (mode "verbose", qui indique les valeurs de tous les arguments)

    Copyright 2007-2022, F. Mailhot et Université de Sherbrooke
"""

import labo_config


class Pgcd(labo_config.PgcdBase):
    """Classe Pgcd, utilisée pour comparer les trois méthodes de calcul du pgcd :

    - l'algorithme de Euclide
    - la méthode binaire de calcul du pgcd
    - le calcul standard du pgcd (méthode fournie par numpy et fournie dans la classe de base PgcdBase)
    """

    @staticmethod
    def pgcd_binaire(a, b):
        """Vous devez coder l'algorithme calcul binaire du pgcd

        Args:
            a (long): Le premier nombre
            b (long): Le deuxième nombre

        Returns:
            long: Le plus grand common diviseur entre les nombres a et b
        """

        # voir si les chiffre sont impaire ou il y as un entre eux est pair
        # est ce qu'il est pair ? => x mod(2) = 0 alors x est pair



        while a != b:  # quand on arrive a a = b alors on obtient le pgcd
            if a % 2 == 0:
                # print("a est pair")

                a = a >> 1  # divider le nb sur 2
            if b % 2 == 0:
                # print("b est pair")
                b = b >> 1  # diviser le nb sur 2
            if b % 2 != 0 and a % 2 != 0:

                # print("a et b sont impair")
                if a > b:
                    a = a - b  # faire une soustraction du plus grand nb
                elif a < b:
                    b = b - a

        # print(" resultat : a = ", a, "b = ", b)

        if a == b:
            res = a
        return a


class PowerMod(labo_config.PowerModBase, labo_config.UtilFuncs):
    """Classe PowerMod, utilisée pour comparer les trois méthodes de mise à une puissance, modulo un certain nombre:

    - la méthode binaire des exposants
    - la méthode de Montgomery
    - la méthode fournie par Python (effectué dans la classe de base PowerModBase)

    Le nombre utilisé pour le modulo est défini lors de la création d'une instance
        - multiplication standard: n'a besoin que du modulo
        - multiplication de Montgomery:
            - a besoin du modulo
            - doit connaître la base utilisée (base 10, base 2, base 4, base 8, base 16, etc.)
            - doit connaitre B et B^2, pour calculer les nombres "tilde"
            - doit connaitre le nombre de "chiffres" dans les nombres avec lesquels
                les calculs sont faits (déterminés par la base et le nombre n)
            - doit connaître comment obtenir le "chiffre" le plus faible d'un nombre
                pour pouvoir trouver le multiple de n qui, additionné au nombre,
                fait en sorte que le "chiffre" le plus faible est un zéro
            - doit déterminer comment faire le décalage d'un nombre avec un zéro dans le chiffre le plus faible
            - lors de sa création, une instance destinée
                au calcul de Montgomery créée le tableau des multiples du modulo
                qui sont nécessaires (1 seul en base 2, 3 en base 4, 7 en base 8, 9 en base 10, 15 en base 16, etc.)
            - lorsqu'elle est exécutée, la multiplication de Montgomery utilise toutes ces données
    """

    def set_B2_numshift_and_unite(self):
        """Méthode pour préparer les données nécessaires à la multiplication de Montgomery:
            - Utilisée lors de l'initialisation de la méthode de Montgomery
            - B est la puissance de la base (self.base) immédiatement supérieure à n (self.n)
            - B^2 est utilisé pour calculer a_tilde dans les multiplications de Montgomery
            - num_shift représente le nombre de fois que la multiplication de Montgomery
                doit être effectuée lorsqu'on multiplie 2 nombres
            - num_shift est le nombre de chiffres du nombre n (self.n), exprimé dans la base (self.base):
                + Par exemple: pour n = 31, base = 10, il y a 2 chiffres (3 et 1)
                + pour n = 31, base = 2, il y a 5 chiffres (1, 1, 1, 1, 1)
                + pour n = 31, base = 4, il y a 3 chiffres (1, 3, 3)
                + pour n = 31, base = 8, il y a 2 chiffres (3, 7)
                + pour n = 31, base = 16, il y a 2 chiffres (1, 15)  ou (0x1, 0xF)
            - unite est la valeur d'une unité pour le début du calcul binaire des exposants:
                + Pour la méthode standard, cette valeur est 1,
                + mais pour la méthode de Montgomery, cette valeur est 1 "tilde", c'est-à-dire B
            - self.base (long) : La base de calcul utilisée (10 ou une puissance de 2)
            - self.N (long) : Le nombre avec lequel le modulo est effectué
            - Aucun paramètre passé en entrée.  Tout est compris dans les champs de l'objet

        Returns:
            void: Aucune valeur retournée.  Les champs B, B2 (B^2), num_shift
                et unite sont calculés et ajoutés à l'objet de type POWER_MOD
        """
        return

    def set_ordered_multiples(self):
        """Méthode pour obtenir un tableau des multiples de n:
            - Utilisée lors de l'initialisation de la méthode de Montgomery
            - Les valeurs sont ordonnées pour compléter le résidu du résultat partiel
                de telle sorte qu'on puisse ensuite décaler ce résultat
            - Par exemple, pour n = 7, avec un calcul en base 10:
                + la valeur 49 (7 * 7) se trouve à l'indice 1 du tableau
                + la valeur 28 (4 * 7) se trouve à l'indice 2 du tableau
                + la valeur 7  (1 * 7) se trouve à l'indice 3 du tableau
                + la valeur 56 (8 * 7) se trouve à l'indice 4 du tableau
                + la valeur 35 (5 * 7) se trouve à l'indice 5 du tableau
                + la valeur 14 (2 * 7) se trouve à l'indice 6 du tableau
                + la valeur 63 (9 * 7) se trouve à l'indice 7 du tableau
                + la valeur 42 (6 * 7) se trouve à l'indice 8 du tableau
                + la valeur 21 (3 * 7) se trouve à l'indice 9 du tableau
            - self.base (long) : La base de calcul utilisée (10 ou une puissance de 2)
            - self.N (long) : Le nombre avec lequel le modulo est effectué
            - Aucun paramètre passé en entrée.  Tout est compris dans les champs de l'objet

        Returns:
            void: Aucune valeur retournée.  Le tableau self.ordered_multiples[] est créé dans l'objet de type POWER_MOD
        """
        return

    def init_Montgomery(self):
        """Méthode pour initialiser l'objet pour utiliser la multiplication et l'exponentiation de Montgomery:

        Devrait faire:
            + Le calcul de B, et B^2 modulo n, où B est la puissance de la base immédiatement supérieure à n
            + Le calcul de la taille (nombre de chiffres) des nombres à traiter modulo n.
                Cette taille dépend de la base de calcul
            + Le calcul du tableau d'ajouts complémentaires de "n" au résultat de multiplication partielle
                (ce qui permet d'obtenir un "0" dans le "chiffre" le plus faible d'un nombre)
            + Le calcul de la valeur correspondant à "1 tilde",
                qui doit être utilisé lorsque le calcul de l'exponentiation est amorcé
            + La valeur de "1 tilde" peut être conservée dans self.unite (qui contient 1 par défaut)

        Note:
            + Si la base utilisée est une puissance de 2:
                - Les "décalages" de Montgomery peuvent se faire avec des décalages binaires
                - Sinon, il faut utiliser une division standard

            + Le plus petit "chiffre" du multiplicande est défini par le reste modulo la base de calcul:
                - Pour une base qui est une puissance de 2, un & binaire avec la (base -1)
                    (par exemple, 0b111 en base 8) peut calculer ce "chiffre"
                - Pour une base autre qu'une puissance de 2 (par exemple, en base 10),
                    il faut utiliser un modulo standard pour trouver le "chiffre"

            + Il faut donc définir comment faire les décalages
                et comment obtenir le "chiffre" le plus faible d'un nombre
            + Une instance de la classe labo_config.UtilsFuncs
                et certaines de ses méthodes pourraient s'avérer utiles

        Rien n'est passé en paramètre, tout le nécessaire est déjà contenu dans l'objet

        Returns:
            void: Rien n'est retourné, cette méthode prépare l'objet pour l'utilisation de la méthode de Montgomery
        """
        return

    def mult_standard(self, a, b):
        """Méthode de multiplication standard, modulo un nombre N:

            - self.N (long) : Le nombre avec lequel le modulo est effectué

        Args:
            a (long): Le multiplicateur
            b (long): Le multiplicande

        Returns:
            long: La valeur de a * b mod(n)
        """
        return 42

    def mult_montgomery(self, a, b):
        """Méthode de multiplication de Montgomery:

            - Prend un "chiffre" à la fois du multiplicateur (b):
                + Le chiffre correspond à (b modulo la base de calcul utilisée)
                + Pour un calcul en base 10: plus petit chiffre (par exemple, pour 543, utiliser 3)
                + Pour un calcul en base 2: le LSB (par exemple, pour 27, 0b11011, utiliser 1)
                + Pour un calcul en base 4: les deux derniers LSB
                    (par exemple, pour 27, 0b11011, utiliser 3 (0b11 en base 2))
                + Pour un calcul en base 16: les quatre derniers LSB
                    (par exemple, pour 27, 0b11011, 0x1D, utiliser 0xD (0b1011 en base 2)
            - Multiplie le chiffre du multiplicateur par le multiplicande
            - Complète le résultat (avec un multiple de n qui permet ensuite de décaler):
                + Le nombre obtenu a alors un "0" comme dernier chiffre
                + On peut par la suite décaler le dernier chiffre (équivalent à une division par la base de calcul)
            - Décale le résultat (dépend de la base de calcul utilisée):
                + Décalage binaire de 1 bit en base 2, équivalent à une division par 2
                + Décalage binaire de 2 bits en base 4, équivalent à une division par 4
                + Décalage binaire de 4 bits en base 16, équivalent à une division par 16
                + Décalage binaire de k bits en base 2^k, équivalent à une division par 2^k
                + Division par 10 en base 10
            - self.N (long) : Le nombre avec lequel le modulo est effectué

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de a * b mod(n)
        """
        return 42

    def power_struct(self, a, w):
        """Méthode binaire des exposants (structure):

            - Structure utilisant la fonction de multiplication fournie dans POWER_MOD.mult
            - POWER_MOD.mult pointe vers mult_standard ou mult_montgomery
            - Attention: au début de la première itération, cette méthode devrait multiplier l'unité (1) par elle-même:
                + Pour une multiplication de Montgomery,
                    il faut redéfinir l'unité (1), pour correspondre à "1 tilde", qui est ...?
                + Sinon la multiplication de Montgomery de (1 * 1) donnera (1 / B)
                + self.unite peut être calculé à cet effet dans self.init_Montgomery()
            - self.n (long) : Le nombre avec lequel le modulo est effectué
            - Certaines méthodes de self.util (une instance de labo_config.UtilsFuncs) pourraient être utiles...

        Args:
            a (long): Le nombre à élever à une puissance
            w (long): La puissance

        Returns:
            long: La valeur de a^w mod(n)
        """
        return 42 * (
            1 + (a - a + w - w) * self.base
        )  # Expression bidon pour éliminer les warnings de PyCharm

    def power_mod(self, a, w):
        """Méthode binaire des exposants traditionnelle:
            - Calcul habituel de la mise à une puissance, modulo un nombre
            - Une validation doit être faite pour assurer que le nombre "a" est plus petit que "n"
            - self.n (long): Le nombre avec lequel le modulo est effectué

        Args:
            a (long): Le nombre à élever à une puissance
            w (long): La puissance

        Returns:
            long: La valeur de a^w mod(n)
        """
        return 42

    def power_monty(self, a, w):
        """Méthode de mise à une puissance utilisant la multiplication de Montgomery:

            - Vous devez coder cette méthode
            - Déterminez ce qui doit être fait pour préparer l'utilisation de la multiplication de Montgomery
            - Inclure ces calculs préliminaires dans la méthode POWER_MOD.init_montgomery,
                qui est appelée automatiquement par le constructeur
            - Vous pouvez réutiliser la méthode POWER_MOD.power_struct,
                qui utilise la méthode de multiplication appropriée:
                + Le constructeur pointe POWER_MOD.mult vers la méthode de multiplication requise
                par le type de calcul demandé (standard ou Montgomery)
            - self.N (long): Le nombre avec lequel le modulo est effectué

        Args:
            a (long): Le nombre à élever à une puissance
            w (long): La puissance


        Returns:
            long: La valeur de a^w mod(n)
        """
        return 42


class Mult(labo_config.MultBase, labo_config.UtilFuncs):
    """Classe Mult, utilisée pour comparer les méthodes de multiplication suivantes:

    - mult_std (multiplication standard Python, méthode fournie)
    - mult_n2 (multiplication apprise au primaire, un chiffre à la fois (en base 10, à coder)
    - mult_ko (multiplication de Karatsuba-Ofman (à coder)
    """

    def init_mult_n2(self):
        """Méthode pour initialiser l'objet pour utiliser la multiplication apprise au primaire:

        Devrait faire:
            + Utilise la base (self.base) pour:
                - déterminer comment obtenir le plus petit chiffre
                - déterminer comment décaler le produit partiel

        Note:
            + Si la base utilisée est une puissance de 2:
                - Les "décalages" peuvent se faire avec des décalages binaires
                - Sinon, il faut utiliser une division standard

            + Le plus petit "chiffre" du multiplicande est défini par le reste modulo la base de calcul:
                - Pour une base qui est une puissance de 2, un & binaire avec la (base -1)
                    (par exemple, 0b111 en base 8) peut calculer ce "chiffre"
                - Pour une base autre qu'une puissance de 2 (par exemple, en base 10),
                    il faut utiliser un modulo standard pour trouver le "chiffre"

            + Il faut donc définir comment faire les décalages
                et comment obtenir le "chiffre" le plus faible d'un nombre

        Rien n'est passé en paramètre, tout le nécessaire est déjà contenu dans l'objet

        Returns:
            void: Rien n'est retourné, cette méthode prépare l'utilisation de la multiplication du primaire
        """
        return

    def mult_n2(self, a, b):
        """Méthode de multiplication apprise à l'école primaire:
            - Par défaut:  le calcul est fait en base 10:
                + Pouvez-vous le faire dans une base arbitraire self.base?
                + Est-ce que certaines bases seraient avantageuses?
            - Chacun des chiffres du multiplicateur est multiplié à tour de rôle par le multiplicande
            - Décalages des résultats partiels (équivalent à une multiplication par 10)
            - Somme des résultats partiels

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de (a * b)
        """
        return 42

    def init_mult_ko(self):
        """Méthode pour initialiser l'objet pour utiliser la multiplication de Karatsuba-Ofman:

        Devrait faire:
            + Utilise la base (self.base) pour:
                - déterminer comment obtenir le plus petit chiffre
                - déterminer comment décaler le produit partiel

        Note:
            + Si la base utilisée est une puissance de 2:
                - Les "décalages" peuvent se faire avec des décalages binaires
                - Sinon, il faut utiliser une division standard

            + Le plus petit "chiffre" du multiplicande est défini par le reste modulo la base de calcul:
                - Pour une base qui est une puissance de 2, un & binaire avec la (base -1)
                    (par exemple, 0b111 en base 8) peut calculer ce "chiffre"
                - Pour une base autre qu'une puissance de 2 (par exemple, en base 10),
                    il faut utiliser un modulo standard pour trouver le "chiffre"

            + Il faut donc définir comment faire les décalages
                et comment obtenir le "chiffre" le plus faible d'un nombre

        Rien n'est passé en paramètre, tout le nécessaire est déjà contenu dans l'objet

        Returns:
            void: Rien n'est retourné, cette méthode prépare l'utilisation de la multiplication de Karatsuba-Ofman
        """
        return

    def mult_ko(self, a, b):
        """Méthode de multiplication de Karatsuba-Ofman:
            - Par défaut:  le calcul est fait en base 10:
                + Pouvez-vous le faire dans une base arbitraire self.base?
                + Est-ce que certaines bases seraient avantageuses?
            - Le multiplicateur et le multiplicande sont séparés en deux groupes de chiffres:
                - a = (aH, aL), aH le groupe le plus significatif, aL le groupe le moins significatif
                - b = (bH, bL), bH le groupe le plus significatif, bL le groupe le moins significatif
            - Décalages des résultats partiels (équivalent à une multiplication par 10)
            - Somme des résultats partiels

        Args:
            a (long): Le multiplicande
            b (long): Le multiplicateur

        Returns:
            long: La valeur de (a * b)
        """
        return 42
