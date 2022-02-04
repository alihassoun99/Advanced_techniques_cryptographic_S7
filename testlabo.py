#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Programme python pour l'évaluation de la performance
#
#
#  Copyright 2007-2022 F. Mailhot et Université de Sherbrooke
#

import numpy
import argparse
import timeit
import labo


class TestLabo:
    """Classe à utiliser pour valider les exercices de laboratoire:

        - Contient tout le nécessaire pour tester le laboratoire.
        - Utilise des objets de type Pgcd, PowerMod et Mult
            +     La description des méthodes à compléter se trouve dans le fichier labo.py

    Pour valider le laboratoire, effectuer:
        - python testlabo.py -all -v
            + Toutes les méthodes seront validées
        - python testlabo.py -help
            + Indique tous les arguments et options disponibles

    Copyright 2007-2022, F. Mailhot et Université de Sherbrooke
    """

    TESTLABO_PGCD_EUCLID = 1
    TESTLABO_PGCD_BINAIRE = 2
    TESTLABO_PGCD_STD = 3
    TESTLABO_EXPOSANT_BINAIRE = 4
    TESTLABO_EXPOSANT_MONTGOMERY = 5
    TESTLABO_EXPOSANT_STD = 6
    TESTLABO_MULT = 7
    TESTLABO_MULT_N2 = 8
    TESTLABO_MULT_KO = 9

    @staticmethod
    def get_pgcd_num(iterations, init):
        """Méthode utilisée pour trouver des séquences de grands nombres qui exigent beaucoup de calculs pour le pgcd.
        Utilisée pour obtenir les valeurs de pgcd1 et de pgcd2 (utilisés pour tester le code du labo)
        Cette méthode n'est pas appelée directement pour ne pas influencer le temps d'exécution des tests
        """

        # Le paramètres pgcd1 et pgcd2 utilisés pour valider le calcul du pgcd ont été obtenus ainsi:
        # pgcd1 = get_pgcd_num(501,1)
        # pgcd2 = get_pgcd_num(500,1)

        t_bot = init
        t_top = init + init
        i = iterations
        t_max = 1
        while i != 0:
            i = i - 1
            t_max = t_top + t_bot
            t_bot = t_top
            t_top = t_max
        return t_max

    @staticmethod
    def appel_vide2(num1, _):
        """Méthode à deux paramètres qui ne fait aucun calcul:
            - Utilisée pour déterminer le temps requis pour faire un simple appel à 2 paramètres

        Returns:
            long: Le premier paramètres est retourné (pour simuler l'appel légitime)
        """
        return num1

    def test_vide2(self, param1, param2):
        """Test d'un appel vide à deux paramètres:
            - Utilisée pour déterminer le temps requis pour faire un simple appel à 2 paramètres

        Returns:
            long: Le résultat de l'appel vide
        """
        self.appel_vide2(param1, param2)

    @staticmethod
    def appel_vide3(param1, _, __):
        """Méthode à trois paramètres qui ne fait aucun calcul:
            - Utilisée pour déterminer le temps requis pour faire un simple appel à 3 paramètres

        Returns:
            long: Le premier paramètres est retourné (pour simuler l'appel légitime)
        """
        return param1

    def test_vide3(self, param1, param2, param3):
        """Test d'un appel vide à trois paramètres:
            - Utilisée pour déterminer le temps requis pour faire un simple appel à 3 paramètres

        Returns:
            long: Le résultat de l'appel vide
        """
        self.appel_vide3(param1, param2, param3)

    def test_euclide(self, param1, param2):
        """Test du calcul du pgcd (plus grand commun diviseur) utilisant la méthode d'Euclide:
            - Appel de la méthode définie dans le fichier labo_config.py

        Returns:
            long: Le résultat du calcul du pgcd basé sur la méthode d'Euclide
        """
        self.pgcd.pgcd_euclide(param1, param2)

    def test_binaire(self, param1, param2):
        """Test du calcul du pgcd (plus grand commun diviseur) utilisant la méthode binaire:
            - Appel de la méthode définie dans le fichier labo.py

        Returns:
            long: Le résultat du calcul du pgcd basé sur la méthode binaire
        """
        self.pgcd.pgcd_binaire(param1, param2)

    def test_pgcd_std(self, param1, param2):
        """Test du calcul du pgcd (plus grand commun diviseur) standard, définie dans numpy:
            - Appel de la méthode définie dans le fichier labo_config.py

        Returns:
            long: Le résultat du calcul du pgcd défini dans numpy
        """
        self.pgcd.pgcd_std(param1, param2)

    def test_power_mod(self, param1, param2):
        """Test de la mise à une puissance (modulo) utilisant la méthode binaire des exposants:
            - Appel de la méthode définie dans le fichier labo.py

        Returns:
            long: Le résultat de l'exponentiation basée sur la multiplication standard
        """
        self.pm.power_mod(param1, param2)

    def test_power_monty(self, param1, param2):
        """Test de la mise à une puissance (modulo) utilisant la multiplication de Montgomery:
            - Appel de la méthode définie dans le fichier labo.py

        Returns:
            long: Le résultat de l'exponentiation basée sur la multiplication de Montgomery
        """
        self.pm.power_monty(param1, param2)

    def test_power_std(self, param1, param2):
        """Test de la mise à une puissance (modulo) standard de Python:
            - Appel de la méthode définie dans le fichier labo_config.py

        Returns:
            long: Le résultat de l'exponentiation standard de Python
        """
        self.pm.power_std(param1, param2)

    def test_mult(self, param1, param2):
        """Test de la multiplication par défaut de Python:
            - Appel de la méthode définie dans le fichier labo_config.py

        Returns:
            long: Le résultat de la multiplication standard de Python
        """
        self.m.mult_std(param1, param2)

    def test_mult_n2(self, param1, param2):
        """Test de la multiplication apprise au primaire (un chiffre à la fois):
            - Appel de la méthode définie dans le fichier labo.py

        Returns:
            long: Le résultat de la multiplication apprise au primaire
        """
        self.m.mult_n2(param1, param2)

    def test_mult_ko(self, param1, param2):
        """Test de la multiplication de Karatsuba-Ofman:
            - Appel de la méthode définie dans le fichier labo.py

        Returns:
            long: Le résultat de la multiplication de Karatsuba-Ofman
        """
        self.m.mult_ko(param1, param2)

    def inner_loop(self, called_func, params):
        """Appel en rafale de la fonction passée en paramètres:
            - Temps initial mesuré
            - Appel de la fonction self.inner_iterations fois
            - Temps final mesuré

        Args:
            called_func (None): La fonction à mesurer
            params ([long]): Vecteur de paramètres utilisés par la fonction à mesurer

        Returns:
            int: Le temps d'exécution de la fonction passée en paramètres
        """
        start_time = timeit.default_timer()

        for i in range(1, self.inner_iterations):
            called_func(*params)

        stop_time = timeit.default_timer()
        return stop_time - start_time

    def setup_iterations(self, test_type):
        """Préparation des tests d'un certain type:
            - Choix de la méthode de test à utiliser
            - Choix de la méthode "à vide" à utiliser
            - Validation du calcul effectué (utilisation des méthodes standard Python)

        Args:
            test_type (int): type de test à effectuer (voir TESTLABO_***)

        Returns:
            bool: Vrai si calcul valide, Faux autrement
        """
        if (
            test_type == self.TESTLABO_PGCD_EUCLID
            or test_type == self.TESTLABO_PGCD_BINAIRE
            or test_type == self.TESTLABO_PGCD_STD
        ):
            if test_type == self.TESTLABO_PGCD_EUCLID:
                print("PGCD Euclide:\t\t\t\t\t\t\t\t", end="")
                self.called_func = self.test_euclide
                op_type = labo.Pgcd.PGCD_EUCLIDE
            elif test_type == self.TESTLABO_PGCD_BINAIRE:
                print("PGCD binaire:\t\t\t\t\t\t\t\t", end="")
                self.called_func = self.test_binaire
                op_type = labo.Pgcd.PGCD_BINAIRE
            else:  # test_type == self.TESTLABO_PGCD_STD:
                print("PGCD standard (version numpy):\t\t\t\t", end="")
                self.called_func = self.test_pgcd_std
                op_type = labo.Pgcd.PGCD_STD
            self.pgcd = labo.Pgcd(op_type)
            labo_res = self.pgcd.pgcd(self.pgcd1, self.pgcd2)
            real_res = numpy.gcd(self.pgcd1, self.pgcd2)
            self.empty_func = self.test_vide2
            self.params = [self.pgcd1, self.pgcd2]
        elif (
            test_type == self.TESTLABO_EXPOSANT_BINAIRE
            or test_type == self.TESTLABO_EXPOSANT_MONTGOMERY
            or test_type == self.TESTLABO_EXPOSANT_STD
        ):
            if test_type == self.TESTLABO_EXPOSANT_BINAIRE:
                print("Methode binaire des exposants:\t\t\t\t", end="")
                self.called_func = tl.test_power_mod
                op_type = labo.PowerMod.MULT_STANDARD
            elif test_type == self.TESTLABO_EXPOSANT_MONTGOMERY:
                print("Methode de Montgomery:\t\t\t\t\t\t", end="")
                self.called_func = tl.test_power_monty
                op_type = labo.PowerMod.MULT_MONTGOMERY
            else:  # test_type == self.TESTLABO_EXPOSANT_STD:
                print("Methode Python standard d'exponentiation:\t", end="")
                self.called_func = tl.test_power_std
                op_type = labo.PowerMod.POWER_MOD_STD
            self.pm = labo.PowerMod(op_type, self.power_n, self.base)
            labo_res = self.pm.power(self.power_a, self.power_w)
            real_res = pow(tl.power_a, tl.power_w, tl.power_n)
            self.empty_func = tl.test_vide2
            self.params = [tl.power_a, tl.power_w]
        elif (
            test_type == self.TESTLABO_MULT
            or test_type == self.TESTLABO_MULT_N2
            or test_type == self.TESTLABO_MULT_KO
        ):
            if test_type == self.TESTLABO_MULT:
                print("Multiplication native Python:\t\t\t\t", end="")
                self.called_func = self.test_mult
                op_type = labo.Mult.MULT_STANDARD
            elif test_type == self.TESTLABO_MULT_N2:
                print("Multiplication école primaire:\t\t\t\t", end="")
                self.called_func = self.test_mult_n2
                op_type = labo.Mult.MULT_N2
            else:  # test_type == self.TESTLABO_MULT_KO:
                print("Multiplication Karatsuba-Ofman:\t\t\t\t", end="")
                self.called_func = self.test_mult_ko
                op_type = labo.Mult.MULT_KO
            self.m = labo.Mult(op_type)
            labo_res = self.m.mult(self.m1, self.m2)
            real_res = self.m1 * self.m2
            self.empty_func = self.test_vide2
            self.params = [self.m1, self.m2]
        else:
            print("Unknown test")
            self.called_func = None
            self.empty_func = None
            self.params = []
            real_res = 0
            labo_res = 0
            exit()

        self.res_ok = real_res == labo_res

    def multiple_calls(self):
        """Exécute en séquence une série d'appels à la méthode sous test:
            - Chaque itération est indépendante
            - Mesure du temps d'exécution du test (chaque test est appelé self.iterations * self.inner_iterations fois)
            - Mesure du temps d'exécution "à vide" (l'appel à une procédure qui ne fait rien)

        Returns:
            void: Les résultats des tests sont enregistrés dans l'objet
        """
        self.total_delay = 0
        self.total_call_delay = 0
        for j in range(0, self.iterations):
            self.total_delay += self.inner_loop(self.called_func, self.params)
            self.total_call_delay += self.inner_loop(self.empty_func, self.params)

    def print_one_test_result(self):
        """Imprime à l'écran le résultat d'un test:
            - Indique le temps moyen d'exécution
            - Indique si la méthode testée calcule le bon résultat (ou non)

        Returns:
            void: Le résultats du test est imprimé
        """
        if self.res_ok:
            print(
                "{:.2e}\tCalcul valide".format(
                    (self.total_delay - self.total_call_delay)
                    / (self.iterations * self.inner_iterations)
                )
            )
        else:
            print(
                "{:.2e}\tCalcul INVALIDE".format(
                    (self.total_delay - self.total_call_delay)
                    / (self.iterations * self.inner_iterations)
                )
            )

    def execute_all_tests(self):
        """Pour chacun des tests dans la liste de tests à effectuer:
            - Initialisation du test
            - Mesure le temps moyen d'exécution du test en faisant de nombreux appels en séquence
            - Imprime les résultats de chacun des tests à l'écran

        Returns:
            void: Les tests sont effectués et les résultats sont affichés à l'écran
        """
        self.res_ok = True
        print("Résultats des tests:")
        for test_type in self.testlist:
            self.setup_iterations(test_type)
            self.multiple_calls()
            self.print_one_test_result()
        return

    def register_test(self, reg_type):
        """Enregistre un test à effectuer d'un certain type:
            - Une validation est effectuée pour empêcher la duplication de tests
            - Chaque test d'un certain type n'est inscrit qu'une seule fois

        Args:
            reg_type (int): Le type de test à effectuer (voir les constantes TESTLABO_*** au début de cette classe)

        Returns:
            void: Le test demandé est ajouté à la liste de tests self.testlist
        """
        if reg_type not in self.testlist:
            self.testlist.append(reg_type)

    def __init__(self):
        """Initialisation d'une nouvelle instance de TestLabo:
            - Ajoute toutes les valeurs par défaut des paramètres utilisés pour les tests
            - Modifie les valeurs redéfinies sur la ligne de commande

        Returns:
            void: Au retour, l'objet est initialisé
        """
        self.setup_and_parse_cli()
        self.testlist = []

        # Selon le type de procedure testée, vous devrez possiblement adapter
        #   le nombre d'itérations globales et le nombre d'appels internes
        # Le produite des deux nombres determine le nombre total d'appels
        self.iterations = 5
        self.inner_iterations = 100

        self.called_func = None
        self.empty_func = None
        self.params = []

        # Les grands nombres suivants sont prédéfinis pour faire les
        # tests, mais si vous le désirez vous pouvez en utiliser d'autres
        # pour faire des tests plus complets.
        #
        # pgcd1:    premier grand nombre utilisé pour le calcul du pgcd
        # pgcd2:    deuxième grand nombre utilisé pour le calcul du pgcd
        # power_a:  nombre à élever à une puissance
        # power_w:  puissance
        # power_n:  base utilisée pour le modulo
        # m1:       premier nombre utilisé pour la multiplication
        # m2:       deuxième nombre utilisé pour la multiplication
        self.pgcd1 = 955620997609204752896986850849030784038174487916669186294134525152075026461787231598163278910835948084128
        self.pgcd2 = 590606256885570541884749772942551428042092906415213688441386695785274827100237057501589632981816458291377
        self.power_a = 1234567
        self.power_w = 9876543210987654321
        self.power_n = 123456789876543212345678987654321
        self.m1 = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
        self.m2 = 9876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210
        self.base = 10

        # self.args contient tout ce que le parser de ligne de commande a obtenu
        if self.args.it:
            self.iterations = int(self.args.it)
        if self.args.inner_it:
            self.inner_iterations = int(self.args.inner_it)
        if self.args.pgcd1:
            self.pgcd1 = int(self.args.pgcd1)
        if self.args.pgcd2:
            self.pgcd2 = int(self.args.pgcd2)
        if self.args.a:
            self.power_a = int(self.args.a)
        if self.args.w:
            self.power_w = int(self.args.w)
        if self.args.n:
            self.power_n = int(self.args.n)
        if self.args.m1:
            self.m1 = int(self.args.m1)
        if self.args.m2:
            self.m2 = int(self.args.m2)
        if self.args.base:
            self.base = int(self.args.base)
        return

    # Si mode verbose, refléter les valeurs des paramètres passés sur la ligne de commande
    def print_verbose(self):
        """Mode verbose, imprime l'ensemble des paramètres utilisés pour ce test:
            - Valeur des paramètres par défaut s'ils n'ont pas été modifiés sur la ligne de commande
            - Ensemble des tests demandés

        Returns:
            void: Ne fait qu'imprimer les valeurs contenues dans self
        """
        if self.args.v:
            print("Mode verbose:")
            print("Itérations: " + str(self.iterations))
            print("Itérations internes: " + str(self.inner_iterations))
            print("Premier nombre pour pgcd: " + str(self.pgcd1))
            print("Deuxième nombre pour pgcd: " + str(self.pgcd2))
            print("Nombre à élever à une puissance: " + str(self.power_a))
            print("Puissance à utiliser: " + str(self.power_w))
            print("Modulo pour l'élévation à une puissance: " + str(self.power_n))
            print("Premier nombre pour multiplication: " + str(self.m1))
            print("Deuxième nombre pour multiplication: " + str(self.m2))

            print("")
            if self.args.all:
                print("Test de l'ensemble des méthodes de calcul")
            else:
                if self.args.pgcd:
                    print("Test de la méthode d'Euclide pour le PGCD")
                    print("Test de la méthode binaire pour le PGCD")
                    print("Test de la méthode standard de calcul du PGCD avec numpy")
                else:
                    if self.args.euclide:
                        print("Test de la méthode d'Euclide pour le PGCD")

                    if self.args.pgcd_binaire:
                        print("Test de la méthode binaire pour le PGCD")

                    if self.args.pgcd_std:
                        print(
                            "Test de la méthode standard de calcul du PGCD avec numpy"
                        )

                if self.args.exposant:
                    print("Test de la méthode binaire des exposants")
                    print(
                        "Test de la méthode de Montgomery appliquée au calcul des exposants"
                    )
                    print("Test de la méthode Python standard de calcul des exposants")
                else:
                    if self.args.exposant_binaire:
                        print("Test de la méthode binaire des exposants")

                    if self.args.exposant_Montgomery:
                        print(
                            "Test de la méthode de Montgomery appliquée au calcul des exposants"
                        )

                    if self.args.exposant_std:
                        print(
                            "Test de la méthode Python standard de calcul des exposants"
                        )

                if self.args.mult:
                    print("Test de la multiplication standard de Python")
                    print("Test de la multiplication du primaire")
                    print("Test de la multiplication de Karatsuba-Ofman")
                else:
                    if self.args.mult_std:
                        print("Test de la multiplication standard de Python")

                    if self.args.mult_prim:
                        print("Test de la multiplication du primaire")

                    if self.args.mult_KO:
                        print("Test de la multiplication de Karatsuba-Ofman")

            print("")
        return

    # ------------------------------------------------------------------------------
    # Vous devez choisir une procedure à tester:
    #   -euclide                : pgcd Euclide
    #   -pgcd_binaire           : pgcd binaire
    #   -pgcd_std               : Méthode standard en Python pour le pgcd
    #   -pgcd                   : Effectue le test des trois méthodes de calcul du pgcd
    #   -exposant_binaire       : Méthode binaire des exposants
    #   -exposant_Montgomery    : Méthode de Montgomery avec methode binaire des exposants
    #   -exposant_std           : Méthode standard (avec numpy) de calcul des exposants
    #   -exposant               : Effectue le test des trois méthodes de calcul des exposants
    #   -mult_std               : Multiplication standard en Python
    #   -mult_prim              : Multiplication traditionnelle
    #   -mult_KO                : Multiplication de Karatsuba-Ofman
    #   -mult                   : Effectue le test des trois méthodes de calcul des exposants
    # ------------------------------------------------------------------------------

    def setup_and_parse_cli(self):
        """Utilise le module argparse pour:
            - Enregistrer les commandes à reconnaître
            - Lire la ligne de commande et créer le champs self.args qui récupère la structure produite

        Returns:
            void: Au retour, toutes les commandes reconnues sont comprises dans self.args
        """
        parser = argparse.ArgumentParser(prog="testlabo.py")
        parser.add_argument(
            "-euclide",
            action="store_true",
            help="Tester l'algorithme d'Euclide standard",
        )
        parser.add_argument("-pgcd_binaire", action="store_true", help="PGCD binaire")
        parser.add_argument(
            "-pgcd", action="store_true", help="PGCD binaire et méthode d'Euclide"
        )
        parser.add_argument(
            "-pgcd_std", action="store_true", help="PGCD standard avec numpy"
        )
        parser.add_argument(
            "-exposant_binaire",
            action="store_true",
            help="Méthode binaire des exposants",
        )
        parser.add_argument(
            "-exposant_Montgomery",
            action="store_true",
            help="Méthode d'exponentiation de Montgomery",
        )
        parser.add_argument(
            "-exposant_std",
            action="store_true",
            help="Méthode standard d'exponentiation",
        )
        parser.add_argument(
            "-exposant",
            action="store_true",
            help="Test des deux méthode d'exponentiation",
        )
        parser.add_argument(
            "-mult_std", action="store_true", help="Multiplication python"
        )
        parser.add_argument(
            "-mult_prim", action="store_true", help="Multiplication école primaire"
        )
        parser.add_argument(
            "-mult_KO", action="store_true", help="Multiplication Karatsuba-Ofman"
        )
        parser.add_argument(
            "-mult",
            action="store_true",
            help="Test des trois méthodes de multiplication",
        )
        parser.add_argument(
            "-all",
            action="store_true",
            help="Test de l'ensemble des méthodes de calcul",
        )
        parser.add_argument("-it", type=int, help="Nombre d'itérations")
        parser.add_argument("-inner_it", type=int, help="Nombre d'itérations internes")
        parser.add_argument("-pgcd1", type=int, help="Nombre 1 pour calculer pgcd")
        parser.add_argument("-pgcd2", type=int, help="Nombre 2 pour calculer pgcd")
        parser.add_argument("-a", type=int, help="Nombre à élever à une puissance")
        parser.add_argument("-w", type=int, help="Puissance à utiliser")
        parser.add_argument(
            "-n", type=int, help="Modulo à utiliser pour la mise à une puissance"
        )
        parser.add_argument(
            "-base",
            type=int,
            help="Base utilisée pour le calcul de Montgomery (typiquement 2 ou 10)",
        )
        parser.add_argument("-m1", type=int, help="Nombre 1 pour calculer produit")
        parser.add_argument("-m2", type=int, help="Nombre 2 pour calculer produit")
        parser.add_argument(
            "-v",
            action="store_true",
            help="Mode verbose, imprime les valeurs de tous les paramètres",
        )
        self.args = parser.parse_args()
        return

    def register_all_tests(self):
        """Pour chacun des tests demandés sur la ligne de commande, appeler self.register_test:
            - Chacun des tests individuels demandé est ajouté
            - Si un test global (par exemple, -pgcd) est appelé, enregistrement de tous les tests de ce type
            - Si -all est utilisé, enregistrement de l'ensemble des tests

        Returns:
            void: Au retour de cette méthode, la liste self.testall contient tous les tests à effectuer
        """
        pas_de_test = True
        if self.args.euclide:
            self.register_test(self.TESTLABO_PGCD_EUCLID)
            pas_de_test = False
        if self.args.pgcd_binaire:
            self.register_test(self.TESTLABO_PGCD_BINAIRE)
            pas_de_test = False
        if self.args.pgcd_std:
            self.register_test(self.TESTLABO_PGCD_STD)
            pas_de_test = False
        if self.args.pgcd:
            self.register_test(self.TESTLABO_PGCD_EUCLID)
            self.register_test(self.TESTLABO_PGCD_BINAIRE)
            self.register_test(self.TESTLABO_PGCD_STD)
            pas_de_test = False
        if self.args.exposant_binaire:
            self.register_test(self.TESTLABO_EXPOSANT_BINAIRE)
            pas_de_test = False
        if self.args.exposant_Montgomery:
            self.register_test(self.TESTLABO_EXPOSANT_MONTGOMERY)
            pas_de_test = False
        if self.args.exposant_std:
            self.register_test(self.TESTLABO_EXPOSANT_STD)
            pas_de_test = False
        if self.args.exposant:
            self.register_test(self.TESTLABO_EXPOSANT_BINAIRE)
            self.register_test(self.TESTLABO_EXPOSANT_MONTGOMERY)
            self.register_test(self.TESTLABO_EXPOSANT_STD)
            pas_de_test = False
        if self.args.mult_std:
            self.register_test(self.TESTLABO_MULT)
            pas_de_test = False
        if self.args.mult_prim:
            self.register_test(self.TESTLABO_MULT_N2)
            pas_de_test = False
        if self.args.mult_KO:
            self.register_test(self.TESTLABO_MULT_KO)
            pas_de_test = False
        if self.args.mult:
            self.register_test(self.TESTLABO_MULT)
            self.register_test(self.TESTLABO_MULT_N2)
            self.register_test(self.TESTLABO_MULT_KO)
            pas_de_test = False
        if self.args.all:
            self.register_test(self.TESTLABO_PGCD_BINAIRE)
            self.register_test(self.TESTLABO_PGCD_EUCLID)
            self.register_test(self.TESTLABO_PGCD_STD)
            self.register_test(self.TESTLABO_EXPOSANT_BINAIRE)
            self.register_test(self.TESTLABO_EXPOSANT_MONTGOMERY)
            self.register_test(self.TESTLABO_EXPOSANT_STD)
            self.register_test(self.TESTLABO_MULT_N2)
            self.register_test(self.TESTLABO_MULT_KO)
            self.register_test(self.TESTLABO_MULT)
            pas_de_test = False
        if pas_de_test:
            print("Pas de test à effectuer!")
            exit(1)
        return


if __name__ == "__main__":
    tl = TestLabo()
    tl.print_verbose()
    tl.register_all_tests()
    tl.execute_all_tests()
