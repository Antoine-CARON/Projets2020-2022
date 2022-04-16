donnees=(
("Lille", (2.8,3.4,6.2,9.3,12.6,15.4,17.1,17.3,15.2,11,6.6,3.6), (52,44,49,42,54,60,62,60,60,63,69,58)),
("Turin", (1.4,3.6,8.3,12.6,17.1,20.7,23.6,22.4,18.8,13,6.9,2.9), (38,52,71,97,108,89,55,70,68,86,71,41)),
("Moscou", (-9.2,-8,-2.5,5.9,12.8,16.8,18.4,16.6,11.2,4.9,-1.5,-6.2), (43,35,33,42,49,78,89,76,63,61,57,53)),
("Madrid",  (5,6.4,9.6,12.2,15.8,20.4,24,23.2,19.6,14,8.9,5.4), (43,44,35,45,44,28,11,11,30,51,58,50)),
("Alméria",  (11.8,12.2,14.1,15.8,18.5,21.8,24.8,25.3,23.3,19.3,15.4,12.7), (30,22,22,24,18,9,1,2,13,31,27,29)),
("Berlin",  (-0.9,0,3.9,8.6,13.5,16.8,18.6,18,14.4,10.4,4.4,1), (43,34,35,41,54,70,57,61,44,37,45,49))  )

def ville_dans_liste(ville):
    rep = False
    for i in range(len(donnees)):
        if ville==donnees[i][0]:
            rep=i
    return(rep)
def temp_moyenne(ville,rep):
    moyenne=0
    somme=0
    valeur=0
    for i in range(12):
        valeur=donnees[(rep)][1][i]
        somme=somme+valeur
    moyenne=somme/12
    print(moyenne)
def cumul_precipitation(ville,rep):
    somme2=0
    valeur2=0
    for i in range(12):
        valeur2=donnees[(rep)][2][i]
        somme2=somme2+valeur2
    print(somme2)




saisie=input("Choisissez votre ville")
saisie=str(saisie)
rep=ville_dans_liste(saisie)
if rep==False:
    print("Nous ne possédons pas ces valeurs")
else:
    temp_moyenne(saisie,rep)
    cumul_precipitation(saisie,rep)










