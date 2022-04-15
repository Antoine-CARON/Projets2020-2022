from random import randint



class Pokémon:
    def __init__ (self,PV,Attaque,Nom,Element,Vitesse):
        self.PV=PV
        self.Attaque=Attaque
        self.Nom=Nom
        self.Element=Element
        self.Vitesse=Vitesse
    def aide(self):
        	print("Pour que le joueur 1 choisisse sont pokemon il faut qu'il tape le nom de son pokemon avant le '.combat'")
        	print("Pour que le joueur 2 ai un pokemon il faut qu'il tape le nom de celui ci entre les parentheses du '.combat' avant de mettre la virgule")
        	print("Pour choisir un mode de jeux il faut taper 0 ou 9 apres la virgule entre les parentheses du '.combat'")
        	print("Pour creer un pokemon il faut lui ecrire un nom puis .Pokémon et entre parentheses ses pv puis ses points d'attaques puis le nom entre guillemet tout comme son element juste apres enfin mettre ses point de vitesse")
        	print(" les elements sont orthogarphies comme ceci :électricité,terre,plante,normal,combat,eau et feu")
        	
        	
        	
    def change_att(self,ennemi):
        if ennemi.Element=="feu" and self.Element=="eau":
        	ennemi.Attaque//=2
        	self.Attaque*=2        	
         

        elif ennemi.Element=="eau" and self.Element=="feu":
        	ennemi.Attaque*=2
        	self.Attaque//=2        	
        	

        elif ennemi.Element=='eau' and self.Element=="électricité":
            ennemi.Attaque//=2
            self.Attaque*=2
            
            
        elif ennemi.Element=='électricité' and self.Element=="eau":
            ennemi.Attaque*=2
            self.Attaque//=2
            
            
        elif ennemi.Element=='plante' and self.Element=="feu":
            ennemi.Attaque//=2
            self.Attaque*=2
            
            
        elif ennemi.Element=='feu' and self.Element=="plante":
            ennemi.Attaque*=2
            self.Attaque//=2
            
            
        elif ennemi.Element=='plante' and self.Element=="eau":
            ennemi.Attaque*=2
            self.Attaque//=2
            
            
        elif ennemi.Element=='eau' and self.Element=="plante":
            ennemi.Attaque//=2
            self.Attaque*=2
            
            
        elif ennemi.Element=='normal' and self.Element=="combat":
            self.Attaque*=2
            
            
        elif ennemi.Element=='terre' and self.Element=="électricité":
            ennemi.Attaque*=2
            self.Attaque//=2
            
            
        elif ennemi.Element=='électricité' and self.Element=="terre":
            ennemi.Attaque//=2
            self.Attaque*=2
            
            
        elif ennemi.Element=='combat' and self.Element=="normal":
            ennemi.Attaque*=2
            
        return self.Attaque and ennemi.Attaque



    def chang_pv(self,pv_chang):#changer la vie en retirant pv
        self.PV-=pv_chang
        return self.PV

    def Attaquer (self,ennemi):# ataquer perso en changeant sa vie en utilisant fonction change pv en retirant nb degats Attaque en pv
    	ennemi.chang_pv(self.Attaque)
    	return ennemi.PV

    def combat(self,ennemi,tir):
        sor=tir#tirer au sort 1er qui Attaque
        winner=0
        
        




        if sor==0:
            sor=randint(1,2)
            print("Le joueur",sor,"va commencer!")
            print("Vous jouer en mode simple :")
            print("-le joueur commançant sera tiré au sort")
            print("-les éléments des pokémon n'influencent pas le combat")

        if sor==9:
            if self.Vitesse>ennemi.Vitesse:
                sor=1
                print ("Le joueur",sor,"va commencer!")
            elif self.Vitesse<ennemi.Vitesse:
                sor=2
                print ("Le joueur",sor,"va commencer!")
            else:
                sor=randint(1,2)
                print ("Le joueur",sor,"va commencer!")
            self.change_att(ennemi)#changer attaque des pokemon en fonction de leur elements pour qu'ils est un impact sur le combat
            print("Point d'attaque du joueur 1:",self.Attaque)
            print("Point d'attaque du joueur 2:", ennemi.Attaque)
            print("Vous jouer en mode complexe :")
            print("-le joueur commançant sera sera celui avec la plus grande vitesse ; si les deux pokémon ont la même vitesse l'un des deux sera tiré au sort")
            print("-les éléments des pokémon influencent le combat")


        while ennemi.PV>0 or self.PV>0:#tant que les joueurs sont vivant ils combattent
            if ennemi.PV<=0 :#si l'ennemi est mort alors le j1  a gagner'
                winner=self.Nom
                return winner
            elif self.PV<=0: #si on est mort allors le j2 a gagner
                    winner=ennemi.Nom
                    winner
                    return winner
                    
                    
            elif sor==1:
                self.Attaquer(ennemi)
                #print (sor)
                print("Point de vie du joueur 2:",ennemi.PV)
                sor=3
                self.combat(ennemi,sor)
                
                
            elif sor==2:
                ennemi.Attaquer(self)
                #print(sor)
                print("Point de vie du joueur 1:",self.PV )
                sor=4
                self.combat(ennemi,sor)
                
            elif sor==4:
                self.Attaquer(ennemi)
                #print(sor)
                print("Point de vie du joueur 2:",ennemi.PV)
                sor=2
                self.combat(ennemi,sor)
                
            elif sor==3:
                ennemi.Attaquer(self)
                #print(sor)
                print("Point de vie du joueur 1:",self.PV )
                sor=1
                self.combat(ennemi,sor)









Goupix = Pokémon(440,70,"Goupix","feu",75)

Bulbizar= Pokémon(565,60,"Bulbizar","plante",60)

Carapuce = Pokémon(625,45,"Carapuce","eau",55)

Pikachu = Pokémon(550,60,"Pikachu","électricité",68)

Ratata = Pokémon(570,50,"Ratata","normal",68)

Salamèche = Pokémon(575,50,"Salamèche","feu",65)

Magicarpe = Pokémon(975,30,"Magicarpe","eau",12)

Machoc = Pokémon(500,65,"Machoc","combat",110)

Racaillou= Pokémon (750,40,"Racaillou","terre",5)

#zz.aide()
#print(gt.combat(zz,0))
print("le gagnant est:",Pikachu.combat(Magicarpe,9))