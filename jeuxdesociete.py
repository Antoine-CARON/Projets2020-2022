from random import randint #permet d'avoir un nombre aléatoire entre 2 nombres compris
import time #permet d'avoir des pauses entre 2 lignes avec une durée choisi

PFCLS = ["Pierre","Feuille","Ciseaux","Lézard","Spock"]#liste avec les 5 choix
def choix_j():
    choix1=input("Choisissez Pierre, Feuille, Ciseaux, Lézard ou Spock \n >>>")#demande à l'utilisateur de choisir
    while choix1 != PFCLS[1] and choix1 != PFCLS[2] and choix1 != PFCLS[0] and choix1 != PFCLS[3] and choix1 != PFCLS[4]:#tant que le joueur n'as pas donné l'1 des 5 choix le programme va lui demander de choisir
        choix1=input("Pierre, Feuille , Ciseaux, Lézard ou Spock!\n >>>")
    print("Vous choisissez: ",choix1)#écrit votre choix dans la barre d'execution
    return choix1

def choix_b():
    choix0 = randint(0, 4)#va choisir un nombre entre 0 et 4; 0 et 4 compris
    print("Le choix de l'ordinateur est",PFCLS[choix0])#Va prendre l'un des 5 choix grace a l index au hasard car choix0 est aléatoire
    return PFCLS[choix0]

def résultat(joueur,bot):

    if joueur==bot:#joueur==choix_j qui est le choix du joueur et bot==choix_b qui est le choix de l' ordinateur
        print("L'ordinateur et vous avez choisi",bot,"! Il y a donc une égalité!")

    elif joueur=="Pierre":#le joueur a choisi pierre
        if bot=="Feuille":#le bot a choisi la feuille il a donc perdu
            print("Vous avez perdu car la feuille entoure la pierre!")
        if bot=="Spock":
            print("Vous avez perdu car Spock détruit la pierre!")
        elif bot=="Ciseaux":
            print("Vous avez gagné car la pierre casse les ciseaux!")
        elif bot=="Lézard":
            print("Vous avez gagné car la pierre écrase le lézard!")

    elif joueur=="Feuille":

        if bot=="Ciseaux":
            print("Vous avez perdu car les ciseaux coupent la feuille!")
        if bot=="Lézard":
            print("Vous avez perdu car lézard mange la feuille!")
        elif bot=="Pierre":
            print("Vous avez gagné car la feuille entoure les ciseaux!")
        elif bot=="Spock":
            print("Vous avez gagné car la feuille repousse Spock!")

    elif joueur=="Lézard":

        if bot=="Pierre":
            print("Vous avez perdu car la pierre écrase le lézard!")
        elif bot=="Ciseaux":
            print("Vous avez perdu car les ciseaux décapitent le lézard!")
        elif bot=="Spock":
            print("Vous avez gagné car le lézard empoisonne Spock!")
        elif bot=="Papier":
            print("Vous avez gagné car lézard mange le papier!")

    elif joueur=="Spock":

        if bot=="Papier":
            print("Vous avez perdu car le papier repousse Spock!")
        elif bot=="Lézard":
            print("Vous avez perdu car le lézard empoisonne Spock!")
        elif bot=="Ciseaux":
            print("Vous avez gagné car Spock écrabouille les ciseaux!")
        elif bot=="Pierre":
            print("Vous avez gagné car Spock détruit la pierre!")

    elif joueur=="Ciseaux":
        if bot=="Pierre":
            print("Vous avez perdu car la pierre casse les ciseaux!")
        elif bot=="Spock":
            print("Vous avez perdu car Spock écrabouille les ciseaux!")
        elif bot=="Feuille":
            print("Vous avez gagné car les ciseaux coupent la feuille!")
        elif bot=="Lézard":
            print("Vous avez gagné car les ciseaux décapitent le lézard!")




def partie():
    print("************************************************\n-Jeu du Pierre, Feuille, Ciseaux, Lézard, Spock- \n************************************************")# "\n" permet de sauter une ligne
    time.sleep(1)# attend 1 sec et execute le script d'apres
    start=input("Connaissez-vous les règles du Pierre, Feuille, Ciseaux, Lézard, Spock ?")
    if start==("oui"):#se lance si la personne a dit qu elle connaissait les règles
        joueur=choix_j()#indique joueur est le script choix_j pour que le résultat sache ce qu'est joueur
        bot=choix_b()#indique bot est le script choix_b pour que le résultat sache ce qu'est bot
        résultat(joueur,bot)
    else:
        print("Les règles sont les mêmes que le pierre, papier, ciseaux classique mais il y a quelques différences:")#règles
        time.sleep(3)#fait une pause de 3 sec
        print(">>>La pierre gagne contre le lézard\n>>>Le lézard gagne contre Spock\n>>>Spock gagne contre la pierre")
        time.sleep(5)# une pause afin que le joueur ne connaissant pas les règles est le temps de les lires
        print(">>>Spock gagne contre les ciseaux\n>>>Les ciseaux gagne contre le lézard")
        time.sleep(5)
        print(">>>Le lézard gagne contre le papier\n>>>Le papier gagne contre Spock")
        time.sleep(5)
        compris=input("Avez-vous compris") #question pour savoir si la personne a compris
        if input==("oui"):
            joueur=choix_j()
            bot=choix_b()
            résultat(joueur,bot)
        else:
            print("Je vous laisse plus de temps pour les connaître")#règles
            time.sleep(2.5)
            print(">>>La pierre gagne contre le lézard\n>>>Le lézard gagne contre Spock\n>>>Spock gagne contre la pierre")
            time.sleep(7.5)#pauses plus longues afin que la personne est plus de temps pour lire et comprendre chaque règle
            print(">>>Spock gagne contre les ciseaux\n>>>Les ciseaux gagne contre le lézard")
            time.sleep(7.5)
            print(">>>Le lézard gagne contre le papier\n>>>Le papier gagne contre Spock")
            time.sleep(7.5)
            joueur=choix_j()
            bot=choix_b()
            résultat(joueur,bot)





partie()#lance le script partie qui est l'ensemble de tou les scripts

