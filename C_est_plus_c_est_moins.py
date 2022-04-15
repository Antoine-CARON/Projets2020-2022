import os
import random as rd
nombreTire = rd.randint(0, 100000)  #La fonction "randint" de la bibliothèque « random » tire un nombre entier
print ("\t\t    === JEU DU C'EST PLUS, C'EST MOI?S ===\n\n")

nombreTape = 0

while nombreTape != nombreTire :
      print("Tapez un nombre entier :")
      nombreTape = int(input())
      if nombreTape > nombreTire :
            print("c'est moins\n\n")

      elif nombreTape < nombreTire:
            print("c'est plus\n\n")

      else :
            print("c'est gagné")